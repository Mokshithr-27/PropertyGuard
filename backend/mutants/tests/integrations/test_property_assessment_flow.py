
"""
PropertyGuard AI - Integration Tests
-------------------------------------
Tests the interaction between:
1. FastAPI application and health endpoint
2. Authentication dependency and project document requirements
3. Document requirement retrieval and document validation
4. Evaluation endpoint authentication and authorization
"""

from types import SimpleNamespace
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.dependencies import get_current_user


client = TestClient(app)


@pytest.fixture
def builder_user():
    """Create a simulated authenticated builder."""
    return SimpleNamespace(
        id=uuid4(),
        full_name="Integration Test Builder",
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )


@pytest.fixture
def authenticated_builder(builder_user):
    """Override authentication for this test and restore it afterward."""
    previous = app.dependency_overrides.get(get_current_user)
    app.dependency_overrides[get_current_user] = lambda: builder_user

    yield builder_user

    if previous is None:
        app.dependency_overrides.pop(get_current_user, None)
    else:
        app.dependency_overrides[get_current_user] = previous


def test_health_endpoint():
    """Verify that the FastAPI application responds correctly."""
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "propertyguard-backend"


def test_property_document_workflow(authenticated_builder):
    """
    Integration smoke test:
    Retrieve apartment document requirements, then validate
    a sanctioned-plan PDF through the document API.
    """

    # Step 1: Retrieve required documents for an apartment.
    requirements_response = client.get(
        "/api/v1/projects/required-documents",
        params={"project_type": "APARTMENT"},
    )

    assert requirements_response.status_code == 200

    requirements = requirements_response.json()
    document_types = {
        item["document_type"] for item in requirements
    }

    assert "SANCTIONED_PLAN" in document_types
    assert "LAND_TITLE" in document_types
    assert "RERA" in document_types

    # Step 2: Validate a PDF for one required document.
    pdf_content = (
        b"%PDF-1.4\n"
        b"1 0 obj\n<<>>\nendobj\n"
        b"trailer\n<<>>\n"
        b"startxref\n9\n%%EOF"
    )

    validation_response = client.post(
        "/api/v1/documents/validate",
        files={
            "file": (
                "sanctioned_plan.pdf",
                pdf_content,
                "application/pdf",
            )
        },
        data={"document_type": "SANCTIONED_PLAN"},
    )

    assert validation_response.status_code == 200

    result = validation_response.json()
    assert result["is_valid"] is True
    assert len(result["sha256"]) == 64
    assert result["error"] is None


def test_evaluation_endpoint_requires_authentication():
    """An unauthenticated user must not start an evaluation."""
    response = client.post(
        f"/api/v1/projects/{uuid4()}/evaluations"
    )

    assert response.status_code in (401, 403)


def test_buyer_cannot_start_builder_evaluation():
    """A buyer must not be authorized to start a builder evaluation."""
    buyer = SimpleNamespace(
        id=uuid4(),
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUYER")
            )
        ],
    )

    previous = app.dependency_overrides.get(get_current_user)
    app.dependency_overrides[get_current_user] = lambda: buyer

    try:
        response = client.post(
            f"/api/v1/projects/{uuid4()}/evaluations"
        )

        assert response.status_code == 403
        assert response.json()["detail"] == (
            "BUILDER or ADMIN role required"
        )
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_current_user, None)
        else:
            app.dependency_overrides[get_current_user] = previous
