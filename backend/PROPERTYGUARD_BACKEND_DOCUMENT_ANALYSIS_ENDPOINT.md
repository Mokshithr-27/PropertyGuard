# PropertyGuard Backend — Document Analysis Retrieval

Added a builder-authorized endpoint:

`GET /api/v1/documents/{document_id}/analysis`

It returns the latest completed `DocumentAnalysis` and its `DocumentEvidence` records for a document owned by the authenticated Builder.

This endpoint does not make a compliance decision. It exposes the evidence produced by the existing text/OCR/AI document-processing pipeline so the frontend can display and apply unique extracted project metadata.

No database migration is required because this change reads the existing document analysis and evidence tables.
