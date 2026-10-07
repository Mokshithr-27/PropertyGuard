from types import SimpleNamespace

import pytest

from app.services import document_processing_service


class FakeDB:
    pass


def make_version(status="UPLOADED"):
    return SimpleNamespace(
        id="test-version-id",
        deleted_at=None,
        processing_status=status,
    )


def make_job(status="QUEUED"):
    return SimpleNamespace(
        id="test-job-id",
        document_version_id="test-version-id",
        status=status,
        attempt_count=0,
        queued_at=None,
        started_at=None,
        completed_at=None,
        error_message=None,
    )


def test_queue_document_processing_success(monkeypatch):
    db = FakeDB()
    version = make_version()

    created_jobs = []

    def fake_get_active_job(db, document_version_id):
        return None

    def fake_create_job(db, job):
        created_jobs.append(job)
        return job

    def fake_update_version(db, version):
        return version

    monkeypatch.setattr(
        document_processing_service,
        "get_active_processing_job",
        fake_get_active_job,
    )
    monkeypatch.setattr(
        document_processing_service,
        "create_processing_job",
        fake_create_job,
    )
    monkeypatch.setattr(
        document_processing_service,
        "update_document_version",
        fake_update_version,
    )

    result = document_processing_service.queue_document_processing(
        db=db,
        version=version,
    )

    assert result.status == "QUEUED"
    assert version.processing_status == "QUEUED"
    assert len(created_jobs) == 1


def test_queue_document_processing_rejects_duplicate(monkeypatch):
    db = FakeDB()
    version = make_version()

    existing_job = make_job("QUEUED")

    def fake_get_active_job(db, document_version_id):
        return existing_job

    monkeypatch.setattr(
        document_processing_service,
        "get_active_processing_job",
        fake_get_active_job,
    )

    with pytest.raises(
        ValueError,
        match="active processing job already exists",
    ):
        document_processing_service.queue_document_processing(
            db=db,
            version=version,
        )


def test_start_document_processing_success(monkeypatch):
    db = FakeDB()
    job = make_job("QUEUED")

    def fake_update_job(db, job):
        return job

    monkeypatch.setattr(
        document_processing_service,
        "update_processing_job",
        fake_update_job,
    )

    result = document_processing_service.start_document_processing(
        db=db,
        job=job,
    )

    assert result.status == "PROCESSING"
    assert result.attempt_count == 1
    assert result.started_at is not None


def test_complete_document_processing_success(monkeypatch):
    db = FakeDB()
    job = make_job("PROCESSING")
    version = make_version("PROCESSING")

    def fake_update_job(db, job):
        return job

    def fake_update_version(db, version):
        return version

    monkeypatch.setattr(
        document_processing_service,
        "update_processing_job",
        fake_update_job,
    )
    monkeypatch.setattr(
        document_processing_service,
        "update_document_version",
        fake_update_version,
    )

    result = document_processing_service.complete_document_processing(
        db=db,
        job=job,
        version=version,
    )

    assert result.status == "COMPLETED"
    assert result.completed_at is not None
    assert version.processing_status == "COMPLETED"


def test_fail_document_processing_success(monkeypatch):
    db = FakeDB()
    job = make_job("PROCESSING")
    version = make_version("PROCESSING")

    def fake_update_job(db, job):
        return job

    def fake_update_version(db, version):
        return version

    monkeypatch.setattr(
        document_processing_service,
        "update_processing_job",
        fake_update_job,
    )
    monkeypatch.setattr(
        document_processing_service,
        "update_document_version",
        fake_update_version,
    )

    result = document_processing_service.fail_document_processing(
        db=db,
        job=job,
        version=version,
        error_message="OCR processing failed",
    )

    assert result.status == "FAILED"
    assert result.error_message == "OCR processing failed"
    assert result.completed_at is not None
    assert version.processing_status == "FAILED"


def test_start_document_processing_rejects_invalid_state(
    monkeypatch,
):
    db = FakeDB()
    job = make_job("COMPLETED")

    with pytest.raises(
        ValueError,
        match="Only queued jobs can be started",
    ):
        document_processing_service.start_document_processing(
            db=db,
            job=job,
        )