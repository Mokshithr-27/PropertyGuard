/**
 * PropertyGuard API Data Contracts & Response Types
 * Strongly typed TypeScript interfaces mirroring backend models: users, builder profiles,
 * projects, required document catalog, versions, analyses, evaluations, and findings.
 */

export type Role = 'BUILDER' | 'BUYER' | 'ADMIN' | 'SUPER_ADMIN';

export interface ApiUser {
  id: string;
  email: string;
  full_name: string;
  phone: string | null;
  is_active: boolean;
  is_email_verified: boolean;
  roles: Role[] | string[];
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface BuilderProfile {
  id: string;
  user_id: string;
  company_name: string;
  registration_number: string | null;
  address: string | null;
  verification_status: string;
  created_at: string;
  updated_at: string;
}

export interface Project {
  id: string;
  builder_id: string;
  name: string;
  description: string | null;
  project_type: string;
  address: string | null;
  status: string;
  created_at: string;
  updated_at: string;
  latest_version_number?: number | null;
  documents_count?: number;
  compliance_score?: number | null;
}

export interface ProjectUpdate {
  name: string;
  description?: string | null;
  project_type: string;
  address?: string | null;
}

export interface ProjectCreate {
  name: string;
  description?: string | null;
  project_type: string;
  address?: string | null;
}

export interface RequiredDocument {
  document_type: string;
  name: string;
  description: string;
  is_mandatory: boolean;
  authority: string;
  category: string;
  accepted_formats: string[];
}

export interface DocumentVersion {
  id: string;
  document_id: string;
  version_number: number;
  file_name: string;
  mime_type: string;
  file_size: number;
  file_hash: string;
  storage_key: string;
  uploaded_by: string;
  processing_status: string;
  created_at: string;
  deleted_at: string | null;
}

export interface DocumentItem {
  id: string;
  project_id: string;
  document_type: string;
  title: string;
  description: string | null;
  visibility: string;
  authority_level: number | null;
  expiry_date: string | null;
  status: string;
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
}

export interface DocumentDetail extends DocumentItem {
  versions: DocumentVersion[];
}

export interface DocumentValidation {
  is_valid: boolean;
  file_name: string;
  mime_type: string;
  file_size: number;
  file_size_formatted: string;
  sha256: string;
  detected_format: string;
  error: string | null;
  details: Record<string, string | number | boolean>;
}

export interface ProcessingJob {
  id: string;
  document_version_id: string;
  status: string;
  attempt_count: number;
  queued_at: string;
  started_at: string | null;
  completed_at: string | null;
  error_message: string | null;
  created_at: string;
}

export interface EvaluationRun {
  id: string;
  project_id: string;
  status: string;
  started_at: string;
  completed_at: string | null;
  error_message: string | null;
  created_at: string;
}

export interface ComplianceResult {
  id: string;
  project_id: string;
  evaluation_run_id: string | null;
  rule_version_id: string;
  outcome: string;
  explanation: string | null;
  dependency_affected: boolean;
  evaluated_at: string;
  created_at: string;
}

export interface EvaluationRunResults {
  evaluation_run: EvaluationRun;
  results: ComplianceResult[];
}

export interface Finding {
  id: string;
  compliance_result_id: string;
  severity: string;
  title: string;
  description: string;
  status: string;
  resolution_note: string | null;
  resolved_at: string | null;
  created_at: string;
  updated_at: string;
}

export interface FindingUpdate {
  status?: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED';
  resolution_note?: string | null;
}
