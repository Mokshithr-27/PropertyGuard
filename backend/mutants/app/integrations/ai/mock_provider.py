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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut: MutantDict = {}  # type: ignore

class MockDocumentAIProvider:
    @_mutmut_mutated(mutants_xǁMockDocumentAIProviderǁanalyze__mutmut)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_orig(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_1(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_2(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_3(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text and ""
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_4(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or "XXXX"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_5(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_6(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.lower()
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_7(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper or ("NOC" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_8(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "XXFIREXX" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_9(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "fire" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_10(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" not in upper and ("NOC" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_11(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper and "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_12(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("XXNOCXX" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_13(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("noc" in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_14(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" not in upper or "NO OBJECTION" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_15(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "XXNO OBJECTIONXX" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_16(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "no objection" in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_17(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" not in upper):
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_18(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_19(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "XXFIRE_NOCXX"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_20(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "fire_noc"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_21(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper and "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_22(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper and "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_23(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "XXSANCTIONED PLANXX" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_24(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "sanctioned plan" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_25(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" not in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_26(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "XXBUILDING PERMISSIONXX" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_27(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "building permission" in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_28(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" not in upper or "BUILDING APPROVAL" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_29(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "XXBUILDING APPROVALXX" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_30(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "building approval" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_31(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" not in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_32(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_33(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "XXSANCTIONED_PLANXX"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_34(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "sanctioned_plan"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_35(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper and "REAL ESTATE REGULATORY AUTHORITY" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_36(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "XXRERAXX" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_37(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "rera" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_38(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" not in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_39(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "XXREAL ESTATE REGULATORY AUTHORITYXX" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_40(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "real estate regulatory authority" in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_41(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "REAL ESTATE REGULATORY AUTHORITY" not in upper:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_42(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
            doc_type = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_43(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
            doc_type = "XXRERAXX"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_44(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []
        full_text = extracted_document.full_text or ""
        upper = full_text.upper()
        if "FIRE" in upper and ("NOC" in upper or "NO OBJECTION" in upper):
            doc_type = "FIRE_NOC"
        elif "SANCTIONED PLAN" in upper or "BUILDING PERMISSION" in upper or "BUILDING APPROVAL" in upper:
            doc_type = "SANCTIONED_PLAN"
        elif "RERA" in upper or "REAL ESTATE REGULATORY AUTHORITY" in upper:
            doc_type = "rera"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_45(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            doc_type = None

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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_46(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            doc_type = "XXUNKNOWNXX"

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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_47(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            doc_type = "unknown"

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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_48(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            text = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_49(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            text = page.text and ""
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_50(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            text = page.text or "XXXX"
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_51(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_52(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(None, text, flags=re.IGNORECASE)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_53(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(pattern, None, flags=re.IGNORECASE)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_54(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(pattern, text, flags=None)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_55(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(text, flags=re.IGNORECASE)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_56(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(pattern, flags=re.IGNORECASE)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_57(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    match = re.search(pattern, text, )
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_58(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_59(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", match.group(1)).strip(None)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_60(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(None, " ", match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_61(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", None, match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_62(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", None).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_63(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(" ", match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_64(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_65(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", ).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_66(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"XX\s+XX", " ", match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_67(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", "XX XX", match.group(1)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_68(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", match.group(None)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_69(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", match.group(2)).strip(" .,:;-")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_70(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        value = re.sub(r"\s+", " ", match.group(1)).strip("XX .,:;-XX")
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_71(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            start, end = None
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_72(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            evidence.append(None)
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_73(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                field_name=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_74(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                field_value=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_75(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                page_number=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_76(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                confidence=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_77(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_78(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                source=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_79(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_80(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_81(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_82(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_83(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_84(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_85(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                confidence=1.85,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_86(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(None, start-30):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_87(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, None):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_88(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(start-30):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_89(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, ):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_90(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(1, start-30):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_91(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start + 30):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_92(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-31):min(len(text), end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_93(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(None, end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_94(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(len(text), None)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_95(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(end+30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_96(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(len(text), )].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_97(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(len(text), end - 30)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_98(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                evidence_text=text[max(0, start-30):min(len(text), end+31)].strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_99(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                source="XXLABEL_PATTERNXX",
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_100(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                                source="label_pattern",
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_101(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                        return
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_102(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                evidence.append(None)

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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_103(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_name=None, field_value=text.strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_104(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_name="page_text", field_value=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_105(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    page_number=None, confidence=1.0,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_106(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    page_number=page.page_number, confidence=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_107(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    evidence_text=None, source=page.source,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_108(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    evidence_text=text.strip(), source=None,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_109(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_value=text.strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_110(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_name="page_text", page_number=page.page_number, confidence=1.0,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_111(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    confidence=1.0,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_112(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    page_number=page.page_number, evidence_text=text.strip(), source=page.source,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_113(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    source=page.source,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_114(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    evidence_text=text.strip(), ))

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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_115(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_name="XXpage_textXX", field_value=text.strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_116(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    field_name="PAGE_TEXT", field_value=text.strip(),
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_117(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                    page_number=page.page_number, confidence=2.0,
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
    def xǁMockDocumentAIProviderǁanalyze__mutmut_118(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            detected_document_type=None,
            summary=f"Local extraction inspected {extracted_document.page_count} page(s); only explicit labelled values are promoted as structured evidence.",
            structured_data={"page_count": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_119(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            summary=None,
            structured_data={"page_count": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_120(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            structured_data=None,
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_121(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=None,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_122(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            evidence=None,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_123(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            summary=f"Local extraction inspected {extracted_document.page_count} page(s); only explicit labelled values are promoted as structured evidence.",
            structured_data={"page_count": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_124(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            structured_data={"page_count": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_125(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_126(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_127(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_128(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            structured_data={"XXpage_countXX": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_129(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            structured_data={"PAGE_COUNT": extracted_document.page_count,
                            "has_text": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_130(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "XXhas_textXX": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_131(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "HAS_TEXT": extracted_document.has_text,
                            "text_length": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_132(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "XXtext_lengthXX": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_133(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "TEXT_LENGTH": len(full_text),
                            "extraction_mode": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_134(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "XXextraction_modeXX": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_135(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "EXTRACTION_MODE": "deterministic_label_patterns"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_136(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "extraction_mode": "XXdeterministic_label_patternsXX"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_137(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
                            "extraction_mode": "DETERMINISTIC_LABEL_PATTERNS"},
            overall_confidence=0.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_138(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=0.85 if (evidence) and False else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_139(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=0.85 if (evidence) or True else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_140(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=1.85 if evidence else 0.0,
            evidence=evidence,
        )
    def xǁMockDocumentAIProviderǁanalyze__mutmut_141(self, extracted_document: ExtractedDocument) -> AIAnalysisResult:
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
            overall_confidence=0.85 if evidence else 1.0,
            evidence=evidence,
        )

mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['_mutmut_orig'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_1'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_2'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_3'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_4'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_5'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_6'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_7'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_8'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_9'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_10'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_11'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_12'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_13'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_14'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_15'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_16'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_17'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_18'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_19'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_20'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_21'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_22'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_23'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_24'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_25'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_26'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_27'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_28'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_29'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_30'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_31'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_32'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_33'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_34'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_35'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_36'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_37'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_38'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_39'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_40'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_41'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_42'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_43'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_44'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_45'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_46'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_47'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_48'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_49'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_50'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_51'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_52'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_53'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_53 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_54'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_54 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_55'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_55 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_56'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_56 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_57'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_57 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_58'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_58 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_59'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_59 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_60'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_60 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_61'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_61 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_62'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_62 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_63'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_63 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_64'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_64 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_65'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_65 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_66'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_66 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_67'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_67 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_68'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_68 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_69'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_69 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_70'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_70 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_71'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_71 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_72'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_72 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_73'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_73 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_74'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_74 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_75'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_75 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_76'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_76 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_77'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_77 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_78'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_78 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_79'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_79 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_80'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_80 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_81'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_81 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_82'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_82 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_83'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_83 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_84'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_84 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_85'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_85 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_86'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_86 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_87'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_87 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_88'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_88 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_89'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_89 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_90'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_90 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_91'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_91 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_92'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_92 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_93'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_93 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_94'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_94 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_95'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_95 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_96'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_96 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_97'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_97 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_98'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_98 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_99'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_99 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_100'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_100 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_101'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_101 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_102'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_102 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_103'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_103 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_104'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_104 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_105'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_105 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_106'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_106 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_107'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_107 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_108'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_108 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_109'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_109 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_110'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_110 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_111'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_111 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_112'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_112 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_113'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_113 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_114'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_114 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_115'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_115 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_116'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_116 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_117'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_117 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_118'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_118 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_119'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_119 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_120'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_120 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_121'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_121 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_122'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_122 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_123'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_123 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_124'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_124 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_125'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_125 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_126'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_126 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_127'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_127 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_128'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_128 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_129'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_129 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_130'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_130 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_131'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_131 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_132'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_132 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_133'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_133 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_134'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_134 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_135'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_135 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_136'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_136 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_137'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_137 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_138'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_138 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_139'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_139 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_140'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_140 # type: ignore # mutmut generated
mutants_xǁMockDocumentAIProviderǁanalyze__mutmut['xǁMockDocumentAIProviderǁanalyze__mutmut_141'] = MockDocumentAIProvider.xǁMockDocumentAIProviderǁanalyze__mutmut_141 # type: ignore # mutmut generated
