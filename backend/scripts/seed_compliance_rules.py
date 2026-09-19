from datetime import datetime, timezone

from app.core.database import SessionLocal
from app.models.compliance import (
    ComplianceRule,
    RuleApplicability,
    RuleVersion,
)
from app.repositories.compliance_repository import (
    get_rule_by_code,
)


RULES = [
    {
        "rule_code": "PG_RERA_REGISTRATION",
        "name": "RERA Registration Evidence",
        "description": (
            "Verify whether the project has evidence of RERA registration."
        ),
        "category": "REGULATORY",
        "authority": "Telangana RERA",
        "rule_text": (
            "RERA registration evidence should be available for the project."
        ),
        "severity": "HIGH",
        "evaluation_logic": {
            "type": "DOCUMENT_EXISTS",
            "document_type": "RERA",
        },
    },
    {
        "rule_code": "PG_APPROVED_BUILDING_PLAN",
        "name": "Approved Building Plan",
        "description": (
            "Verify whether an approved building plan document exists."
        ),
        "category": "DOCUMENTATION",
        "authority": "Competent Planning Authority",
        "rule_text": (
            "An approved building plan document should be available."
        ),
        "severity": "HIGH",
        "evaluation_logic": {
            "type": "DOCUMENT_EXISTS",
            "document_type": "APPROVED_BUILDING_PLAN",
        },
    },
    {
        "rule_code": "PG_FIRE_SAFETY_DOCUMENT",
        "name": "Fire Safety Documentation",
        "description": (
            "Verify whether fire safety documentation exists."
        ),
        "category": "SAFETY",
        "authority": "Relevant Fire Safety Authority",
        "rule_text": (
            "Fire safety documentation should be available."
        ),
        "severity": "HIGH",
        "evaluation_logic": {
            "type": "DOCUMENT_EXISTS",
            "document_type": "FIRE_SAFETY",
        },
    },
]


def seed_rules():
    db = SessionLocal()

    try:
        created_rules = 0
        created_versions = 0
        created_applicability = 0

        for rule_data in RULES:
            rule = get_rule_by_code(db, rule_data["rule_code"])

            if rule is None:
                rule = ComplianceRule(
                    rule_code=rule_data["rule_code"],
                    name=rule_data["name"],
                    description=rule_data["description"],
                    category=rule_data["category"],
                    authority=rule_data["authority"],
                    is_active=True,
                )

                db.add(rule)
                db.flush()
                created_rules += 1

            existing_version = next(
                (
                    version
                    for version in rule.versions
                    if version.version_number == 1
                ),
                None,
            )

            if existing_version is None:
                version = RuleVersion(
                    rule_id=rule.id,
                    version_number=1,
                    rule_text=rule_data["rule_text"],
                    required_evidence={
                        "document_type": rule_data["evaluation_logic"][
                            "document_type"
                        ]
                    },
                    evaluation_logic=rule_data["evaluation_logic"],
                    severity=rule_data["severity"],
                    risk_floor_implication=True,
                    effective_from=datetime.now(timezone.utc),
                    is_active=True,
                )

                db.add(version)
                db.flush()
                created_versions += 1

                applicability = RuleApplicability(
                    rule_version_id=version.id,
                    property_type="APARTMENT",
                    conditions=None,
                    is_active=True,
                )

                db.add(applicability)
                created_applicability += 1

        db.commit()

        print("Compliance rule seeding completed.")
        print(f"Rules created: {created_rules}")
        print(f"Rule versions created: {created_versions}")
        print(
            f"Applicability records created: "
            f"{created_applicability}"
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_rules()