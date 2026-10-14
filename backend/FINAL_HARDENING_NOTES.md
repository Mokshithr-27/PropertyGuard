# PropertyGuard Backend — Final Hardening Checkpoint

## Changes implemented

1. Builder registration now creates the builder profile with `PENDING` verification status.
2. Project creation no longer auto-creates or auto-verifies a missing builder profile.
3. Project creation explicitly requires an existing builder profile with `verification_status == VERIFIED`.
4. `GET /api/v1/projects/{project_id}` now enforces project-level authorization:
   - `ADMIN` / `SUPER_ADMIN`: any non-deleted project.
   - `BUILDER`: only projects owned by that builder.
   - other roles: `403`.
5. The project list no longer exposes the fabricated `compliance_score=85`. The field is `null` until a real score engine is implemented.
6. Projects now support soft deletion through `Project.deleted_at` and `status=INACTIVE`.
7. Deleted projects are excluded from normal project retrieval/listing and builder ownership queries.
8. Building/unit ownership checks and admin project-version approval checks ignore soft-deleted projects.
9. Focused API/service tests were added for builder verification, project access control, soft deletion, and builder registration.
10. Alembic migration `9b7d2a6c4e11_add_project_soft_delete.py` adds `projects.deleted_at` and an index.

## Validation performed in this environment

- All Python source files in `app`, `tests`, and `alembic/versions` were successfully AST/compile parsed.
- Migration chain parsing confirms `9b7d2a6c4e11` is the single new head after `72cc7b4c2798`.
- Full pytest execution could not be completed in this isolated environment because the uploaded project dependencies (`psycopg` and `google-genai`) are not installed here and external package installation is unavailable.

## Run on the development machine

```powershell
cd C:\PROJECT\PropertyGuard\backend
.\.venv\Scripts\activate
alembic upgrade head
alembic check
python -m pytest -v
```

Expected migration state:

```text
Current head: 9b7d2a6c4e11
```

The existing Docker PostgreSQL/Redis/MinIO services should remain running before the API/integration tests that require them.
\n\nAlembic index sync fix: Project.deleted_at now declares index=True to match migration 9b7d2a6c4e11.\n