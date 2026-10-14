"""
PropertyGuard PyMuPDF Fast Document Text Extraction Service
-----------------------------------------------------------
Extracts digital text and page structures from PDF documents using PyMuPDF (fitz),
producing ExtractedDocument and ExtractedPage models for downstream AI analysis.
"""

from dataclasses import dataclass

import pymupdf


@dataclass
class ExtractedPage:
    page_number: int
    text: str
    source: str = "PDF_TEXT"


@dataclass
class ExtractedDocument:
    page_count: int
    pages: list[ExtractedPage]

    @property
    def full_text(self) -> str:
        return "\n\n".join(
            page.text
            for page in self.pages
            if page.text.strip()
        )

    @property
    def has_text(self) -> bool:
        return bool(self.full_text.strip())


def extract_pdf_text(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=data, filetype="pdf")
    except Exception as exc:
        raise ValueError("Unable to open PDF document") from exc

    try:
        pages: list[ExtractedPage] = []

        for index, page in enumerate(document):
            text = page.get_text("text").strip()

            pages.append(
                ExtractedPage(
                    page_number=index + 1,
                    text=text,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()