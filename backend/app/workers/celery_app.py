from celery import Celery

from app.core.config import REDIS_URL


celery_app = Celery(
    "propertyguard",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.workers"])

celery_app.conf.imports = (
    "app.workers.tasks",
    "app.workers.document_tasks",
)