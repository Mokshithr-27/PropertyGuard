
from io import BytesIO
from unittest.mock import patch
from urllib.error import URLError

from app.services.rera_verification_service import verify_telangana_rera


class FakeResponse(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def fake_response(html):
    return FakeResponse(html.encode() if isinstance(html, str) else html)


def test_matching_result_requires_status_review():
    html = """
    <table>
      <tr><th>Registration</th><th>Project</th><th>Promoter</th></tr>
      <tr><td>P02400001484</td><td>GREEN VALLEY APARTMENTS</td>
          <td>ABC DEVELOPERS</td></tr>
    </table>
    """
    with patch(
        "app.services.rera_verification_service.urlopen",
        return_value=fake_response(html),
    ):
        result = verify_telangana_rera(
            "P02400001484", "Green Valley Apartments", "ABC Developers"
        )

    assert result.status == "NEEDS_REVIEW"
    assert result.matched_project_name == "GREEN VALLEY APARTMENTS"
    assert result.matched_promoter_name == "ABC DEVELOPERS"
    assert result.evidence["project_name_match"] is True
    assert result.evidence["promoter_name_match"] is True
    assert "rerait.telangana.gov.in" in result.source_url


def test_revocation_order_is_not_treated_as_active():
    html = """
    <table>
      <tr><td>P02200003688</td><td>JAYAS PLATINUM</td>
          <td>JAYATHRI INFRASTRUCTURES INDIA PRIVATE LIMITED</td>
          <td><a href="https://rera.telangana.gov.in/Home/Revoked"
                 title="View Details">Revocation Order</a></td></tr>
    </table>
    """
    with patch(
        "app.services.rera_verification_service.urlopen",
        return_value=fake_response(html),
    ):
        result = verify_telangana_rera(
            "P02200003688",
            "JAYAS PLATINUM",
            "JAYATHRI INFRASTRUCTURES INDIA PRIVATE LIMITED",
        )

    assert result.status == "REVOCATION_INDICATED"
    assert result.evidence["revocation_indicators"]
    assert "revocation order" in result.message.lower()
    assert result.status != "VERIFIED"


def test_project_mismatch_never_reports_verified():
    html = """
    <table>
      <tr><td>P02400001484</td><td>OTHER PROJECT</td>
          <td>ABC DEVELOPERS</td></tr>
    </table>
    """
    with patch(
        "app.services.rera_verification_service.urlopen",
        return_value=fake_response(html),
    ):
        result = verify_telangana_rera(
            "P02400001484", "Green Valley Apartments"
        )

    assert result.status == "MISMATCH"


def test_captcha_routes_to_manual_review():
    html = (
        "<html><body>Search Project Details "
        "Enter the text below as you see in the captcha</body></html>"
    )
    with patch(
        "app.services.rera_verification_service.urlopen",
        return_value=fake_response(html),
    ):
        result = verify_telangana_rera("P02400001484")

    assert result.status == "MANUAL_REVIEW_REQUIRED"


def test_no_matching_row_requires_review():
    html = """
    <html><body><div id="div_norecords">
      No Records Found
    </div></body></html>
    """
    with patch(
        "app.services.rera_verification_service.urlopen",
        return_value=fake_response(html),
    ):
        result = verify_telangana_rera("P02400001484")

    assert result.status == "NEEDS_REVIEW"


def test_source_failure_is_not_treated_as_invalid_registration():
    with patch(
        "app.services.rera_verification_service.urlopen",
        side_effect=URLError("offline"),
    ):
        result = verify_telangana_rera("P02400001484")

    assert result.status == "SOURCE_UNAVAILABLE"
    assert "no verification conclusion" in result.message.lower()


def test_invalid_registration_input_does_not_call_network():
    with patch(
        "app.services.rera_verification_service.urlopen"
    ) as mock_open:
        result = verify_telangana_rera("bad number !")

    assert result.status == "INVALID_INPUT"
    mock_open.assert_not_called()
