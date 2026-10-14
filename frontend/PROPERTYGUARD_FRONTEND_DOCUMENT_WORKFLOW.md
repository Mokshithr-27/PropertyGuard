# PropertyGuard Frontend — Document-First Project Workflow

## What changed

The project dashboard is now a light, minimal workspace and the Builder project-creation flow is document-first after the initial project shell is created.

### Builder flow

1. Builder clicks **New project**.
2. Builder enters the initial project name, property type, address, and optional description.
3. Frontend creates the project through `POST /api/v1/projects`.
4. Frontend immediately retrieves the project-specific required-document catalog through `GET /api/v1/projects/required-documents`.
5. Mandatory documents are clearly marked and must be uploaded before processing can start.
6. Each selected document is sent to `POST /api/v1/documents/validate` before storage.
7. Valid documents are uploaded to MinIO through `POST /api/v1/documents`.
8. The latest document version is queued with `POST /api/v1/documents/versions/{version_id}/process`.
9. The frontend polls the document version status.
10. Text PDFs use the PyMuPDF extraction path. Image-only/scanned PDFs are routed to the dedicated OCR worker and then the AI provider.
11. The frontend retrieves the completed analysis from `GET /api/v1/documents/{document_id}/analysis`.
12. Semantic evidence is displayed to the Builder.
13. Unique `project_name`, `property_name`, `address`, `location`, and `summary` evidence is applied back to the project where supported by the current Project schema.
14. The final project state is refreshed from the backend.

## Important architecture rule

AI/OCR extraction supplies evidence and understanding. It does **not** decide regulatory compliance. Compliance remains deterministic in the backend.

## Light UI

The dashboard, authentication pages, navigation, forms, document workflow, processing state, and evidence panels use a restrained light theme with minimal cards, neutral borders, and blue status accents.

## Backend addition

The frontend requires the new builder-authorized endpoint:

`GET /api/v1/documents/{document_id}/analysis`

This endpoint returns the latest completed analysis and its evidence for a document owned by the authenticated Builder.
