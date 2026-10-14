
"""Conservative adapter for the public Telangana RERA search portal."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen
import re
import ssl

import truststore

OFFICIAL_SEARCH_URL = "https://rerait.telangana.gov.in/searchlist/search"
OFFICIAL_HOME_URL = "https://rerait.telangana.gov.in/"
USER_AGENT = "Mozilla/5.0 (compatible; PropertyGuard/1.0)"


class _TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows: list[list[str]] = []
        self.links: list[list[dict[str, str]]] = []
        self._in_table = False
        self._in_row = False
        self._in_cell = False
        self._cell: list[str] = []
        self._row: list[str] = []
        self._row_links: list[dict[str, str]] = []
        self._text: list[str] = []
        self._current_link: dict[str, str] | None = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag.lower() == "table":
            self._in_table = True
        if self._in_table and tag.lower() == "tr":
            self._in_row = True
            self._row = []
            self._row_links = []
        if self._in_row and tag.lower() in ("td", "th"):
            self._in_cell = True
            self._cell = []
        if self._in_row and tag.lower() == "a":
            self._current_link = {
                "href": attrs.get("href", ""),
                "title": attrs.get("title", ""),
                "text": "",
            }

    def handle_data(self, data):
        self._text.append(data)
        if self._in_cell:
            self._cell.append(data)
        if self._current_link is not None:
            self._current_link["text"] += data

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "a" and self._current_link is not None:
            self._row_links.append(self._current_link)
            self._current_link = None
        if self._in_cell and tag in ("td", "th"):
            self._row.append(" ".join(" ".join(self._cell).split()))
            self._in_cell = False
        if self._in_row and tag == "tr":
            if any(self._row):
                self.rows.append(self._row)
                self.links.append(self._row_links)
            self._in_row = False
        if tag == "table":
            self._in_table = False


@dataclass
class ReraCheckResult:
    status: str
    source_url: str
    source_title: str
    registration_number: str
    checked_at: str
    message: str
    matched_project_name: str | None = None
    matched_promoter_name: str | None = None
    evidence: dict | None = None


def _normalise(value: str | None) -> str:
    return re.sub(r"[^A-Z0-9]", "", (value or "").upper())


def verify_telangana_rera(
    registration_number: str,
    expected_project_name: str | None = None,
    expected_promoter_name: str | None = None,
    timeout: float = 15.0,
) -> ReraCheckResult:
    number = (registration_number or "").strip()
    now = datetime.now(timezone.utc).isoformat()

    if not number or len(number) > 150 or not re.fullmatch(
        r"[A-Za-z0-9./_-]+", number
    ):
        return ReraCheckResult(
            "INVALID_INPUT",
            OFFICIAL_HOME_URL,
            "Telangana RERA",
            number,
            now,
            "Provide a valid registration-number string before checking the official portal.",
        )

    url = OFFICIAL_SEARCH_URL + "?" + urlencode({"CertficateNo": number})
    request = Request(url, headers={"User-Agent": USER_AGENT})
    context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    try:
        with urlopen(request, timeout=timeout, context=context) as response:
            html = response.read(2_000_000).decode("utf-8", errors="replace")
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return ReraCheckResult(
            "SOURCE_UNAVAILABLE",
            url,
            "Telangana RERA",
            number,
            now,
            f"Official portal could not be reliably queried ({type(exc).__name__}). No verification conclusion was made.",
            evidence={"error_type": type(exc).__name__},
        )

    parser = _TableParser()
    parser.feed(html)
    number_norm = _normalise(number)
    candidates = []

    # The number in the search form is not proof of a result match.
    # Require the exact normalized number to occur in a result-table row.
    for index, row in enumerate(parser.rows):
        row_text = " | ".join(row)
        if number_norm and number_norm in _normalise(row_text):
            candidates.append((index, row, parser.links[index]))

    if len(candidates) > 1:
        return ReraCheckResult(
            "NEEDS_REVIEW",
            url,
            "Telangana RERA",
            number,
            now,
            "Multiple result rows appear to match; manual confirmation is required.",
            evidence={"candidate_rows": [item[1] for item in candidates[:10]]},
        )

    if len(candidates) == 1:
        _, row, row_links = candidates[0]
        row_text = " | ".join(row)
        project_name = row[1] if len(row) > 1 else None
        promoter_name = row[2] if len(row) > 2 else None

        project_match = (
            _normalise(expected_project_name) in _normalise(row_text)
            if expected_project_name
            else None
        )
        promoter_match = (
            _normalise(expected_promoter_name) in _normalise(row_text)
            if expected_promoter_name
            else None
        )

        evidence = {
            "matched_row": row,
            "links": [
                {
                    "text": link["text"].strip(),
                    "title": link["title"],
                    "url": urljoin(url, link["href"]),
                }
                for link in row_links
            ],
            "project_name_match": project_match,
            "promoter_name_match": promoter_match,
        }

        if project_match is False or promoter_match is False:
            return ReraCheckResult(
                "MISMATCH",
                url,
                "Telangana RERA",
                number,
                now,
                "The official result row appears inconsistent with the supplied project/promoter details. Admin review is required.",
                project_name,
                promoter_name,
                evidence,
            )

        revocation_links = [
            link for link in row_links
            if "revocation" in (
                link["text"] + " " + link["title"] + " " + link["href"]
            ).lower()
        ]

        if revocation_links:
            evidence["revocation_indicators"] = [
                {
                    "text": link["text"].strip(),
                    "title": link["title"],
                    "url": urljoin(url, link["href"]),
                }
                for link in revocation_links
            ]
            return ReraCheckResult(
                "REVOCATION_INDICATED",
                url,
                "Telangana RERA",
                number,
                now,
                "The official search result links to a revocation order. Do not treat this record as an active registration without reviewing the official order and confirming its current legal status.",
                project_name,
                promoter_name,
                evidence,
            )

        # Even a row match is not sufficient to assert that registration
        # is currently active. Keep it as a review outcome until status is
        # established from authoritative evidence.
        return ReraCheckResult(
            "NEEDS_REVIEW",
            url,
            "Telangana RERA",
            number,
            now,
            "A matching result row was found, but the current registration status has not been independently established. Confirm the official record before relying on it.",
            project_name,
            promoter_name,
            evidence,
        )

    body_text = " ".join(" ".join(parser._text).split()).lower()
    if any(
        marker in body_text
        for marker in ("captcha", "enter the text below", "search project details")
    ):
        status = "MANUAL_REVIEW_REQUIRED"
        message = "The portal did not expose an unambiguous registration result and may require interactive search/CAPTCHA. Confirm manually on the official portal."
    else:
        status = "NEEDS_REVIEW"
        message = "No unambiguous matching result row was found. This is not proof that the registration is invalid; verify manually on the official portal."

    return ReraCheckResult(
        status,
        url,
        "Telangana RERA",
        number,
        now,
        message,
        evidence={"response_excerpt": body_text[:1200]},
    )
