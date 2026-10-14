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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_ocr_result_to_extracted_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_ocr_result_to_extracted_document__mutmut)
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


def x_ocr_result_to_extracted_document__mutmut_orig(
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


def x_ocr_result_to_extracted_document__mutmut_1(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if isinstance(ocr_result, dict):
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


def x_ocr_result_to_extracted_document__mutmut_2(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError(None)

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


def x_ocr_result_to_extracted_document__mutmut_3(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("XXOCR result must be a dictionaryXX")

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


def x_ocr_result_to_extracted_document__mutmut_4(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("ocr result must be a dictionary")

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


def x_ocr_result_to_extracted_document__mutmut_5(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR RESULT MUST BE A DICTIONARY")

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


def x_ocr_result_to_extracted_document__mutmut_6(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = None
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


def x_ocr_result_to_extracted_document__mutmut_7(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get(None)
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


def x_ocr_result_to_extracted_document__mutmut_8(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("XXpage_countXX")
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


def x_ocr_result_to_extracted_document__mutmut_9(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("PAGE_COUNT")
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


def x_ocr_result_to_extracted_document__mutmut_10(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("page_count")
    pages = None

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


def x_ocr_result_to_extracted_document__mutmut_11(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("page_count")
    pages = ocr_result.get(None)

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


def x_ocr_result_to_extracted_document__mutmut_12(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("page_count")
    pages = ocr_result.get("XXpagesXX")

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


def x_ocr_result_to_extracted_document__mutmut_13(
    ocr_result: dict,
) -> ExtractedDocument:
    """
    Convert the JSON result returned by the OCR Celery worker
    into the existing ExtractedDocument representation.
    """

    if not isinstance(ocr_result, dict):
        raise ValueError("OCR result must be a dictionary")

    page_count = ocr_result.get("page_count")
    pages = ocr_result.get("PAGES")

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


def x_ocr_result_to_extracted_document__mutmut_14(
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

    if isinstance(page_count, int):
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


def x_ocr_result_to_extracted_document__mutmut_15(
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
        raise ValueError(None)

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


def x_ocr_result_to_extracted_document__mutmut_16(
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
        raise ValueError("XXOCR result must contain an integer page_countXX")

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


def x_ocr_result_to_extracted_document__mutmut_17(
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
        raise ValueError("ocr result must contain an integer page_count")

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


def x_ocr_result_to_extracted_document__mutmut_18(
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
        raise ValueError("OCR RESULT MUST CONTAIN AN INTEGER PAGE_COUNT")

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


def x_ocr_result_to_extracted_document__mutmut_19(
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

    if isinstance(pages, list):
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


def x_ocr_result_to_extracted_document__mutmut_20(
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
        raise ValueError(None)

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


def x_ocr_result_to_extracted_document__mutmut_21(
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
        raise ValueError("XXOCR result must contain a pages listXX")

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


def x_ocr_result_to_extracted_document__mutmut_22(
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
        raise ValueError("ocr result must contain a pages list")

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


def x_ocr_result_to_extracted_document__mutmut_23(
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
        raise ValueError("OCR RESULT MUST CONTAIN A PAGES LIST")

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


def x_ocr_result_to_extracted_document__mutmut_24(
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

    extracted_pages: list[ExtractedPage] = None

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


def x_ocr_result_to_extracted_document__mutmut_25(
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
        if isinstance(page, dict):
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


def x_ocr_result_to_extracted_document__mutmut_26(
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
            raise ValueError(None)

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


def x_ocr_result_to_extracted_document__mutmut_27(
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
            raise ValueError("XXEach OCR page must be a dictionaryXX")

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


def x_ocr_result_to_extracted_document__mutmut_28(
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
            raise ValueError("each ocr page must be a dictionary")

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


def x_ocr_result_to_extracted_document__mutmut_29(
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
            raise ValueError("EACH OCR PAGE MUST BE A DICTIONARY")

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


def x_ocr_result_to_extracted_document__mutmut_30(
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

        page_number = None
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


def x_ocr_result_to_extracted_document__mutmut_31(
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

        page_number = page.get(None)
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


def x_ocr_result_to_extracted_document__mutmut_32(
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

        page_number = page.get("XXpage_numberXX")
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


def x_ocr_result_to_extracted_document__mutmut_33(
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

        page_number = page.get("PAGE_NUMBER")
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


def x_ocr_result_to_extracted_document__mutmut_34(
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
        text = None

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


def x_ocr_result_to_extracted_document__mutmut_35(
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
        text = page.get(None, "")

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


def x_ocr_result_to_extracted_document__mutmut_36(
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
        text = page.get("text", None)

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


def x_ocr_result_to_extracted_document__mutmut_37(
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
        text = page.get("")

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


def x_ocr_result_to_extracted_document__mutmut_38(
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
        text = page.get("text", )

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


def x_ocr_result_to_extracted_document__mutmut_39(
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
        text = page.get("XXtextXX", "")

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


def x_ocr_result_to_extracted_document__mutmut_40(
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
        text = page.get("TEXT", "")

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


def x_ocr_result_to_extracted_document__mutmut_41(
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
        text = page.get("text", "XXXX")

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


def x_ocr_result_to_extracted_document__mutmut_42(
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

        if isinstance(page_number, int):
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


def x_ocr_result_to_extracted_document__mutmut_43(
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
                None
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


def x_ocr_result_to_extracted_document__mutmut_44(
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
                "XXOCR page must contain an integer page_numberXX"
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


def x_ocr_result_to_extracted_document__mutmut_45(
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
                "ocr page must contain an integer page_number"
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


def x_ocr_result_to_extracted_document__mutmut_46(
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
                "OCR PAGE MUST CONTAIN AN INTEGER PAGE_NUMBER"
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


def x_ocr_result_to_extracted_document__mutmut_47(
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

        if isinstance(text, str):
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


def x_ocr_result_to_extracted_document__mutmut_48(
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
                None
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


def x_ocr_result_to_extracted_document__mutmut_49(
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
                "XXOCR page text must be a stringXX"
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


def x_ocr_result_to_extracted_document__mutmut_50(
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
                "ocr page text must be a string"
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


def x_ocr_result_to_extracted_document__mutmut_51(
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
                "OCR PAGE TEXT MUST BE A STRING"
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


def x_ocr_result_to_extracted_document__mutmut_52(
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
            None
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_53(
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
                page_number=None,
                text=text.strip(),
                source="OCR",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_54(
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
                text=None,
                source="OCR",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_55(
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
                source=None,
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_56(
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
                text=text.strip(),
                source="OCR",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_57(
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
                source="OCR",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_58(
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
                )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_59(
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
                source="XXOCRXX",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_60(
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
                source="ocr",
            )
        )

    return ExtractedDocument(
        page_count=page_count,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_61(
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
        page_count=None,
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_62(
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
        pages=None,
    )


def x_ocr_result_to_extracted_document__mutmut_63(
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
        pages=extracted_pages,
    )


def x_ocr_result_to_extracted_document__mutmut_64(
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
        )

mutants_x_ocr_result_to_extracted_document__mutmut['_mutmut_orig'] = x_ocr_result_to_extracted_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_1'] = x_ocr_result_to_extracted_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_2'] = x_ocr_result_to_extracted_document__mutmut_2 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_3'] = x_ocr_result_to_extracted_document__mutmut_3 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_4'] = x_ocr_result_to_extracted_document__mutmut_4 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_5'] = x_ocr_result_to_extracted_document__mutmut_5 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_6'] = x_ocr_result_to_extracted_document__mutmut_6 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_7'] = x_ocr_result_to_extracted_document__mutmut_7 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_8'] = x_ocr_result_to_extracted_document__mutmut_8 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_9'] = x_ocr_result_to_extracted_document__mutmut_9 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_10'] = x_ocr_result_to_extracted_document__mutmut_10 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_11'] = x_ocr_result_to_extracted_document__mutmut_11 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_12'] = x_ocr_result_to_extracted_document__mutmut_12 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_13'] = x_ocr_result_to_extracted_document__mutmut_13 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_14'] = x_ocr_result_to_extracted_document__mutmut_14 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_15'] = x_ocr_result_to_extracted_document__mutmut_15 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_16'] = x_ocr_result_to_extracted_document__mutmut_16 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_17'] = x_ocr_result_to_extracted_document__mutmut_17 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_18'] = x_ocr_result_to_extracted_document__mutmut_18 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_19'] = x_ocr_result_to_extracted_document__mutmut_19 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_20'] = x_ocr_result_to_extracted_document__mutmut_20 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_21'] = x_ocr_result_to_extracted_document__mutmut_21 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_22'] = x_ocr_result_to_extracted_document__mutmut_22 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_23'] = x_ocr_result_to_extracted_document__mutmut_23 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_24'] = x_ocr_result_to_extracted_document__mutmut_24 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_25'] = x_ocr_result_to_extracted_document__mutmut_25 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_26'] = x_ocr_result_to_extracted_document__mutmut_26 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_27'] = x_ocr_result_to_extracted_document__mutmut_27 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_28'] = x_ocr_result_to_extracted_document__mutmut_28 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_29'] = x_ocr_result_to_extracted_document__mutmut_29 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_30'] = x_ocr_result_to_extracted_document__mutmut_30 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_31'] = x_ocr_result_to_extracted_document__mutmut_31 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_32'] = x_ocr_result_to_extracted_document__mutmut_32 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_33'] = x_ocr_result_to_extracted_document__mutmut_33 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_34'] = x_ocr_result_to_extracted_document__mutmut_34 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_35'] = x_ocr_result_to_extracted_document__mutmut_35 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_36'] = x_ocr_result_to_extracted_document__mutmut_36 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_37'] = x_ocr_result_to_extracted_document__mutmut_37 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_38'] = x_ocr_result_to_extracted_document__mutmut_38 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_39'] = x_ocr_result_to_extracted_document__mutmut_39 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_40'] = x_ocr_result_to_extracted_document__mutmut_40 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_41'] = x_ocr_result_to_extracted_document__mutmut_41 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_42'] = x_ocr_result_to_extracted_document__mutmut_42 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_43'] = x_ocr_result_to_extracted_document__mutmut_43 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_44'] = x_ocr_result_to_extracted_document__mutmut_44 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_45'] = x_ocr_result_to_extracted_document__mutmut_45 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_46'] = x_ocr_result_to_extracted_document__mutmut_46 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_47'] = x_ocr_result_to_extracted_document__mutmut_47 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_48'] = x_ocr_result_to_extracted_document__mutmut_48 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_49'] = x_ocr_result_to_extracted_document__mutmut_49 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_50'] = x_ocr_result_to_extracted_document__mutmut_50 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_51'] = x_ocr_result_to_extracted_document__mutmut_51 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_52'] = x_ocr_result_to_extracted_document__mutmut_52 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_53'] = x_ocr_result_to_extracted_document__mutmut_53 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_54'] = x_ocr_result_to_extracted_document__mutmut_54 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_55'] = x_ocr_result_to_extracted_document__mutmut_55 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_56'] = x_ocr_result_to_extracted_document__mutmut_56 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_57'] = x_ocr_result_to_extracted_document__mutmut_57 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_58'] = x_ocr_result_to_extracted_document__mutmut_58 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_59'] = x_ocr_result_to_extracted_document__mutmut_59 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_60'] = x_ocr_result_to_extracted_document__mutmut_60 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_61'] = x_ocr_result_to_extracted_document__mutmut_61 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_62'] = x_ocr_result_to_extracted_document__mutmut_62 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_63'] = x_ocr_result_to_extracted_document__mutmut_63 # type: ignore # mutmut generated
mutants_x_ocr_result_to_extracted_document__mutmut['x_ocr_result_to_extracted_document__mutmut_64'] = x_ocr_result_to_extracted_document__mutmut_64 # type: ignore # mutmut generated