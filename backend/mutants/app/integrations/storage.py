"""
PropertyGuard MinIO Object Storage Integration
----------------------------------------------
Provides an interface to S3-compatible MinIO object storage for document binaries,
handling bucket creation, byte uploads, downloads, existence checks, and deletion.
"""

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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_ensure_bucket__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_ensure_bucket__mutmut)
def ensure_bucket() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if not minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(MINIO_BUCKET)


def x_ensure_bucket__mutmut_orig() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if not minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(MINIO_BUCKET)


def x_ensure_bucket__mutmut_1() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(MINIO_BUCKET)


def x_ensure_bucket__mutmut_2() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if not minio_client.bucket_exists(None):
        minio_client.make_bucket(MINIO_BUCKET)


def x_ensure_bucket__mutmut_3() -> None:
    """Create the PropertyGuard document bucket if it does not exist."""
    if not minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(None)

mutants_x_ensure_bucket__mutmut['_mutmut_orig'] = x_ensure_bucket__mutmut_orig # type: ignore # mutmut generated
mutants_x_ensure_bucket__mutmut['x_ensure_bucket__mutmut_1'] = x_ensure_bucket__mutmut_1 # type: ignore # mutmut generated
mutants_x_ensure_bucket__mutmut['x_ensure_bucket__mutmut_2'] = x_ensure_bucket__mutmut_2 # type: ignore # mutmut generated
mutants_x_ensure_bucket__mutmut['x_ensure_bucket__mutmut_3'] = x_ensure_bucket__mutmut_3 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_upload_bytes__mutmut)
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


def x_upload_bytes__mutmut_orig(
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


def x_upload_bytes__mutmut_1(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        None,
        object_name,
        BytesIO(data),
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_2(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        None,
        BytesIO(data),
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_3(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        object_name,
        None,
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_4(
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
        length=None,
        content_type=content_type,
    )


def x_upload_bytes__mutmut_5(
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
        content_type=None,
    )


def x_upload_bytes__mutmut_6(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        object_name,
        BytesIO(data),
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_7(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        BytesIO(data),
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_8(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        object_name,
        length=len(data),
        content_type=content_type,
    )


def x_upload_bytes__mutmut_9(
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
        content_type=content_type,
    )


def x_upload_bytes__mutmut_10(
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
        )


def x_upload_bytes__mutmut_11(
    data: bytes,
    object_name: str,
    content_type: str,
) -> None:
    """Upload raw bytes to MinIO."""
    ensure_bucket()

    minio_client.put_object(
        MINIO_BUCKET,
        object_name,
        BytesIO(None),
        length=len(data),
        content_type=content_type,
    )

mutants_x_upload_bytes__mutmut['_mutmut_orig'] = x_upload_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_1'] = x_upload_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_2'] = x_upload_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_3'] = x_upload_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_4'] = x_upload_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_5'] = x_upload_bytes__mutmut_5 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_6'] = x_upload_bytes__mutmut_6 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_7'] = x_upload_bytes__mutmut_7 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_8'] = x_upload_bytes__mutmut_8 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_9'] = x_upload_bytes__mutmut_9 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_10'] = x_upload_bytes__mutmut_10 # type: ignore # mutmut generated
mutants_x_upload_bytes__mutmut['x_upload_bytes__mutmut_11'] = x_upload_bytes__mutmut_11 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_download_bytes__mutmut)
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


def x_download_bytes__mutmut_orig(object_name: str) -> bytes:
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


def x_download_bytes__mutmut_1(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = ""

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


def x_download_bytes__mutmut_2(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = None
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def x_download_bytes__mutmut_3(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            None,
            object_name,
        )
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def x_download_bytes__mutmut_4(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            MINIO_BUCKET,
            None,
        )
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def x_download_bytes__mutmut_5(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            object_name,
        )
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def x_download_bytes__mutmut_6(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            MINIO_BUCKET,
            )
        return response.read()
    finally:
        if response is not None:
            response.close()
            response.release_conn()


def x_download_bytes__mutmut_7(object_name: str) -> bytes:
    """Download an object from MinIO."""
    response = None

    try:
        response = minio_client.get_object(
            MINIO_BUCKET,
            object_name,
        )
        return response.read()
    finally:
        if response is None:
            response.close()
            response.release_conn()

mutants_x_download_bytes__mutmut['_mutmut_orig'] = x_download_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_1'] = x_download_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_2'] = x_download_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_3'] = x_download_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_4'] = x_download_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_5'] = x_download_bytes__mutmut_5 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_6'] = x_download_bytes__mutmut_6 # type: ignore # mutmut generated
mutants_x_download_bytes__mutmut['x_download_bytes__mutmut_7'] = x_download_bytes__mutmut_7 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_object_exists__mutmut)
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


def x_object_exists__mutmut_orig(object_name: str) -> bool:
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


def x_object_exists__mutmut_1(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            None,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_2(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            None,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_3(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_4(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_5(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return False
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_6(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code not in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_7(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"XXNoSuchKeyXX", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_8(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"nosuchkey", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_9(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NOSUCHKEY", "NoSuchObject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_10(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "XXNoSuchObjectXX", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_11(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "nosuchobject", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_12(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NOSUCHOBJECT", "NotFound"}:
            return False
        raise


def x_object_exists__mutmut_13(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "XXNotFoundXX"}:
            return False
        raise


def x_object_exists__mutmut_14(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "notfound"}:
            return False
        raise


def x_object_exists__mutmut_15(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NOTFOUND"}:
            return False
        raise


def x_object_exists__mutmut_16(object_name: str) -> bool:
    """Check whether an object exists in MinIO."""
    try:
        minio_client.stat_object(
            MINIO_BUCKET,
            object_name,
        )
        return True
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return True
        raise

mutants_x_object_exists__mutmut['_mutmut_orig'] = x_object_exists__mutmut_orig # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_1'] = x_object_exists__mutmut_1 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_2'] = x_object_exists__mutmut_2 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_3'] = x_object_exists__mutmut_3 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_4'] = x_object_exists__mutmut_4 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_5'] = x_object_exists__mutmut_5 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_6'] = x_object_exists__mutmut_6 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_7'] = x_object_exists__mutmut_7 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_8'] = x_object_exists__mutmut_8 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_9'] = x_object_exists__mutmut_9 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_10'] = x_object_exists__mutmut_10 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_11'] = x_object_exists__mutmut_11 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_12'] = x_object_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_13'] = x_object_exists__mutmut_13 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_14'] = x_object_exists__mutmut_14 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_15'] = x_object_exists__mutmut_15 # type: ignore # mutmut generated
mutants_x_object_exists__mutmut['x_object_exists__mutmut_16'] = x_object_exists__mutmut_16 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_delete_object__mutmut)
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
def x_delete_object__mutmut_orig(object_name: str) -> None:
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
def x_delete_object__mutmut_1(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            None,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_2(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            None,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_3(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_4(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_5(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code not in {"NoSuchKey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_6(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"XXNoSuchKeyXX", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_7(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"nosuchkey", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_8(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NOSUCHKEY", "NoSuchObject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_9(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "XXNoSuchObjectXX", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_10(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "nosuchobject", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_11(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NOSUCHOBJECT", "NotFound"}:
            return
        raise
def x_delete_object__mutmut_12(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "XXNotFoundXX"}:
            return
        raise
def x_delete_object__mutmut_13(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "notfound"}:
            return
        raise
def x_delete_object__mutmut_14(object_name: str) -> None:
    """Delete an object from MinIO."""
    try:
        minio_client.remove_object(
            MINIO_BUCKET,
            object_name,
        )
    except S3Error as exc:
        if exc.code in {"NoSuchKey", "NoSuchObject", "NOTFOUND"}:
            return
        raise

mutants_x_delete_object__mutmut['_mutmut_orig'] = x_delete_object__mutmut_orig # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_1'] = x_delete_object__mutmut_1 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_2'] = x_delete_object__mutmut_2 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_3'] = x_delete_object__mutmut_3 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_4'] = x_delete_object__mutmut_4 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_5'] = x_delete_object__mutmut_5 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_6'] = x_delete_object__mutmut_6 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_7'] = x_delete_object__mutmut_7 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_8'] = x_delete_object__mutmut_8 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_9'] = x_delete_object__mutmut_9 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_10'] = x_delete_object__mutmut_10 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_11'] = x_delete_object__mutmut_11 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_12'] = x_delete_object__mutmut_12 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_13'] = x_delete_object__mutmut_13 # type: ignore # mutmut generated
mutants_x_delete_object__mutmut['x_delete_object__mutmut_14'] = x_delete_object__mutmut_14 # type: ignore # mutmut generated