from fastapi import FastAPI

from app.api.v1.documents import router as documents_router

from app.api.v1.builder import router as builder_router

from app.api.v1.admin import router as admin_router

from app.api.v1.auth import router as auth_router

from app.api.v1.project import router as project_router

app = FastAPI(
    title="PropertyGuard API",
    description="AI-Assisted Property Compliance & Risk Assessment Platform",
    version="0.1.0",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)


app.include_router(
    documents_router,
    prefix="/api/v1",
)

app.include_router(
    builder_router,
    prefix="/api/v1",
)

app.include_router(
    admin_router,
    prefix="/api/v1",
)

app.include_router(
    project_router,
    prefix="/api/v1",
)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "propertyguard-backend",
        "version": "0.1.0",
    }