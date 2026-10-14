# PropertyGuard AI — Evidence, Compliance and Official Verification Integration

## What is included

- Connects the existing structured document-analysis output to evidence-backed deterministic compliance evaluation. The rule evaluator remains the authority for PASS/FAIL/NEEDS_REVIEW/NOT_APPLICABLE; AI does not decide legal compliance.
- Adds/uses the project compliance evaluation API from the project details UI.
- Adds a project-scoped online Telangana RERA check, records the source, result, timestamp, response evidence and checking user, and exposes past verification records.
- Official source adapter points at the Telangana RERA public search portal. It only reports VERIFIED when it finds one unambiguous result row matching the normalized registration number. Portal CAPTCHA, ambiguous responses, unavailable source and no match are not treated as invalid registration; they require manual review.
- Adds a safe `.env.example`. A machine-local `.env` is deliberately excluded from this delivery.
- Normalizes `backend/requirements.txt` to UTF-8 and adds missing processing/provider dependencies used by the code.

## Important limitations

1. The online portal may change markup, require interactive CAPTCHA, block automated access, or return a page that cannot be parsed. The application must show manual review in those cases. Do not bypass CAPTCHA or access controls.
2. An exact registration-number row is a preliminary online match, not a legal opinion. Check project/promoter names, registration status, validity, extensions, revocation/defaulter notices and underlying records on the official site before relying on a result.
3. The configured compliance engine can only validate the rules actually seeded/configured in the database. The complete Telangana 30–40-rule library still needs research against current official sources, citations, applicability, effective dates, and admin review.
4. The full repository test suite and frontend production build could not be confirmed in this environment because the execution image lacks backend packages (including `psycopg`, `minio`, and the Google GenAI SDK) and frontend type packages (`vite/client`, `node`). Python source compilation passed. Run tests in the project's configured environment before replacing your working copy.

## Setup

1. Extract the ZIP into a new folder and keep the original project as backup.
2. Copy `backend/.env.example` to `backend/.env` and set local values/secrets.
3. From `backend`, install dependencies with `python -m pip install -r requirements.txt`.
4. Start Docker Compose dependencies and run `alembic upgrade head` using the configured database URL.
5. Start the API and Celery worker as documented in the backend README.
6. From `frontend`, run `npm ci`, then `npm run build`, then start the dev server.
7. Log in as an authorized Builder/Admin, open a project, run compliance evaluation, and separately check its RERA registration number. Confirm the result links to the official source and review any `NEEDS_REVIEW`/`MANUAL_REVIEW_REQUIRED` outcome manually.

## Validation performed for this bundle

- `python -m compileall -q app`: passed.
- `pytest -q`: collection blocked by missing packages in the execution environment; no full-suite pass is claimed.
- `npm run build`: blocked because `vite/client` and `node` type definitions are not installed; no frontend build pass is claimed.
- Official portal URL was checked against the public Telangana RERA portal pages. Portal access behavior can vary and must be re-tested from the user's network.
