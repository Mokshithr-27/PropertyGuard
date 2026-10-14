"""
PropertyGuard Document Tasks Worker Test Suite
----------------------------------------------
Validates Celery document processing task pipeline, testing mock extraction paths,
AI analysis persistence, OCR worker delegation, and error rollback handling.
"""

from types import SimpleNamespace

from uuid import UUID

from app.workers import document_tasks


class FakeDB:
    def __init__(self):
        self.commit_count = 0
        self.refresh_count = 0
        self.rollback_count = 0
        self.close_count = 0

    def commit(self):
        self.commit_count += 1

    def refresh(self, obj):
        self.refresh_count += 1

    def rollback(self):
        self.rollback_count += 1

    def close(self):
        self.close_count += 1


def make_version():
    return SimpleNamespace(
        id=UUID("11111111-1111-1111-1111-111111111111"),
        storage_key="test/storage/document.pdf",
        processing_status="QUEUED",
    )


def make_job():
    return SimpleNamespace(
        id=UUID("22222222-2222-2222-2222-222222222222"),
        status="QUEUED",
    )


def make_extracted_document():
    page = SimpleNamespace(
        page_number=1,
        text="RERA Registration Number: RERA123456",
    )

    return SimpleNamespace(
        page_count=1,
        pages=[page],
        full_text="RERA Registration Number: RERA123456",
        has_text=True,
    )


def test_process_document_task_success(monkeypatch):
    db = FakeDB()
    version = make_version()
    job = make_job()
    extracted = make_extracted_document()


    monkeypatch.setattr(
        document_tasks,
        "SessionLocal",
        lambda: db,
    )

    monkeypatch.setattr(
        document_tasks,
        "get_document_version",
        lambda db, version_id: version,
    )

    monkeypatch.setattr(
        document_tasks,
        "get_processing_job",
        lambda db, job_id: job,
    )

    monkeypatch.setattr(
        document_tasks,
        "start_document_processing",
        lambda db, job: setattr(job, "status", "PROCESSING"),
    )

    monkeypatch.setattr(
        document_tasks,
        "download_bytes",
        lambda storage_key: b"fake-pdf-data",
    )

    monkeypatch.setattr(
        document_tasks,
        "extract_pdf_text",
        lambda data: extracted,
    )

    analysis_calls = []
    provider_calls = []


    class FakeProvider:
        def analyze(self, extracted_document):
            provider_calls.append(extracted_document)

            return SimpleNamespace(
                detected_document_type="RERA",
                summary="Mock RERA analysis",
                structured_data={
                    "registration_number": "RERA123456",
                },
                overall_confidence=0.95,
                evidence=[],
            )


    monkeypatch.setattr(
        document_tasks,
        "get_ai_provider",
        lambda: FakeProvider(),
    )


    def fake_persist_document_analysis(
        db,
        document_version_id,
        result,
    ):
        analysis_calls.append(
            {
                "document_version_id": document_version_id,
                "result": result,
            }
        )


    monkeypatch.setattr(
        document_tasks,
        "persist_document_analysis",
        fake_persist_document_analysis,
    )


    monkeypatch.setattr(
        document_tasks,
        "complete_document_processing",
        lambda db, job, version: (
            setattr(job, "status", "COMPLETED"),
            setattr(version, "processing_status", "COMPLETED"),
        ),
    )

    result = document_tasks.process_document_task.run(
        "11111111-1111-1111-1111-111111111111",
        "22222222-2222-2222-2222-222222222222",
    )

    assert result["version_id"] == "11111111-1111-1111-1111-111111111111"
    assert result["job_id"] == "22222222-2222-2222-2222-222222222222"
    assert result["page_count"] == 1
    assert result["has_text"] is True
    assert result["text_length"] == len(extracted.full_text)
    assert result["status"] == "COMPLETED"

    assert len(provider_calls) == 1
    assert provider_calls[0] is extracted

    assert len(analysis_calls) == 1
    assert analysis_calls[0]["document_version_id"] == UUID(
        "11111111-1111-1111-1111-111111111111"
    )

    assert analysis_calls[0]["result"].detected_document_type == "RERA"
    assert analysis_calls[0]["result"].summary == "Mock RERA analysis"
    assert analysis_calls[0]["result"].overall_confidence == 0.95

    

    assert job.status == "COMPLETED"
    assert version.processing_status == "COMPLETED"

    assert db.commit_count == 2
    assert db.close_count == 1


def test_process_document_task_fails_when_analysis_fails(monkeypatch):
    db = FakeDB()
    version = make_version()
    job = make_job()
    extracted = make_extracted_document()

    monkeypatch.setattr(
        document_tasks,
        "SessionLocal",
        lambda: db,
    )

    monkeypatch.setattr(
        document_tasks,
        "get_document_version",
        lambda db, version_id: version,
    )

    monkeypatch.setattr(
        document_tasks,
        "get_processing_job",
        lambda db, job_id: job,
    )

    monkeypatch.setattr(
        document_tasks,
        "start_document_processing",
        lambda db, job: setattr(job, "status", "PROCESSING"),
    )

    monkeypatch.setattr(
        document_tasks,
        "download_bytes",
        lambda storage_key: b"fake-pdf-data",
    )

    monkeypatch.setattr(
        document_tasks,
        "extract_pdf_text",
        lambda data: extracted,
    )

    class FailingProvider:
        def analyze(self, extracted_document):
            raise ValueError("AI analysis failed")


    monkeypatch.setattr(
        document_tasks,
        "get_ai_provider",
        lambda: FailingProvider(),
    )

    def fake_fail_document_processing(
        db,
        job,
        version,
        error_message,
    ):
        job.status = "FAILED"
        version.processing_status = "FAILED"

    monkeypatch.setattr(
        document_tasks,
        "fail_document_processing",
        fake_fail_document_processing,
    )

    try:
        document_tasks.process_document_task.run(
            "11111111-1111-1111-1111-111111111111",
            "22222222-2222-2222-2222-222222222222",
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "AI analysis failed"

    assert job.status == "FAILED"
    assert version.processing_status == "FAILED"
    assert db.rollback_count == 1
    assert db.close_count == 1