from celery import Celery

from app.integrations.storage import download_bytes
from app.ocr_service.paddle_ocr_service import PaddleOCRService
from app.ocr_worker.celery_app import (
    REDIS_URL,
    ocr_celery_app,
)


@ocr_celery_app.task
def ocr_health_check() -> dict:
    return {
        "status": "OK",
        "worker": "propertyguard_ocr",
    }


@ocr_celery_app.task
def ocr_process_document(
    storage_key: str,
    version_id: str | None = None,
    job_id: str | None = None,
) -> dict:
    """
    Download a PDF from MinIO and run PaddleOCR.

    When version_id and job_id are supplied, dispatch the
    backend continuation task after successful OCR.
    """

    if not storage_key:
        raise ValueError("storage_key cannot be empty")

    pdf_bytes = download_bytes(storage_key)

    ocr_service = PaddleOCRService()
    result = ocr_service.process_pdf(pdf_bytes)

    ocr_result = {
        "storage_key": storage_key,
        "page_count": result.page_count,
        "pages": [
            {
                "page_number": page.page_number,
                "text": page.text,
                "confidence": page.confidence,
            }
            for page in result.pages
        ],
        "full_text": result.full_text,
    }

    if version_id is not None and job_id is not None:
        backend_app = Celery(
            "propertyguard_ocr_callback",
            broker=REDIS_URL,
            backend=REDIS_URL,
        )

        backend_app.send_task(
            "app.workers.document_tasks.continue_document_processing_after_ocr",
            args=[
                version_id,
                job_id,
                ocr_result,
            ],
        )

    return ocr_result