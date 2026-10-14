# PropertyGuard rules-verification implementation notes

## Changes

1. Compliance rule versions are now evaluated in dependency-first order, regardless of rule-code ordering. This prevents a dependent rule from being marked `NEEDS_REVIEW` merely because its dependency happened to appear later in the active-rule list.
2. A cycle in active rule dependencies now fails the evaluation explicitly instead of producing order-dependent outcomes.
3. The OCR worker logs only page count and extracted-text length; it no longer prints raw OCR text into worker logs.
4. Added focused unit tests for dependency ordering and dependency-cycle rejection.

## Validation

- Python compilation of `app` and `tests`: passed.
- Focused pytest run could not complete in this archive-validation environment because the `psycopg` runtime dependency is not installed. Run tests from the project's `.venv` on the development machine.

## Important scope note

This connects the existing deterministic evaluator more reliably. It does not populate a complete, legally reviewed Telangana compliance rule catalog, and it does not verify certificate authenticity against official portals. Those remain separate work items.

## Run locally

```powershell
cd C:\PROJECT\PropertyGuard\backend
.\.venv\Scripts\Activate.ps1
python -m pytest tests\services\test_compliance_service.py tests\rules\test_evaluator.py tests\workers\test_document_tasks.py -q
```
