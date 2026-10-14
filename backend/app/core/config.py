"""
PropertyGuard Application Configuration
----------------------------------------
Loads environment variables from .env to configure PostgreSQL database connection,
Redis broker URL, MinIO S3-compatible storage settings, JWT authentication secrets,
and AI provider parameters (Gemini API, Ollama, Mock).
"""

import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://propertyguard:propertyguard_dev_password@localhost:5432/propertyguard",
)

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0",
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

AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "mock",
)

AI_MODEL_NAME = os.getenv(
    "AI_MODEL_NAME",
    "mock-document-analyzer",
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    "",
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)

OLLAMA_MODEL_NAME = os.getenv(
    "OLLAMA_MODEL_NAME",
    "llama3.1:latest",
)