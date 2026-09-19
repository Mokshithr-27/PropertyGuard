# PropertyGuard AI

AI-Assisted Property Compliance & Risk Assessment Platform.

## Technology Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- MinIO
- Docker
- React + TypeScript

## Implemented Features

- Authentication and JWT authorization
- Builder and admin roles
- Project and property hierarchy management
- Document upload and versioning
- MinIO document storage
- Compliance rules and rule versions
- Deterministic rule evaluation
- Evaluation run tracking
- Compliance result history

## Backend Setup

1. Configure environment variables using `.env.example`.
2. Start Docker services:

   `docker compose up -d`

3. Run database migrations:

   `alembic upgrade head`

4. Run tests:

   `python -m pytest -v`

## Current Status

The backend foundation, document management, compliance domain, and evaluation run tracking are implemented.

Future work includes AI document extraction, advanced compliance workflows, reporting, frontend integration, and production hardening.
