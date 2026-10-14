"""
PropertyGuard Multi-Format Document Extraction Service
------------------------------------------------------
Extracts plain raw text from text-based PDF and DOCX files using PyPDF and python-docx.
"""

from io import BytesIO
from pathlib import Path

from docx import Document
from pypdf import PdfReader


def extract_pdf_text(file_bytes: bytes) -> str:
    """Extract text from a text-based PDF."""

    reader = PdfReader(BytesIO(file_bytes))

    pages = []

    for page in reader.pages:
        pages.append(page.extract_text() or "")

    return "\n".join(pages).strip()


def extract_docx_text(file_bytes: bytes) -> str:
    """Extract text from a DOCX file."""

    document = Document(BytesIO(file_bytes))

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs).strip()


def extract_document_text(
    file_bytes: bytes,
    file_name: str,
    mime_type: str,
) -> str:
    """Extract text based on the document format."""

    extension = Path(file_name).suffix.lower()

    if extension == ".pdf" or mime_type == "application/pdf":
        return extract_pdf_text(file_bytes)

    if (
        extension == ".docx"
        or mime_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        return extract_docx_text(file_bytes)

    raise ValueError(
        f"Unsupported document format: {extension or mime_type}"
    )