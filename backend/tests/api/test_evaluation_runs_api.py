from app.main import app


from fastapi.testclient import TestClient

from app.main import app

from types import SimpleNamespace

from app.api.dependencies import get_current_user

from app.api.v1 import project as project_router

client = TestClient(app)

def test_evaluation_runs_endpoints_registered():
    schema = app.openapi()

    path = "/api/v1/projects/{project_id}/evaluations"

    assert path in schema["paths"]

    endpoint = schema["paths"][path]

    assert "post" in endpoint
    assert "get" in endpoint


def test_create_evaluation_run_openapi():
    schema = app.openapi()

    endpoint = schema["paths"][
        "/api/v1/projects/{project_id}/evaluations"
    ]["post"]

    assert endpoint["responses"]["201"]
    assert endpoint["responses"]["422"]


def test_get_evaluation_runs_openapi():
    schema = app.openapi()

    endpoint = schema["paths"][
        "/api/v1/projects/{project_id}/evaluations"
    ]["get"]

    assert endpoint["responses"]["200"]
    assert endpoint["responses"]["422"]

def test_create_evaluation_run_requires_authentication():
    response = client.post(
        "/api/v1/projects/00000000-0000-0000-0000-000000000000/evaluations"
    )

    assert response.status_code == 401


def test_get_evaluation_runs_requires_authentication():
    response = client.get(
        "/api/v1/projects/00000000-0000-0000-0000-000000000000/evaluations"
    )

    assert response.status_code == 401


def test_create_evaluation_run_rejects_unauthorized_role():
    unauthorized_user = SimpleNamespace(
        id="00000000-0000-0000-0000-000000000001",
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUYER")
            )
        ],
    )

    app.dependency_overrides[get_current_user] = (
        lambda: unauthorized_user
    )

    try:
        response = client.post(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000/evaluations"
        )

        assert response.status_code == 403
        assert response.json()["detail"] == (
            "BUILDER or ADMIN role required"
        )
    finally:
        app.dependency_overrides.clear()

def test_builder_cannot_access_unowned_project(monkeypatch):
    builder_user = SimpleNamespace(
        id="00000000-0000-0000-0000-000000000001",
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )

    app.dependency_overrides[get_current_user] = (
        lambda: builder_user
    )

    app.dependency_overrides[project_router.get_db] = (
        lambda: SimpleNamespace()
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_profile",
        lambda db, user_id: SimpleNamespace(id="builder-profile-id"),
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_project",
        lambda db, project_id, builder_id: None,
    )

    try:
        response = client.post(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000/evaluations"
        )

        assert response.status_code == 404
        assert response.json()["detail"] == "Project not found"
    finally:
        app.dependency_overrides.clear()


def test_run_evaluation_endpoint_registered():
    from app.main import app

    openapi_schema = app.openapi()
    paths = openapi_schema["paths"]

    assert "/api/v1/projects/{project_id}/evaluations/run" in paths
    assert "post" in paths[
        "/api/v1/projects/{project_id}/evaluations/run"
    ]


def test_get_evaluation_run_results_openapi():
    schema = app.openapi()

    path = (
        "/api/v1/projects/"
        "{project_id}/evaluations/"
        "{evaluation_run_id}/results"
    )

    assert path in schema["paths"]

    endpoint = schema["paths"][path]["get"]

    assert endpoint["responses"]["200"]
    assert endpoint["responses"]["422"]


def test_evaluation_history_endpoint_registered():
    from app.main import app

    paths = app.openapi()["paths"]

    route = (
        "/api/v1/projects/"
        "{project_id}/evaluations/history"
    )

    assert route in paths
    assert "get" in paths[route]

    response_schema = (
        paths[route]["get"]["responses"]["200"]
        ["content"]["application/json"]["schema"]
    )

    assert response_schema["type"] == "array"
    assert response_schema["items"]["$ref"] == (
        "#/components/schemas/EvaluationRunResultsResponse"
    )