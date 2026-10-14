"""
PropertyGuard OCR Result Adapter Service
----------------------------------------
Transforms dictionary payloads produced by the PaddleOCR Celery worker
into standard ExtractedDocument and ExtractedPage domain models for uniform AI analysis.
"""

from app.services.document_text_extraction_service import (
    ExtractedDocument,
    ExtractedPage,
)


def ocr_result_to_extracted_document(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("page_count")
    pages = ocr_result.get("pages")

    if not isinstance(page_count, int):
        raise ValueError("OCR result must contain an integer page_count")

    if not isinstance(pages, list):
        raise ValueError("OCR result must contain a pages list")

    extracted_pages: list[ExtractedPage] = []

    for page in pages:
        if not isinstance(page, dict):
            raise ValueError("Each OCR page must be a dictionary")

        page_number = page.get("page_number")
        text = page.get("text", "")

        if not isinstance(page_number, int):
            raise ValueError(
                "OCR page must contain an integer page_number"
            )

        if not isinstance(text, str):
            raise ValueError(
                "OCR page text must be a string"
            )

        extracted_pages.append(
            ExtractedPage(
                page_number=page_number,
                text=text.strip(),
                source="OCR",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )