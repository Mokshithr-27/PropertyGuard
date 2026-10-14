"""
PropertyGuard OCR Dedicated Celery Application
----------------------------------------------
Configures an isolated Celery application instance bound to the 'ocr' queue,
routing heavyweight PaddleOCR processing away from standard API workers.
"""

from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()


REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0",
)


ocr_celery_app = Celery(
    "propertyguard_ocr",
    broker=REDIS_URL,
    backend=REDIS_URL,
)


ocr_celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_default_queue="ocr",
)


ocr_celery_app.conf.imports = (
    "app.ocr_worker.tasks",
)