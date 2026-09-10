import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://propertyguard:propertyguard_dev_password@localhost:5432/propertyguard",
)

MINIO_ENDPOINT = os.getenv(
    "MINIO_ENDPOINT",
    "localhost:9000",
)

MINIO_ACCESS_KEY = os.getenv(
    "MINIO_ACCESS_KEY",
    "propertyguard_admin",
)

MINIO_SECRET_KEY = os.getenv(
    "MINIO_SECRET_KEY",
    "propertyguard_minio_password",
)

MINIO_BUCKET = os.getenv(
    "MINIO_BUCKET",
    "propertyguard-documents",
)

MINIO_SECURE = os.getenv(
    "MINIO_SECURE",
    "false",
).lower() == "true"


JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "CHANGE_THIS_TO_A_RANDOM_SECRET_IN_PRODUCTION",
)

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256",
)

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
        "30",
    )
)