from app.integrations.storage import (
    download_bytes,
    object_exists,
    upload_bytes,
)


OBJECT_NAME = "test/propertyguard-storage-test.txt"
TEST_DATA = b"PropertyGuard storage test successful."


upload_bytes(
    TEST_DATA,
    OBJECT_NAME,
    "text/plain",
)

print("Upload successful:", object_exists(OBJECT_NAME))

downloaded = download_bytes(OBJECT_NAME)

print("Download successful:", downloaded == TEST_DATA)
print("Downloaded content:", downloaded.decode("utf-8"))