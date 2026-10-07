from uuid import uuid4
from types import SimpleNamespace
from fastapi.testclient import TestClient
from app.main import app
from app.api.dependencies import get_current_user, get_db
from app.api.v1 import project as project_router
from app.services.project_service import get_required_documents

client = TestClient(app)


def test_required_documents_service_apartment():
    docs = get_required_documents("APARTMENT")
    doc_types = {d["document_type"] for d in docs}
    assert "SANCTIONED_PLAN" in doc_types
    assert "LAND_TITLE" in doc_types
    assert "ENCUMBRANCE_CERTIFICATE" in doc_types
    assert "RERA" in doc_types
    assert "FIRE_NOC" in doc_types

    # For APARTMENT, RERA and FIRE_NOC must be mandatory
    rera = next(d for d in docs if d["document_type"] == "RERA")
    assert rera["is_mandatory"] is True

    fire = next(d for d in docs if d["document_type"] == "FIRE_NOC")
    assert fire["is_mandatory"] is True


def test_required_documents_service_individual_house():
    docs = get_required_documents("INDIVIDUAL_HOUSE")
    doc_types = {d["document_type"] for d in docs}
    assert "SANCTIONED_PLAN" in doc_types
    assert "LAND_TITLE" in doc_types

    rera = next(d for d in docs if d["document_type"] == "RERA")
    assert rera["is_mandatory"] is False

    fire = next(d for d in docs if d["document_type"] == "FIRE_NOC")
    assert fire["is_mandatory"] is False


def test_required_documents_endpoint_openapi():
    schema = app.openapi()
    path = "/api/v1/projects/required-documents"
    assert path in schema["paths"]
    assert "get" in schema["paths"][path]


def test_required_documents_api_success():
    fake_user = SimpleNamespace(
        id=uuid4(),
        roles=[SimpleNamespace(role=SimpleNamespace(name="BUILDER"))],
    )
    app.dependency_overrides[get_current_user] = lambda: fake_user

    try:
        response = client.get("/api/v1/projects/required-documents?project_type=APARTMENT")
        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 5
        types = [d["document_type"] for d in data]
        assert "SANCTIONED_PLAN" in types
        assert "LAND_TITLE" in types
        assert "ENCUMBRANCE_CERTIFICATE" in types
    finally:
        app.dependency_overrides.clear()


def test_list_projects_endpoint_requires_auth():
    response = client.get("/api/v1/projects")
    assert response.status_code in (401, 403)


def test_list_projects_endpoint_success(monkeypatch):
    fake_user = SimpleNamespace(
        id=uuid4(),
        full_name="Apex Developer",
        roles=[SimpleNamespace(role=SimpleNamespace(name="BUILDER"))],
    )
    app.dependency_overrides[get_current_user] = lambda: fake_user

    fake_profile = SimpleNamespace(id=uuid4(), user_id=fake_user.id)
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, uid: fake_profile)
    monkeypatch.setattr(project_router, "get_builder_projects", lambda db, b_id: [])

    try:
        response = client.get("/api/v1/projects")
        assert response.status_code == 200
        assert response.json() == []
    finally:
        app.dependency_overrides.clear()


def test_validate_document_valid_pdf():
    pdf_content = b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\nstartxref\n9\n%%EOF"
    response = client.post(
        "/api/v1/documents/validate",
        files={"file": ("sanction_plan.pdf", pdf_content, "application/pdf")},
        data={"document_type": "SANCTIONED_PLAN"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is True
    assert "PDF" in data["detected_format"]
    assert len(data["sha256"]) == 64
    assert data["error"] is None


def test_validate_document_valid_png():
    png_content = b"\x89PNG\r\n\x1a\n" + b"\x00" * 32
    response = client.post(
        "/api/v1/documents/validate",
        files={"file": ("title_deed.png", png_content, "image/png")},
        data={"document_type": "LAND_TITLE"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is True
    assert "PNG" in data["detected_format"]


def test_validate_document_empty_file_rejected():
    response = client.post(
        "/api/v1/documents/validate",
        files={"file": ("empty.pdf", b"", "application/pdf")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is False
    assert "Empty" in data["detected_format"]
    assert "0 bytes" in data["error"]


def test_validate_document_invalid_format_rejected():
    txt_content = b"This is just a plain text file pretending to be a legal deed."
    response = client.post(
        "/api/v1/documents/validate",
        files={"file": ("fake_deed.pdf", txt_content, "application/pdf")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is False
    assert "Invalid file signature" in data["error"]


def test_update_project_status_requires_auth():
    response = client.patch(
        f"/api/v1/projects/{uuid4()}/status",
        json={"status": "SUSPENDED"},
    )
    assert response.status_code in (401, 403)


def test_delete_project_requires_auth():
    response = client.delete(
        f"/api/v1/projects/{uuid4()}",
    )
    assert response.status_code in (401, 403)


