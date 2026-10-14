"""
PropertyGuard PyMuPDF Fast Document Text Extraction Service
-----------------------------------------------------------
Extracts digital text and page structures from PDF documents using PyMuPDF (fitz),
producing ExtractedDocument and ExtractedPage models for downstream AI analysis.
"""

from dataclasses import dataclass

import pymupdf


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x_extract_pdf_text__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_extract_pdf_text__mutmut)
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


def x_extract_pdf_text__mutmut_orig(data: bytes) -> ExtractedDocument:
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


def x_extract_pdf_text__mutmut_1(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if data:
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


def x_extract_pdf_text__mutmut_2(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError(None)

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


def x_extract_pdf_text__mutmut_3(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("XXPDF data cannot be emptyXX")

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


def x_extract_pdf_text__mutmut_4(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("pdf data cannot be empty")

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


def x_extract_pdf_text__mutmut_5(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF DATA CANNOT BE EMPTY")

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


def x_extract_pdf_text__mutmut_6(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = None
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


def x_extract_pdf_text__mutmut_7(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=None, filetype="pdf")
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


def x_extract_pdf_text__mutmut_8(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=data, filetype=None)
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


def x_extract_pdf_text__mutmut_9(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(filetype="pdf")
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


def x_extract_pdf_text__mutmut_10(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=data, )
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


def x_extract_pdf_text__mutmut_11(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=data, filetype="XXpdfXX")
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


def x_extract_pdf_text__mutmut_12(data: bytes) -> ExtractedDocument:
    """
    Extract text from a PDF while preserving page boundaries.

    This function only performs deterministic PDF text extraction.
    OCR and AI processing are intentionally handled elsewhere.
    """

    if not data:
        raise ValueError("PDF data cannot be empty")

    try:
        document = pymupdf.open(stream=data, filetype="PDF")
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


def x_extract_pdf_text__mutmut_13(data: bytes) -> ExtractedDocument:
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
        raise ValueError(None) from exc

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


def x_extract_pdf_text__mutmut_14(data: bytes) -> ExtractedDocument:
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
        raise ValueError("XXUnable to open PDF documentXX") from exc

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


def x_extract_pdf_text__mutmut_15(data: bytes) -> ExtractedDocument:
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
        raise ValueError("unable to open pdf document") from exc

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


def x_extract_pdf_text__mutmut_16(data: bytes) -> ExtractedDocument:
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
        raise ValueError("UNABLE TO OPEN PDF DOCUMENT") from exc

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


def x_extract_pdf_text__mutmut_17(data: bytes) -> ExtractedDocument:
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
        pages: list[ExtractedPage] = None

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


def x_extract_pdf_text__mutmut_18(data: bytes) -> ExtractedDocument:
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

        for index, page in enumerate(None):
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


def x_extract_pdf_text__mutmut_19(data: bytes) -> ExtractedDocument:
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
            text = None

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


def x_extract_pdf_text__mutmut_20(data: bytes) -> ExtractedDocument:
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
            text = page.get_text(None).strip()

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


def x_extract_pdf_text__mutmut_21(data: bytes) -> ExtractedDocument:
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
            text = page.get_text("XXtextXX").strip()

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


def x_extract_pdf_text__mutmut_22(data: bytes) -> ExtractedDocument:
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
            text = page.get_text("TEXT").strip()

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


def x_extract_pdf_text__mutmut_23(data: bytes) -> ExtractedDocument:
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
                None
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_24(data: bytes) -> ExtractedDocument:
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
                    page_number=None,
                    text=text,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_25(data: bytes) -> ExtractedDocument:
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
                    text=None,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_26(data: bytes) -> ExtractedDocument:
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
                    text=text,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_27(data: bytes) -> ExtractedDocument:
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
                    )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_28(data: bytes) -> ExtractedDocument:
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
                    page_number=index - 1,
                    text=text,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_29(data: bytes) -> ExtractedDocument:
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
                    page_number=index + 2,
                    text=text,
                )
            )

        return ExtractedDocument(
            page_count=len(document),
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_30(data: bytes) -> ExtractedDocument:
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
            page_count=None,
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_31(data: bytes) -> ExtractedDocument:
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
            pages=None,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_32(data: bytes) -> ExtractedDocument:
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
            pages=pages,
        )

    finally:
        document.close()


def x_extract_pdf_text__mutmut_33(data: bytes) -> ExtractedDocument:
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
            )

    finally:
        document.close()

mutants_x_extract_pdf_text__mutmut['_mutmut_orig'] = x_extract_pdf_text__mutmut_orig # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_1'] = x_extract_pdf_text__mutmut_1 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_2'] = x_extract_pdf_text__mutmut_2 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_3'] = x_extract_pdf_text__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_4'] = x_extract_pdf_text__mutmut_4 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_5'] = x_extract_pdf_text__mutmut_5 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_6'] = x_extract_pdf_text__mutmut_6 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_7'] = x_extract_pdf_text__mutmut_7 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_8'] = x_extract_pdf_text__mutmut_8 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_9'] = x_extract_pdf_text__mutmut_9 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_10'] = x_extract_pdf_text__mutmut_10 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_11'] = x_extract_pdf_text__mutmut_11 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_12'] = x_extract_pdf_text__mutmut_12 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_13'] = x_extract_pdf_text__mutmut_13 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_14'] = x_extract_pdf_text__mutmut_14 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_15'] = x_extract_pdf_text__mutmut_15 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_16'] = x_extract_pdf_text__mutmut_16 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_17'] = x_extract_pdf_text__mutmut_17 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_18'] = x_extract_pdf_text__mutmut_18 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_19'] = x_extract_pdf_text__mutmut_19 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_20'] = x_extract_pdf_text__mutmut_20 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_21'] = x_extract_pdf_text__mutmut_21 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_22'] = x_extract_pdf_text__mutmut_22 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_23'] = x_extract_pdf_text__mutmut_23 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_24'] = x_extract_pdf_text__mutmut_24 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_25'] = x_extract_pdf_text__mutmut_25 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_26'] = x_extract_pdf_text__mutmut_26 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_27'] = x_extract_pdf_text__mutmut_27 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_28'] = x_extract_pdf_text__mutmut_28 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_29'] = x_extract_pdf_text__mutmut_29 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_30'] = x_extract_pdf_text__mutmut_30 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_31'] = x_extract_pdf_text__mutmut_31 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_32'] = x_extract_pdf_text__mutmut_32 # type: ignore # mutmut generated
mutants_x_extract_pdf_text__mutmut['x_extract_pdf_text__mutmut_33'] = x_extract_pdf_text__mutmut_33 # type: ignore # mutmut generated