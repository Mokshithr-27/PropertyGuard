"""
PropertyGuard Compliance Rule Versions Correction Utility
---------------------------------------------------------
Corrects legacy document type keys in seeded compliance rule versions
(e.g., mapping PG_APPROVED_BUILDING_PLAN to SANCTIONED_PLAN and FIRE_SAFETY_DOCUMENT to FIRE_NOC).
"""

from datetime import datetime, timezone

from app.core.database import SessionLocal
from app.models.compliance import ComplianceRule, RuleVersion


CORRECTIONS = {
    "PG_APPROVED_BUILDING_PLAN": "SANCTIONED_PLAN",
    "PG_FIRE_SAFETY_DOCUMENT": "FIRE_NOC",
}


def main():
    db = SessionLocal()

    try:
        created = 0

        for rule_code, document_type in CORRECTIONS.items():
            rule = (
                db.query(ComplianceRule)
                .filter(ComplianceRule.rule_code == rule_code)
                .first()
            )

            if rule is None:
                raise ValueError(f"Rule not found: {rule_code}")

            active_version = (
                db.query(RuleVersion)
                .filter(
                    RuleVersion.rule_id == rule.id,
                    RuleVersion.is_active.is_(True),
                )
                .order_by(RuleVersion.version_number.desc())
                .first()
            )

            if active_version is None:
                raise ValueError(
                    f"No active version found for {rule_code}"
                )

            if (
                active_version.evaluation_logic
                and active_version.evaluation_logic.get("document_type")
                == document_type
            ):
                print(f"{rule_code}: already corrected")
                continue

            active_version.is_active = False

            new_version = RuleVersion(
                rule_id=rule.id,
                version_number=active_version.version_number + 1,
                rule_text=active_version.rule_text,
                required_evidence={
                    "document_type": document_type
                },
                evaluation_logic={
                    "type": "DOCUMENT_EXISTS",
                    "document_type": document_type,
                },
                severity=active_version.severity,
                risk_floor_implication=active_version.risk_floor_implication,
                effective_from=datetime.now(timezone.utc),
                is_active=True,
            )

            db.add(new_version)
            created += 1

            print(
                f"{rule_code}: created version "
                f"{new_version.version_number} → {document_type}"
            )

        db.commit()
        print(f"Corrected versions created: {created}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()