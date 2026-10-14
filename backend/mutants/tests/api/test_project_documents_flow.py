"""
PropertyGuard Project Documents Workflow API Test Suite
--------------------------------------------------------
Tests document requirement retrieval by property type (APARTMENT, VILLA, COMMERCIAL),
file validation, upload flows, and builder project permission boundaries.
"""

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




def _fake_builder_user(*, role="BUILDER"):
    return SimpleNamespace(
        id=uuid4(),
        full_name="Test Builder",
        roles=[SimpleNamespace(role=SimpleNamespace(name=role))],
    )


def _fake_project(*, builder_id):
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc)
    return SimpleNamespace(
        id=uuid4(),
        builder_id=builder_id,
        name="Secure Test Project",
        description="Security test",
        project_type="APARTMENT",
        address="Hyderabad, Telangana",
        status="DRAFT",
        created_at=now,
        updated_at=now,
        versions=[],
        deleted_at=None,
    )


def test_create_project_requires_builder_profile(monkeypatch):
    fake_user = _fake_builder_user()
    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: None)

    try:
        response = client.post(
            "/api/v1/projects",
            json={
                "name": "Unauthorized Project",
                "description": "Should not be created",
                "project_type": "APARTMENT",
                "address": "Hyderabad",
            },
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Builder profile not found"
    finally:
        app.dependency_overrides.clear()


def test_create_project_requires_verified_builder(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(
        id=uuid4(),
        user_id=fake_user.id,
        verification_status="PENDING",
    )
    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)

    def fail_if_called(*args, **kwargs):
        raise AssertionError("create_project must not be called for an unverified builder")

    monkeypatch.setattr(project_router, "create_project", fail_if_called)

    try:
        response = client.post(
            "/api/v1/projects",
            json={
                "name": "Unverified Project",
                "project_type": "APARTMENT",
                "address": "Hyderabad",
            },
        )
        assert response.status_code == 403
        assert response.json()["detail"] == "Builder must be VERIFIED to create projects"
    finally:
        app.dependency_overrides.clear()


def test_create_project_allows_verified_builder(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(
        id=uuid4(),
        user_id=fake_user.id,
        verification_status="VERIFIED",
    )
    fake_project = _fake_project(builder_id=fake_profile.id)

    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)
    monkeypatch.setattr(project_router, "create_project", lambda *args, **kwargs: fake_project)

    try:
        response = client.post(
            "/api/v1/projects",
            json={
                "name": fake_project.name,
                "description": fake_project.description,
                "project_type": fake_project.project_type,
                "address": fake_project.address,
            },
        )
        assert response.status_code == 201
        assert response.json()["id"] == str(fake_project.id)
    finally:
        app.dependency_overrides.clear()


def test_get_project_requires_project_access(monkeypatch):
    fake_user = _fake_builder_user(role="BUYER")
    app.dependency_overrides[get_current_user] = lambda: fake_user

    try:
        response = client.get(f"/api/v1/projects/{uuid4()}")
        assert response.status_code == 403
        assert "role required" in response.json()["detail"]
    finally:
        app.dependency_overrides.clear()


def test_get_project_builder_can_only_access_owned_project(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(id=uuid4(), user_id=fake_user.id)

    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)
    monkeypatch.setattr(project_router, "get_builder_project", lambda db, project_id, builder_id: None)

    try:
        response = client.get(f"/api/v1/projects/{uuid4()}")
        assert response.status_code == 404
        assert response.json()["detail"] == "Project not found"
    finally:
        app.dependency_overrides.clear()


def test_get_project_admin_can_access_project(monkeypatch):
    fake_user = _fake_builder_user(role="ADMIN")
    fake_project = _fake_project(builder_id=uuid4())

    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_project", lambda db, project_id: fake_project)

    try:
        response = client.get(f"/api/v1/projects/{fake_project.id}")
        assert response.status_code == 200
        assert response.json()["id"] == str(fake_project.id)
    finally:
        app.dependency_overrides.clear()


def test_delete_project_soft_deletes_and_preserves_history(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(id=uuid4(), user_id=fake_user.id)
    fake_project = _fake_project(builder_id=fake_profile.id)

    class FakeQuery:
        def filter(self, *args):
            return self

        def first(self):
            return fake_project

    class FakeDB:
        def __init__(self):
            self.deleted = False
            self.committed = False

        def query(self, model):
            return FakeQuery()

        def commit(self):
            self.committed = True

        def refresh(self, obj):
            return None

        def delete(self, obj):
            self.deleted = True

    fake_db = FakeDB()
    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_db] = lambda: fake_db
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)

    try:
        response = client.delete(f"/api/v1/projects/{fake_project.id}")
        assert response.status_code == 200
        assert response.json()["status"] == "DELETED"
        assert fake_project.deleted_at is not None
        assert fake_project.status == "INACTIVE"
        assert fake_db.committed is True
        assert fake_db.deleted is False
    finally:
        app.dependency_overrides.clear()


def test_update_project_requires_project_role(monkeypatch):
    fake_user = _fake_builder_user(role="BUYER")
    app.dependency_overrides[get_current_user] = lambda: fake_user

    try:
        response = client.patch(
            f"/api/v1/projects/{uuid4()}",
            json={
                "name": "Updated Project",
                "description": "Updated",
                "project_type": "APARTMENT",
                "address": "Hyderabad",
            },
        )
        assert response.status_code == 403
        assert "role required" in response.json()["detail"]
    finally:
        app.dependency_overrides.clear()


def test_builder_can_modify_owned_project(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(id=uuid4(), user_id=fake_user.id)
    fake_project = _fake_project(builder_id=fake_profile.id)

    class FakeDB:
        def commit(self):
            pass

        def refresh(self, obj):
            pass

    fake_db = FakeDB()
    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_db] = lambda: fake_db
    monkeypatch.setattr(project_router, "get_project", lambda db, project_id: fake_project)
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)

    try:
        response = client.patch(
            f"/api/v1/projects/{fake_project.id}",
            json={
                "name": "Builder Updated Project",
                "description": "Updated by builder",
                "project_type": "VILLA",
                "address": "Secunderabad, Telangana",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Builder Updated Project"
        assert data["project_type"] == "VILLA"
        assert data["address"] == "Secunderabad, Telangana"
        assert fake_project.name == "Builder Updated Project"
    finally:
        app.dependency_overrides.clear()


def test_builder_cannot_modify_unowned_project(monkeypatch):
    fake_user = _fake_builder_user()
    fake_profile = SimpleNamespace(id=uuid4(), user_id=fake_user.id)
    fake_project = _fake_project(builder_id=uuid4())

    app.dependency_overrides[get_current_user] = lambda: fake_user
    monkeypatch.setattr(project_router, "get_project", lambda db, project_id: fake_project)
    monkeypatch.setattr(project_router, "get_builder_profile", lambda db, user_id: fake_profile)

    try:
        response = client.patch(
            f"/api/v1/projects/{fake_project.id}",
            json={
                "name": "Unauthorized Update",
                "description": "Should not update",
                "project_type": "APARTMENT",
                "address": "Hyderabad",
            },
        )
        assert response.status_code == 403
        assert response.json()["detail"] == "Not authorized to modify this project"
    finally:
        app.dependency_overrides.clear()


def test_admin_can_modify_any_project(monkeypatch):
    fake_user = _fake_builder_user(role="ADMIN")
    fake_project = _fake_project(builder_id=uuid4())

    class FakeDB:
        def commit(self):
            pass

        def refresh(self, obj):
            pass

    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_db] = lambda: FakeDB()
    monkeypatch.setattr(project_router, "get_project", lambda db, project_id: fake_project)

    try:
        response = client.patch(
            f"/api/v1/projects/{fake_project.id}",
            json={
                "name": "Admin Updated Project",
                "description": "Updated by admin",
                "project_type": "INDIVIDUAL_HOUSE",
                "address": "Hyderabad, Telangana",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Admin Updated Project"
        assert data["project_type"] == "INDIVIDUAL_HOUSE"
    finally:
        app.dependency_overrides.clear()
