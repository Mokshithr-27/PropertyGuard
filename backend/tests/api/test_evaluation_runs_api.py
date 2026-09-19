from app.main import app


from fastapi.testclient import TestClient

from app.main import app

from uuid import uuid4

from datetime import datetime, timezone

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
def test_create_evaluation_run_success(monkeypatch):
    import uuid
    from datetime import datetime, timezone

    project_id = uuid.uuid4()
    builder_user_id = uuid.uuid4()
    builder_profile_id = uuid.uuid4()
    evaluation_run_id = uuid.uuid4()

    builder_user = SimpleNamespace(
        id=builder_user_id,
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )

    builder_profile = SimpleNamespace(
        id=builder_profile_id
    )

    project = SimpleNamespace(
        id=project_id,
        builder_id=builder_profile_id
    )

    evaluation_run = SimpleNamespace(
        id=evaluation_run_id,
        project_id=project_id,
        status="RUNNING",
        started_at=datetime.now(timezone.utc),
        completed_at=None,
        error_message=None,
        created_at=datetime.now(timezone.utc),
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
        lambda db, user_id: builder_profile,
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_project",
        lambda db, project_id_arg, builder_id: project,
    )

    monkeypatch.setattr(
        project_router.ComplianceService,
        "create_evaluation_run",
        lambda self, db, project_id_arg: evaluation_run,
    )

    try:
        response = client.post(
            f"/api/v1/projects/{project_id}/evaluations"
        )

        assert response.status_code == 201

        body = response.json()

        assert body["id"] == str(evaluation_run_id)
        assert body["project_id"] == str(project_id)
        assert body["status"] == "RUNNING"
        assert body["completed_at"] is None
        assert body["error_message"] is None

    finally:
        app.dependency_overrides.clear()

def test_run_evaluation_success(monkeypatch):
    import uuid
    from datetime import datetime, timezone

    project_id = uuid.uuid4()
    builder_user_id = uuid.uuid4()
    builder_profile_id = uuid.uuid4()
    evaluation_run_id = uuid.uuid4()

    builder_user = SimpleNamespace(
        id=builder_user_id,
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )

    builder_profile = SimpleNamespace(
        id=builder_profile_id
    )

    project = SimpleNamespace(
        id=project_id,
        builder_id=builder_profile_id
    )

    evaluation_run = SimpleNamespace(
        id=evaluation_run_id,
        project_id=project_id,
        status="COMPLETED",
        started_at=datetime.now(timezone.utc),
        completed_at=datetime.now(timezone.utc),
        error_message=None,
        created_at=datetime.now(timezone.utc),
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
        lambda db, user_id: builder_profile,
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_project",
        lambda db, project_id_arg, builder_id: project,
    )

    monkeypatch.setattr(
        project_router.ComplianceService,
        "run_evaluation",
        lambda self, db, project_id_arg: evaluation_run,
    )

    try:
        response = client.post(
            f"/api/v1/projects/{project_id}/evaluations/run"
        )

        assert response.status_code == 201

        body = response.json()

        assert body["id"] == str(evaluation_run_id)
        assert body["project_id"] == str(project_id)
        assert body["status"] == "COMPLETED"
        assert body["completed_at"] is not None
        assert body["error_message"] is None

    finally:
        app.dependency_overrides.clear()

def test_get_evaluation_history_success(monkeypatch):
    import uuid
    from datetime import datetime, timezone

    project_id = uuid.uuid4()
    builder_user_id = uuid.uuid4()
    builder_profile_id = uuid.uuid4()
    evaluation_run_id = uuid.uuid4()
    rule_version_id = uuid.uuid4()
    result_id = uuid.uuid4()

    builder_user = SimpleNamespace(
        id=builder_user_id,
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )

    builder_profile = SimpleNamespace(
        id=builder_profile_id
    )

    project = SimpleNamespace(
        id=project_id,
        builder_id=builder_profile_id
    )

    evaluation_run = SimpleNamespace(
        id=evaluation_run_id,
        project_id=project_id,
        status="COMPLETED",
        started_at=datetime.now(timezone.utc),
        completed_at=datetime.now(timezone.utc),
        error_message=None,
        created_at=datetime.now(timezone.utc),
    )

    compliance_result = SimpleNamespace(
        id=result_id,
        project_id=project_id,
        evaluation_run_id=evaluation_run_id,
        rule_version_id=rule_version_id,
        outcome="PASS",
        explanation="Required document exists.",
        dependency_affected=False,
        evaluated_at=datetime.now(timezone.utc),
        created_at=datetime.now(timezone.utc),
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
        lambda db, user_id: builder_profile,
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_project",
        lambda db, project_id_arg, builder_id: project,
    )

    monkeypatch.setattr(
        project_router.ComplianceService,
        "get_project_evaluation_history",
        lambda self, db, project_id_arg: [
            {
                "evaluation_run": evaluation_run,
                "results": [compliance_result],
            }
        ],
    )

    try:
        response = client.get(
            f"/api/v1/projects/{project_id}/evaluations/history"
        )

        assert response.status_code == 200

        body = response.json()

        assert len(body) == 1
        assert body[0]["evaluation_run"]["id"] == str(
            evaluation_run_id
        )
        assert body[0]["evaluation_run"]["status"] == "COMPLETED"
        assert len(body[0]["results"]) == 1
        assert body[0]["results"][0]["outcome"] == "PASS"
        assert body[0]["results"][0]["evaluation_run_id"] == str(
            evaluation_run_id
        )

    finally:
        app.dependency_overrides.clear()


def test_get_evaluation_run_results_success(monkeypatch):
    project_id = uuid4()
    evaluation_run_id = uuid4()
    result_id = uuid4()
    rule_version_id = uuid4()
    builder_profile_id = uuid4()

    builder_user = SimpleNamespace(
        id=uuid4(),
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )
    builder_profile = SimpleNamespace(
        id=builder_profile_id,
        user_id=builder_user.id,
    )

    project = SimpleNamespace(
        id=project_id,
        builder_id=builder_profile_id,
    )

    evaluation_run = SimpleNamespace(
        id=evaluation_run_id,
        project_id=project_id,
        status="COMPLETED",
        started_at=datetime.now(timezone.utc),
        completed_at=datetime.now(timezone.utc),
        error_message=None,
        created_at=datetime.now(timezone.utc),
    )

    compliance_result = SimpleNamespace(
        id=result_id,
        project_id=project_id,
        evaluation_run_id=evaluation_run_id,
        rule_version_id=rule_version_id,
        outcome="PASS",
        explanation="Required document exists.",
        dependency_affected=False,
        evaluated_at=datetime.now(timezone.utc),
        created_at=datetime.now(timezone.utc),
    )

    app.dependency_overrides[get_current_user] = (
        lambda: builder_user
    )

    app.dependency_overrides[project_router.get_db] = (
        lambda: SimpleNamespace()
    )

    monkeypatch.setattr(
        project_router,
        "get_evaluation_run",
        lambda db, run_id: evaluation_run,
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_profile",
        lambda db, user_id: builder_profile,
    )

    monkeypatch.setattr(
        project_router,
        "get_builder_project",
        lambda db, project_id_arg, builder_id: project,
    )

    monkeypatch.setattr(
        project_router,
        "get_evaluation_run_compliance_results",
        lambda db, run_id: [compliance_result],
    )

    try:
        response = client.get(
            f"/api/v1/projects/{project_id}/evaluations/"
            f"{evaluation_run_id}/results"
        )

        assert response.status_code == 200

        body = response.json()

        assert body["evaluation_run"]["id"] == str(
            evaluation_run_id
        )

        assert body["evaluation_run"]["status"] == "COMPLETED"

        assert len(body["results"]) == 1

        assert body["results"][0]["id"] == str(result_id)

        assert body["results"][0]["outcome"] == "PASS"

        assert body["results"][0]["evaluation_run_id"] == str(
            evaluation_run_id
        )

    finally:
        app.dependency_overrides.clear()

def test_builder_cannot_access_evaluation_run_from_another_project(
    monkeypatch,
):
    project_id = uuid4()
    different_project_id = uuid4()
    evaluation_run_id = uuid4()

    builder_user = SimpleNamespace(
        id=uuid4(),
        roles=[
            SimpleNamespace(
                role=SimpleNamespace(name="BUILDER")
            )
        ],
    )

    evaluation_run = SimpleNamespace(
        id=evaluation_run_id,
        project_id=different_project_id,
        status="COMPLETED",
        started_at=datetime.now(timezone.utc),
        completed_at=datetime.now(timezone.utc),
        error_message=None,
        created_at=datetime.now(timezone.utc),
    )

    app.dependency_overrides[get_current_user] = (
        lambda: builder_user
    )

    app.dependency_overrides[project_router.get_db] = (
        lambda: SimpleNamespace()
    )

    monkeypatch.setattr(
        project_router,
        "get_evaluation_run",
        lambda db, run_id: evaluation_run,
    )

    try:
        response = client.get(
            f"/api/v1/projects/{project_id}/evaluations/"
            f"{evaluation_run_id}/results"
        )

        assert response.status_code == 404
        assert response.json()["detail"] == (
            "Evaluation run not found"
        )

    finally:
        app.dependency_overrides.clear()