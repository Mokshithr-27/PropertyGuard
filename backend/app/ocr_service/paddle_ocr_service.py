from dataclasses import dataclass

import pymupdf
from paddleocr import PaddleOCR

import numpy as np

@dataclass
class OCRPageResult:
    page_number: int
    text: str
    confidence: float | None


@dataclass
class OCRDocumentResult:
    page_count: int
    pages: list[OCRPageResult]

    @property
    def full_text(self) -> str:
        return "\n\n".join(
            page.text for page in self.pages if page.text.strip()
        )


class PaddleOCRService:
    def __init__(self, language: str = "en") -> None:
        self.ocr = PaddleOCR(lang=language)

    def process_pdf(self, pdf_bytes: bytes) -> OCRDocumentResult:
        if not pdf_bytes:
            raise ValueError("PDF data cannot be empty")

        try:
            document = pymupdf.open(
                stream=pdf_bytes,
                filetype="pdf",
            )
        except Exception as exc:
            raise ValueError("Unable to open PDF document") from exc

        try:
            pages: list[OCRPageResult] = []

            for page_index, page in enumerate(document):
                pixmap = page.get_pixmap(
                    matrix=pymupdf.Matrix(2, 2),
                    alpha=False,
                )

                image_array = np.frombuffer(
                    pixmap.samples,
                    dtype=np.uint8,
                ).reshape(
                    pixmap.height,
                    pixmap.width,
                    pixmap.n,
                )

                result = self.ocr.predict(image_array)

                text_lines: list[str] = []
                scores: list[float] = []

                if result:
                    page_result = result[0]

                    text_lines = page_result.get(
                        "rec_texts",
                        [],
                    )

                    scores = page_result.get(
                        "rec_scores",
                        [],
                    )

                text = "\n".join(
                    line.strip()
                    for line in text_lines
                    if line and line.strip()
                )

                confidence = (
                    sum(scores) / len(scores)
                    if scores
                    else None
                )

                pages.append(
                    OCRPageResult(
                        page_number=page_index + 1,
                        text=text,
                        confidence=confidence,
                    )
                )

            return OCRDocumentResult(
                page_count=len(document),
                pages=pages,
            )

        finally:
            document.close()