"""
PropertyGuard SQLAlchemy ORM Models Package
--------------------------------------------
Exports all database entities including authentication, builder profiles, project
hierarchies, documents, processing jobs, compliance rules, evaluations, and AI evidence.
"""

from app.models.user import User
from app.models.role import Role, UserRole
from app.models.builder import BuilderProfile, BuilderVerification
from app.models.project import Project, ProjectVersion, Building, Unit
from app.models.document import Document, DocumentVersion
from app.models.evaluation import EvaluationRun

from app.models.document_processing_job import DocumentProcessingJob

from app.models.compliance import (
    ComplianceRule,
    RuleVersion,
    RuleApplicability,
    RuleDependency,
    ComplianceResult,
    Finding,
    Discrepancy,
)

from app.models.document_analysis import (
    DocumentAnalysis,
    DocumentEvidence,
)
from app.models.rera_verification import ReraVerification


__all__ = [
    "User",
    "Role",
    "UserRole",
    "BuilderProfile",
    "BuilderVerification",
    "Project",
    "ProjectVersion",
    "Building",
    "Unit",
    "Document",
    "DocumentVersion",
    "ComplianceRule",
    "RuleVersion",
    "RuleApplicability",
    "RuleDependency",
    "ComplianceResult",
    "Finding",
    "Discrepancy",
    "DocumentProcessingJob",
    "DocumentAnalysis",
    "DocumentEvidence",
    "ReraVerification",
]