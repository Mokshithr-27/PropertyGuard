from io import BytesIO

from minio import Minio
from minio.error import S3Error

from app.core.config import (
    MINIO_ACCESS_KEY,
    MINIO_BUCKET,
    MINIO_ENDPOINT,
    MINIO_SECRET_KEY,
    MINIO_SECURE,
)


minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=MINIO_SECURE,
)


def ensure_bucket() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if not minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(MINIO_BUCKET)


def upload_bytes(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        object_name,
        BytesIO(data),
        length=len(data),
        content_type=content_type,
    )


def download_bytes(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            MINIO_BUCKET,
            object_name,
        )
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def object_exists(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise
def delete_object(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise