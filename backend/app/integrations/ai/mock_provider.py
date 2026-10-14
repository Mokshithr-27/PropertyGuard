"""Deterministic local document analyzer for development and tests.

This provider extracts only explicit label/value pairs and retains verbatim
supporting text. It never determines legal compliance or official authenticity.
"""
import re
from app.integrations.ai.base import AIAnalysisResult, EvidenceItem
from app.services.document_text_extraction_service import ExtractedDocument

FIELD_PATTERNS = {
    "registration_number": [r"(?:Telangana\s*RERA|TGRERA|RERA)\s*(?:Registration\s*(?:No|Number))?\s*[:#-]?\s*((?:P|A)\d{2,}[A-Z0-9/-]*)"],
    "project_name": [r"(?:Project\s*Name|Name\s*of\s*Project)\s*[:：-]\s*([^\n\r]{2,160})"],
    "promoter_name": [r"(?:Promoter\s*Name|Builder\s*Name|Developer\s*Name)\s*[:：-]\s*([^\n\r]{2,160})"],
    "approval_number": [r"(?:Approval\s*(?:No|Number)|Permit\s*(?:No|Number)|Proceedings\s*No)\s*[:：-]\s*([^\n\r]{2,100})"],
    "certificate_number": [r"(?:Certificate\s*(?:No|Number)|NOC\s*(?:No|Number))\s*[:：-]\s*([^\n\r]{2,100})"],
    "number_of_floors": [r"(?:Number\s*of\s*Floors|No\.?\s*of\s*Floors|Floors)\s*[:：-]\s*(\d{1,3})\b"],
    "sanctioned_area": [r"(?:Sanctioned\s*Area|Approved\s*Area)\s*[:：-]\s*([\d,.]+\s*(?:sq\.?\s*m(?:eters?)?|sq\.?\s*ft|square feet|square meters)?)"],
    "validity_date": [r"(?:Valid\s*(?:Until|Upto|Till)|Validity\s*Date|Valid\s*Through)\s*[:：-]\s*([^\n\r]{3,60})"],
    "registration_date": [r"(?:Registration\s*Date|Date\s*of\s*Registration)\s*[:：-]\s*([^\n\r]{3,60})"],
}

class MockDocumentAIProvider:
    def analyze(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
            doc_type = "RERA"
        else:
            doc_type = "UNKNOWN"

        for page in extracted_document.pages:
            text = page.text or ""
            for field_name, patterns in FIELD_PATTERNS.items():
                for pattern in patterns:
                    match = re.search(pattern, text, flags=re.IGNORECASE)
                    if match:
                        value = re.sub(r"\s+", " ", match.group(1)).strip(" .,:;-")
                        if value:
                            start, end = match.span()
                            evidence.append(EvidenceItem(
                                field_name=field_name,
                                field_value=value,
                                page_number=page.page_number,
                                confidence=0.85,
                                evidence_text=text[max(0, start-30):min(len(text), end+30)].strip(),
                                source="LABEL_PATTERN",
                            ))
                        break
            if text.strip():
                evidence.append(EvidenceItem(
                    field_name="page_text", field_value=text.strip(),
                    page_number=page.page_number, confidence=1.0,
                    evidence_text=text.strip(), source=page.source,
                ))

        return AIAnalysisResult(
            detected_document_type=doc_type,
            summary=f"Local extraction inspected {extracted_document.page_count} page(s); only explicit labelled values are promoted as structured evidence.",
            structured_data={"page_count": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
