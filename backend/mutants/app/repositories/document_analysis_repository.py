"""
PropertyGuard Document Analysis Repository
------------------------------------------
Handles database retrieval of the latest completed DocumentAnalysis records
and associated DocumentEvidence collections for specific document versions.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_analysis import DocumentAnalysis, DocumentEvidence


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_latest_document_analysis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_latest_document_analysis__mutmut)
def get_latest_document_analysis(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_orig(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_1(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        None
    )


def x_get_latest_document_analysis__mutmut_2(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(None)
    )


def x_get_latest_document_analysis__mutmut_3(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            None,
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_4(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            None,
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_5(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_6(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_7(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            None,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_8(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            None,
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_9(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_10(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_11(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(None)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_12(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id != document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_13(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status != "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_14(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "XXCOMPLETEDXX",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_15(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "completed",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def x_get_latest_document_analysis__mutmut_16(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(2)
    )

mutants_x_get_latest_document_analysis__mutmut['_mutmut_orig'] = x_get_latest_document_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_1'] = x_get_latest_document_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_2'] = x_get_latest_document_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_3'] = x_get_latest_document_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_4'] = x_get_latest_document_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_5'] = x_get_latest_document_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_6'] = x_get_latest_document_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_7'] = x_get_latest_document_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_8'] = x_get_latest_document_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_9'] = x_get_latest_document_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_10'] = x_get_latest_document_analysis__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_11'] = x_get_latest_document_analysis__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_12'] = x_get_latest_document_analysis__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_13'] = x_get_latest_document_analysis__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_14'] = x_get_latest_document_analysis__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_15'] = x_get_latest_document_analysis__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_latest_document_analysis__mutmut['x_get_latest_document_analysis__mutmut_16'] = x_get_latest_document_analysis__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_document_analysis_evidence__mutmut)
def get_document_analysis_evidence(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_orig(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_1(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        None
    )


def x_get_document_analysis_evidence__mutmut_2(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_3(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                None,
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_4(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                None,
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_5(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_6(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_7(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                None,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_8(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(None)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )


def x_get_document_analysis_evidence__mutmut_9(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id != analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )

mutants_x_get_document_analysis_evidence__mutmut['_mutmut_orig'] = x_get_document_analysis_evidence__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_1'] = x_get_document_analysis_evidence__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_2'] = x_get_document_analysis_evidence__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_3'] = x_get_document_analysis_evidence__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_4'] = x_get_document_analysis_evidence__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_5'] = x_get_document_analysis_evidence__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_6'] = x_get_document_analysis_evidence__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_7'] = x_get_document_analysis_evidence__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_8'] = x_get_document_analysis_evidence__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_document_analysis_evidence__mutmut['x_get_document_analysis_evidence__mutmut_9'] = x_get_document_analysis_evidence__mutmut_9 # type: ignore # mutmut generated