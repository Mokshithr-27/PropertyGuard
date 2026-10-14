# PropertyGuard: Document Extraction → Compliance Evaluation

## What is now connected

1. Uploaded documents continue through the existing asynchronous processing pipeline. Digital PDFs use PyMuPDF; scanned PDFs use the OCR worker.
2. The configured document-analysis provider emits evidence items with field name, value, page number, confidence, source, and supporting quote.
3. Offline `AI_PROVIDER=mock` mode now preserves page text and performs conservative label-based extraction for common fields (for example, `registration_number`, `project_name`, `approval_number`, `certificate_number`, `sanctioned_area`, and `number_of_floors`). It only extracts values explicitly labelled in text; it does not decide compliance.
4. `ComplianceService.build_evidence_context()` uses semantic fields from the latest completed analysis for each latest document version. Raw `page_text` is never used as a rule input.
5. Evidence with confidence below 0.70 or without a confidence value is excluded from automatic rule inputs. Conflicting values for the same field remain unresolved rather than being silently selected. Rules that need missing/untrusted values should return `NEEDS_REVIEW`.
6. The `number_of_floors` field is normalized to an integer before evaluation so numeric rule operators can use it. Unit-bearing area values remain text until a rule/unit normalization contract is defined.
7. The dashboard's project details view now exposes **Run verification** to builder/admin users. It calls the existing evaluation API and displays the persisted results returned by the backend.

## Current limitations

- The offline provider is a label-based development fallback, not a substitute for a stronger document-understanding model. It will not extract fields that do not match its explicit labels.
- The Gemini provider remains the semantic AI provider when configured. AI extraction is evidence, not a legal conclusion.
- Rule evaluation only evaluates the rules actually configured and active in the database. This change does not populate or validate the complete Telangana regulatory rule library.
- A rule-engine result is not the same as checking a registration against an official RERA or municipal source. Official-source verification remains a separate integration.
- The UI intentionally requires a user to trigger evaluation after reviewing processing/evidence; it does not automatically evaluate while asynchronous document jobs may still be running.
- Confidence is a provider-supplied extraction signal, not a probability that a certificate is genuine.

## Local setup

1. Copy `.env.example` to `.env` and set local service credentials. Do not commit `.env`.
2. Install the dependencies from `requirements.txt` in a Python environment compatible with the selected OCR packages.
3. Start PostgreSQL, Redis, and MinIO, then apply migrations with `alembic upgrade head`.
4. Start FastAPI and the configured Celery/OCR workers according to your local setup.
5. Upload a sample document with clearly labelled fields, wait for document processing to complete, open project details, review extracted fields and then click **Run verification**.

## Validation performed for this archive

- Python syntax compilation: passed.
- Offline provider tests: passed.
- Full backend test collection could not run in the archive-validation environment because several declared runtime dependencies were not installed there (including PostgreSQL driver, MinIO client, and Google GenAI SDK). Run the full suite in the project's configured virtual environment after installing requirements.
- Frontend build could not run here because `node_modules` was absent and dependency installation timed out. Run `npm ci`, `npm run build`, and `npm run lint` locally.
