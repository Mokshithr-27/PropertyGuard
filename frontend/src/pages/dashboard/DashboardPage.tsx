/**
 * PropertyGuard Primary Dashboard Component
 * Manages project workspaces, document-first upload and validation flows, asynchronous
 * OCR/AI processing polling, semantic evidence review, deterministic compliance evaluation,
 * and project modification/soft deletion controls.
 */

import { useEffect, useMemo, useState } from 'react';
import {
  AlertCircle,
  Download,
  ArrowRight,
  CheckCircle2,
  ClipboardList,
  FileCheck2,
  FileText,
  FolderPlus,
  Globe,
  Play,
  Loader2,
  LogOut,
  Pencil,
  RefreshCw,
  ShieldCheck,
  Trash2,
  UploadCloud,
  UserRound,
  X,
} from 'lucide-react';
import { apiClient } from '../../api/client';
import { useAuth } from '../../context/AuthContext';
import { Button } from '../../components/common/Button';
import { Badge } from '../../components/common/Badge';
import { Input } from '../../components/common/Input';
import styles from './DashboardPage.module.css';

interface ProjectItem {
  id: string;
  builder_id: string;
  name: string;
  description: string | null;
  project_type: string;
  address: string | null;
  status: string;
  latest_version_number: number | null;
  documents_count: number;
  compliance_score: number | null;
  created_at: string;
  updated_at: string;
}

interface RequiredDocument {
  document_type: string;
  name: string;
  description: string;
  is_mandatory: boolean;
  authority: string;
  category: string;
  accepted_formats: string[];
}

interface DocumentVersion {
  id: string;
  document_id: string;
  version_number: number;
  file_name: string;
  mime_type: string;
  file_size: number;
  processing_status: string;
  created_at: string;
  deleted_at: string | null;
}

interface DocumentDetail {
  id: string;
  project_id: string;
  document_type: string;
  title: string;
  status: string;
  versions: DocumentVersion[];
}

interface DocumentSummary {
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

interface DocumentAnalysis {
  id: string;
  document_version_id: string;
  status: string;
  provider: string | null;
  model_name: string | null;
  detected_document_type: string | null;
  summary: string | null;
  structured_data: Record<string, unknown> | null;
  overall_confidence: number | null;
  evidence: EvidenceItem[];
}

interface EvidenceItem {
  id: string;
  field_name: string;
  field_value: string | null;
  page_number: number | null;
  confidence: number | null;
  source: string | null;
  evidence_text: string | null;
}

interface ProcessingItem {
  requirement: RequiredDocument;
  fileName: string;
  status: 'QUEUED' | 'PROCESSING' | 'COMPLETED' | 'FAILED';
  documentId?: string;
  analysis?: DocumentAnalysis;
  error?: string;
}

type WizardStep = 'details' | 'documents' | 'processing' | 'review' | 'complete';

const PROJECT_TYPES = [
  { value: 'APARTMENT', label: 'Residential Apartment' },
  { value: 'VILLA', label: 'Residential Villa / Gated Community' },
  { value: 'INDIVIDUAL_HOUSE', label: 'Individual House' },
];

function roleLabel(role?: string) {
  if (role === 'admin') return 'Admin';
  if (role === 'builder') return 'Builder';
  return 'Buyer';
}

function statusVariant(status: string): 'success' | 'warning' | 'danger' | 'info' | 'default' {
  if (['ACTIVE', 'COMPLETED', 'VERIFIED', 'APPROVED'].includes(status)) return 'success';
  if (['PENDING', 'QUEUED', 'PROCESSING', 'PENDING_APPROVAL'].includes(status)) return 'warning';
  if (['FAILED', 'REJECTED', 'SUSPENDED'].includes(status)) return 'danger';
  return 'info';
}

export function DashboardPage() {
  const { user, logout } = useAuth();
  const [projects, setProjects] = useState<ProjectItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [pageError, setPageError] = useState('');
  const [selectedProject, setSelectedProject] = useState<ProjectItem | null>(null);
  const [showProjectForm, setShowProjectForm] = useState(false);
  const [showCreateWizard, setShowCreateWizard] = useState(false);
  const [editingProject, setEditingProject] = useState<ProjectItem | null>(null);

  const isBuilder = user?.role === 'builder';
  const isAdmin = user?.role === 'admin';
  const canManage = isBuilder || isAdmin;

  const loadProjects = async () => {
    setLoading(true);
    setPageError('');
    try {
      const response = await apiClient.get<ProjectItem[]>('/api/v1/projects');
      setProjects(response.data);
    } catch (error: any) {
      setPageError(error.response?.data?.detail || 'Unable to load projects.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    void loadProjects();
  }, []);

  const activeProjects = useMemo(
    () => projects.filter((project) => project.status !== 'INACTIVE'),
    [projects],
  );

  const handleDelete = async (project: ProjectItem) => {
    if (!window.confirm(`Soft-delete "${project.name}"? Project history will be preserved.`)) return;
    try {
      await apiClient.delete(`/api/v1/projects/${project.id}`);
      setSelectedProject(null);
      await loadProjects();
    } catch (error: any) {
      window.alert(error.response?.data?.detail || 'Unable to delete project.');
    }
  };

  const handleSaveProject = async (payload: ProjectFormValues) => {
    try {
      if (editingProject) {
        await apiClient.patch(`/api/v1/projects/${editingProject.id}`, payload);
      } else {
        await apiClient.post('/api/v1/projects', payload);
      }
      setShowProjectForm(false);
      setEditingProject(null);
      await loadProjects();
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Unable to save project.');
    }
  };

  return (
    <div className={styles.page}>
      <header className={styles.topbar}>
        <div className={styles.brandBlock}>
          <div className={styles.brandIcon}><ShieldCheck size={22} /></div>
          <div>
            <div className={styles.brand}>PropertyGuard</div>
            <div className={styles.brandSub}>Property compliance workspace</div>
          </div>
        </div>
        <div className={styles.userBlock}>
          <div className={styles.userText}>
            <strong>{user?.full_name || user?.email}</strong>
            <span>{roleLabel(user?.role)}</span>
          </div>
          <Button variant="ghost" size="sm" icon={<LogOut size={15} />} onClick={logout}>Sign out</Button>
        </div>
      </header>

      <main className={styles.container}>
        <section className={styles.hero}>
          <div>
            <span className={styles.eyebrow}>Property workspace</span>
            <h1>{isBuilder ? 'Create and verify your property project' : 'Review property projects'}</h1>
            <p>
              {isBuilder
                ? 'Create a project, upload the required statutory documents, and let the processing pipeline extract document evidence before you continue.'
                : 'Review project information and administrative actions using the live backend data.'}
            </p>
          </div>
          {isBuilder && (
            <Button size="lg" icon={<FolderPlus size={18} />} onClick={() => setShowCreateWizard(true)}>
              New project
            </Button>
          )}
        </section>

        {pageError && (
          <div className={styles.errorBanner}><AlertCircle size={18} /> {pageError}</div>
        )}

        <section className={styles.summaryGrid}>
          <SummaryCard icon={<ClipboardList size={20} />} label="Active projects" value={String(activeProjects.length)} />
          <SummaryCard icon={<FileText size={20} />} label="Documents" value={String(projects.reduce((sum, project) => sum + project.documents_count, 0))} />
          <SummaryCard icon={<ShieldCheck size={20} />} label="Evaluations" value="On demand" />
          <SummaryCard icon={<UserRound size={20} />} label="Role" value={roleLabel(user?.role)} />
        </section>

        <section className={styles.section}>
          <div className={styles.sectionHeader}>
            <div>
              <h2>Projects</h2>
              <p>Live projects returned by the PropertyGuard API.</p>
            </div>
            <Button variant="outline" size="sm" icon={<RefreshCw size={15} />} onClick={() => void loadProjects()} isLoading={loading}>
              Refresh
            </Button>
          </div>

          {loading ? (
            <div className={styles.emptyState}><Loader2 className={styles.spin} size={22} /> Loading projects...</div>
          ) : activeProjects.length === 0 ? (
            <div className={styles.emptyState}>
              <FolderPlus size={28} />
              <strong>No projects yet</strong>
              <span>{isBuilder ? 'Start by creating your first project and uploading its required documents.' : 'No active projects are available to this account.'}</span>
            </div>
          ) : (
            <div className={styles.projectGrid}>
              {activeProjects.map((project) => (
                <ProjectCard
                  key={project.id}
                  project={project}
                  canManage={canManage}
                  onOpen={() => setSelectedProject(project)}
                  onEdit={() => { setEditingProject(project); setShowProjectForm(true); }}
                  onDelete={() => void handleDelete(project)}
                />
              ))}
            </div>
          )}
        </section>
      </main>

      {selectedProject && (
        <ProjectDetailsModal
          project={selectedProject}
          canManage={canManage}
          onClose={() => setSelectedProject(null)}
          onEdit={() => { setEditingProject(selectedProject); setSelectedProject(null); setShowProjectForm(true); }}
          onDelete={() => void handleDelete(selectedProject)}
        />
      )}

      {showProjectForm && (
        <ProjectFormModal
          project={editingProject}
          onClose={() => { setShowProjectForm(false); setEditingProject(null); }}
          onSave={handleSaveProject}
        />
      )}

      {showCreateWizard && (
        <CreateProjectWizard
          onClose={() => setShowCreateWizard(false)}
          onCreated={async () => { await loadProjects(); }}
        />
      )}
    </div>
  );
}

interface ProjectFormValues {
  name: string;
  description: string | null;
  project_type: string;
  address: string | null;
}

function SummaryCard({ icon, label, value }: { icon: React.ReactNode; label: string; value: string }) {
  return (
    <div className={styles.summaryCard}>
      <div className={styles.summaryIcon}>{icon}</div>
      <div><span>{label}</span><strong>{value}</strong></div>
    </div>
  );
}

function ProjectCard({ project, canManage, onOpen, onEdit, onDelete }: { project: ProjectItem; canManage: boolean; onOpen: () => void; onEdit: () => void; onDelete: () => void }) {
  return (
    <article className={styles.projectCard}>
      <button className={styles.cardMain} onClick={onOpen} type="button">
        <div className={styles.cardTop}>
          <Badge variant={statusVariant(project.status)}>{project.status.replaceAll('_', ' ')}</Badge>
          <span className={styles.projectType}>{project.project_type.replaceAll('_', ' ')}</span>
        </div>
        <h3>{project.name}</h3>
        <p>{project.address || 'Address not provided'}</p>
        <div className={styles.cardStats}>
          <span><FileText size={14} /> {project.documents_count} documents</span>
          <span>v{project.latest_version_number ?? 1}</span>
        </div>
      </button>
      {canManage && (
        <div className={styles.cardActions}>
          <Button variant="ghost" size="sm" icon={<Pencil size={14} />} onClick={onEdit}>Modify</Button>
          <Button variant="ghost" size="sm" icon={<Trash2 size={14} />} onClick={onDelete}>Delete</Button>
        </div>
      )}
    </article>
  );
}

function ProjectDetailsModal({ project, canManage, onClose, onEdit, onDelete }: { project: ProjectItem; canManage: boolean; onClose: () => void; onEdit: () => void; onDelete: () => void }) {
  const [documents, setDocuments] = useState<DocumentSummary[]>([]);
  const [documentsLoading, setDocumentsLoading] = useState(true);
  const [documentsError, setDocumentsError] = useState('');
  const [downloadingId, setDownloadingId] = useState<string | null>(null);
  const [documentAnalyses, setDocumentAnalyses] = useState<Record<string, DocumentAnalysis>>({});
  const [analysesLoading, setAnalysesLoading] = useState(false);
  const [reraNumber, setReraNumber] = useState('');
  const [reraBusy, setReraBusy] = useState(false);
  const [reraResult, setReraResult] = useState<any>(null);
  const [complianceBusy, setComplianceBusy] = useState(false);
  const [complianceResults, setComplianceResults] = useState<any[]>([]);
  const [complianceMessage, setComplianceMessage] = useState('');

  useEffect(() => {
    let active = true;
    setDocumentsLoading(true);
    setDocumentsError('');
    apiClient.get<DocumentSummary[]>(`/api/v1/documents/project/${project.id}`)
      .then(async (response) => {
        if (!active) return;
        setDocuments(response.data);
        setAnalysesLoading(true);
        const entries = await Promise.all(response.data.map(async (document) => {
          try {
            const analysisResponse = await apiClient.get<DocumentAnalysis>(`/api/v1/documents/${document.id}/analysis`);
            return [document.id, analysisResponse.data] as const;
          } catch {
            return null;
          }
        }));
        if (active) {
          setDocumentAnalyses(Object.fromEntries(entries.filter(Boolean) as Array<readonly [string, DocumentAnalysis]>));
          setAnalysesLoading(false);
        }
      })
      .catch((error: any) => { if (active) setDocumentsError(error.response?.data?.detail || 'Unable to load project documents.'); })
      .finally(() => { if (active) setDocumentsLoading(false); });
    return () => { active = false; };
  }, [project.id]);

  const runCompliance = async () => {
    setComplianceBusy(true);
    setComplianceMessage('');
    try {
      const run = await apiClient.post(`/api/v1/projects/${project.id}/evaluations/run`);
      const response = await apiClient.get(`/api/v1/projects/${project.id}/evaluations/${run.data.id}/results`);
      setComplianceResults(response.data.results || []);
      setComplianceMessage(`Evaluation ${response.data.evaluation_run?.status || 'completed'}. Results below reflect configured rules and available trusted evidence.`);
    } catch (error: any) {
      setComplianceMessage(error.response?.data?.detail || 'Unable to run compliance evaluation.');
    } finally { setComplianceBusy(false); }
  };

  const verifyRera = async () => {
    if (!reraNumber.trim()) return;
    setReraBusy(true);
    setReraResult(null);
    try {
      const response = await apiClient.post(`/api/v1/projects/${project.id}/rera-verifications`, {
        registration_number: reraNumber.trim(),
        expected_project_name: project.name,
      });
      setReraResult(response.data);
    } catch (error: any) {
      setReraResult({ status: 'ERROR', message: error.response?.data?.detail || 'Unable to check official RERA source.' });
    } finally { setReraBusy(false); }
  };

  const downloadDocument = async (document: DocumentSummary) => {
    setDownloadingId(document.id);
    try {
      const response = await apiClient.get(`/api/v1/documents/${document.id}/download`, { responseType: 'blob' });
      const blobUrl = URL.createObjectURL(response.data);
      const anchor = window.document.createElement('a');
      anchor.href = blobUrl;
      anchor.download = document.title || 'property-document';
      window.document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(blobUrl);
    } catch (error: any) {
      window.alert(error.response?.data?.detail || 'Unable to download this document.');
    } finally {
      setDownloadingId(null);
    }
  };

  return (
    <Modal title="Project details" onClose={onClose} wide>
      <div className={styles.detailGrid}>
        <Detail label="Name" value={project.name} />
        <Detail label="Type" value={project.project_type.replaceAll('_', ' ')} />
        <Detail label="Address" value={project.address || 'Not provided'} />
        <Detail label="Status" value={project.status} />
        <Detail label="Documents" value={String(project.documents_count)} />
        <Detail label="Latest version" value={project.latest_version_number ? `v${project.latest_version_number}` : 'No version'} />
        <Detail label="Compliance score" value={project.compliance_score == null ? 'Not calculated yet' : String(project.compliance_score)} />
      </div>
      {project.description && <div className={styles.descriptionBox}>{project.description}</div>}

      <div className={styles.documentPanel}>
        <div className={styles.documentPanelHeader}>
          <div><h3>Uploaded documents</h3><p>Documents available to your account for this project.</p></div>
          <Badge variant="info">{documents.length}</Badge>
        </div>
        {documentsLoading ? (
          <div className={styles.documentEmpty}><Loader2 className={styles.spin} size={18} /> Loading documents...</div>
        ) : documentsError ? (
          <div className={styles.documentError}><AlertCircle size={16} /> {documentsError}</div>
        ) : documents.length === 0 ? (
          <div className={styles.documentEmpty}><FileText size={18} /> No documents are visible to this account.</div>
        ) : (
          <div className={styles.documentList}>
            {documents.map((document) => (
              <div className={styles.documentRow} key={document.id}>
                <div className={styles.documentIcon}><FileText size={18} /></div>
                <div className={styles.documentInfo}>
                  <strong>{document.title}</strong>
                  <span>{document.document_type.replaceAll('_', ' ')} · {document.status}</span>
                </div>
                <Badge variant={document.visibility === 'BUYER_VISIBLE' ? 'success' : 'default'}>{document.visibility.replaceAll('_', ' ')}</Badge>
                <Button variant="outline" size="sm" icon={<Download size={14} />} isLoading={downloadingId === document.id} onClick={() => void downloadDocument(document)}>Download</Button>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className={styles.extractionPanel}>
        <div className={styles.documentPanelHeader}>
          <div><h3>Extracted project details</h3><p>OCR/text extraction and AI fields available from buyer-visible documents.</p></div>
          {analysesLoading && <Loader2 className={styles.spin} size={16} />}
        </div>
        {Object.keys(documentAnalyses).length === 0 && !analysesLoading ? (
          <div className={styles.documentEmpty}><FileText size={18} /> No extracted fields are available yet.</div>
        ) : (
          <div className={styles.extractionList}>
            {documents.map((document) => {
              const analysis = documentAnalyses[document.id];
              if (!analysis) return null;
              const semantic = analysis.evidence.filter((item) => item.field_name !== 'page_text' && item.field_value);
              return (
                <div className={styles.extractionDocument} key={`analysis-${document.id}`}>
                  <div className={styles.extractionDocumentHeader}>
                    <strong>{document.title}</strong>
                    <Badge variant={analysis.status === 'COMPLETED' ? 'success' : 'warning'}>{analysis.detected_document_type || document.document_type}</Badge>
                  </div>
                  {analysis.summary && <p className={styles.extractionSummary}>{analysis.summary}</p>}
                  {semantic.length > 0 ? semantic.map((item) => (
                    <div className={styles.extractionField} key={`${document.id}-${item.id}-${item.field_name}`}>
                      <span>{item.field_name.replaceAll('_', ' ')}</span>
                      <strong>{item.field_value}</strong>
                      <small>{item.source || 'AI'}{item.confidence != null ? ` · ${Math.round(item.confidence * 100)}% confidence` : ''}</small>
                    </div>
                  )) : <span className={styles.formHint}>No semantic fields extracted yet.</span>}
                </div>
              );
            })}
          </div>
        )}
      </div>

      {canManage && (
        <section className={styles.documentPanel}>
          <div className={styles.documentPanelHeader}>
            <div><h3>Rule-based compliance verification</h3><p>Evaluates configured rules against trusted structured evidence. Document presence alone does not validate contents.</p></div>
          </div>
          <Button icon={<Play size={15} />} isLoading={complianceBusy} onClick={() => void runCompliance()}>Run compliance rules</Button>
          {complianceMessage && <p className={styles.formHint}>{complianceMessage}</p>}
          {complianceResults.map((result, index) => (
            <div className={styles.extractionField} key={result.id || `${result.rule_version_id}-${index}`}>
              <span>{result.outcome || 'RESULT'}</span><strong>{result.explanation || 'No explanation returned.'}</strong>
            </div>
          ))}
        </section>
      )}

      {canManage && (
        <section className={styles.documentPanel}>
          <div className={styles.documentPanelHeader}>
            <div><h3>Official Telangana RERA verification</h3><p>Checks the official public portal when an unambiguous result is accessible. CAPTCHA, unavailable pages, or ambiguous results require manual review.</p></div>
          </div>
          <div className={styles.inlineForm}>
            <Input label="RERA registration number" value={reraNumber} onChange={(event) => setReraNumber(event.target.value)} placeholder="e.g. P02400000000" required />
            <Button icon={<Globe size={15} />} isLoading={reraBusy} onClick={() => void verifyRera()}>Check official source</Button>
          </div>
          {reraResult && (
            <div className={styles.extractionDocument}>
              <div className={styles.extractionDocumentHeader}><strong>Verification status</strong><Badge variant={reraResult.status === 'VERIFIED' ? 'success' : reraResult.status === 'MISMATCH' ? 'danger' : 'warning'}>{String(reraResult.status).replaceAll('_', ' ')}</Badge></div>
              <p className={styles.extractionSummary}>{reraResult.message}</p>
              {reraResult.source_url && <a href={reraResult.source_url} target="_blank" rel="noreferrer">Open official source</a>}
              {reraResult.checked_at && <small>Checked: {new Date(reraResult.checked_at).toLocaleString()}</small>}
            </div>
          )}
        </section>
      )}

      <div className={styles.modalFooter}>
        {canManage && <Button variant="outline" icon={<Pencil size={15} />} onClick={onEdit}>Modify</Button>}
        {canManage && <Button variant="danger" icon={<Trash2 size={15} />} onClick={onDelete}>Delete</Button>}
        <Button variant="ghost" onClick={onClose}>Close</Button>
      </div>
    </Modal>
  );
}

function Detail({ label, value }: { label: string; value: string }) {
  return <div className={styles.detail}><span>{label}</span><strong>{value}</strong></div>;
}

function ProjectFormModal({ project, onClose, onSave }: { project: ProjectItem | null; onClose: () => void; onSave: (payload: ProjectFormValues) => Promise<void> }) {
  const [form, setForm] = useState<ProjectFormValues>({
    name: project?.name || '',
    description: project?.description || '',
    project_type: project?.project_type || 'APARTMENT',
    address: project?.address || '',
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  const submit = async (event: React.FormEvent) => {
    event.preventDefault();
    setSaving(true);
    setError('');
    try { await onSave(form); } catch (err) { setError(err instanceof Error ? err.message : 'Unable to save project.'); } finally { setSaving(false); }
  };

  return (
    <Modal title={project ? 'Modify project' : 'Project details'} onClose={onClose}>
      <form className={styles.form} onSubmit={submit}>
        {error && <div className={styles.errorBanner}>{error}</div>}
        <Input label="Project name" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} required />
        <label className={styles.fieldLabel}>Property type<select value={form.project_type} onChange={(e) => setForm({ ...form, project_type: e.target.value })}>{PROJECT_TYPES.map((item) => <option key={item.value} value={item.value}>{item.label}</option>)}</select></label>
        <Input label="Address" value={form.address || ''} onChange={(e) => setForm({ ...form, address: e.target.value })} placeholder="Hyderabad, Telangana" />
        <label className={styles.fieldLabel}>Description<textarea rows={4} value={form.description || ''} onChange={(e) => setForm({ ...form, description: e.target.value })} /></label>
        <div className={styles.modalFooter}><Button variant="ghost" type="button" onClick={onClose}>Cancel</Button><Button type="submit" isLoading={saving}>{project ? 'Save changes' : 'Create project'}</Button></div>
      </form>
    </Modal>
  );
}

function CreateProjectWizard({ onClose, onCreated }: { onClose: () => void; onCreated: () => Promise<void> }) {
  const [step, setStep] = useState<WizardStep>('details');
  const [project, setProject] = useState<ProjectItem | null>(null);
  const [form, setForm] = useState<ProjectFormValues>({ name: '', description: '', project_type: 'APARTMENT', address: '' });
  const [requirements, setRequirements] = useState<RequiredDocument[]>([]);
  const [files, setFiles] = useState<Record<string, File>>({});
  const [processing, setProcessing] = useState<ProcessingItem[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');

  const mandatory = requirements.filter((item) => item.is_mandatory);
  const missingMandatory = mandatory.filter((item) => !files[item.document_type]);

  const createProject = async (event: React.FormEvent) => {
    event.preventDefault();
    setBusy(true);
    setError('');
    try {
      const response = await apiClient.post<ProjectItem>('/api/v1/projects', {
        ...form,
        description: form.description || null,
        address: form.address || null,
      });
      setProject(response.data);
      const docs = await apiClient.get<RequiredDocument[]>('/api/v1/projects/required-documents', { params: { project_type: form.project_type } });
      setRequirements(docs.data);
      setStep('documents');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Project creation failed. Verify that your Builder account is approved.');
    } finally { setBusy(false); }
  };

  const processDocuments = async () => {
    if (!project || missingMandatory.length) return;
    setBusy(true);
    setError('');
    setStep('processing');
    const items: ProcessingItem[] = requirements.filter((item) => files[item.document_type]).map((requirement) => ({ requirement, fileName: files[requirement.document_type].name, status: 'QUEUED' }));
    setProcessing(items);

    const allEvidence: EvidenceItem[] = [];
    try {
      for (let index = 0; index < items.length; index += 1) {
        const item = items[index];
        const file = files[item.requirement.document_type];
        try {
          updateProcessing(setProcessing, index, { status: 'PROCESSING' });
          const validation = new FormData();
          validation.append('file', file);
          validation.append('document_type', item.requirement.document_type);
          const validationResponse = await apiClient.post('/api/v1/documents/validate', validation, { headers: { 'Content-Type': 'multipart/form-data' } });
          if (!validationResponse.data.is_valid) throw new Error(validationResponse.data.error || 'Document validation failed.');

          const upload = new FormData();
          upload.append('project_id', project.id);
          upload.append('document_type', item.requirement.document_type);
          upload.append('title', file.name);
          upload.append('file', file);
          upload.append('description', item.requirement.description);
          upload.append('visibility', 'BUYER_VISIBLE');
          const documentResponse = await apiClient.post<{ id: string }>('/api/v1/documents', upload, { headers: { 'Content-Type': 'multipart/form-data' } });
          const detail = await apiClient.get<DocumentDetail>(`/api/v1/documents/${documentResponse.data.id}`);
          const latest = detail.data.versions[0];
          if (!latest) throw new Error('Document version was not created.');
          await apiClient.post(`/api/v1/documents/versions/${latest.id}/process`);

          const completed = await waitForDocumentCompletion(documentResponse.data.id);
          updateProcessing(setProcessing, index, { status: completed.status as ProcessingItem['status'], documentId: completed.id });

          if (completed.status === 'COMPLETED') {
            try {
              const analysis = await waitForAnalysis(completed.id);
              updateProcessing(setProcessing, index, { analysis });
              allEvidence.push(...analysis.evidence.filter((e) => e.field_name !== 'page_text' && Boolean(e.field_value)));
            } catch {
              // Processing can complete before an analysis is immediately readable; keep the document result.
            }
          }
        } catch (err: any) {
          updateProcessing(setProcessing, index, { status: 'FAILED', error: err.response?.data?.detail || err.message || 'Processing failed.' });
        }
      }

      await applyExtractedDetails(project.id, form, allEvidence);
      await onCreated();
      setStep('review');
    } finally { setBusy(false); }
  };

  return (
    <Modal title="Create project with document verification" onClose={onClose} wide>
      <div className={styles.wizardSteps}>
        <WizardStepIndicator active={step === 'details'} done={step !== 'details'} label="1. Project" />
        <ArrowRight size={15} />
        <WizardStepIndicator active={step === 'documents'} done={step === 'processing' || step === 'complete'} label="2. Documents" />
        <ArrowRight size={15} />
        <WizardStepIndicator active={step === 'processing'} done={step === 'review' || step === 'complete'} label="3. OCR / AI" />
        <ArrowRight size={15} />
        <WizardStepIndicator active={step === 'review'} done={step === 'complete'} label="4. Extracted details" />
        <ArrowRight size={15} />
        <WizardStepIndicator active={step === 'complete'} done={false} label="5. Finish" />
      </div>

      {error && <div className={styles.errorBanner}><AlertCircle size={17} />{error}</div>}

      {step === 'details' && (
        <form className={styles.form} onSubmit={createProject}>
          <div className={styles.notice}><ShieldCheck size={18} /><div><strong>Verified Builder only</strong><span>Your backend account must be ADMIN-verified before a project can be created.</span></div></div>
          <Input label="Initial project name" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} placeholder="e.g. Green Valley Apartments" required />
          <label className={styles.fieldLabel}>Property type<select value={form.project_type} onChange={(e) => setForm({ ...form, project_type: e.target.value })}>{PROJECT_TYPES.map((item) => <option key={item.value} value={item.value}>{item.label}</option>)}</select></label>
          <Input label="Initial address" value={form.address || ''} onChange={(e) => setForm({ ...form, address: e.target.value })} placeholder="Hyderabad, Telangana" />
          <label className={styles.fieldLabel}>Initial description<textarea rows={3} value={form.description || ''} onChange={(e) => setForm({ ...form, description: e.target.value })} placeholder="Optional. Document extraction can enrich this later." /></label>
          <div className={styles.modalFooter}><Button variant="ghost" type="button" onClick={onClose}>Cancel</Button><Button type="submit" isLoading={busy} icon={<ArrowRight size={16} />}>Create and continue</Button></div>
        </form>
      )}

      {step === 'documents' && (
        <div className={styles.form}>
          <div className={styles.notice}><FileCheck2 size={18} /><div><strong>Upload project documents</strong><span>Mandatory documents must be supplied before processing can start. Files are stored privately in MinIO.</span></div></div>
          <div className={styles.requirementList}>
            {requirements.map((requirement) => (
              <DocumentRequirement key={requirement.document_type} requirement={requirement} file={files[requirement.document_type]} onFile={(file) => setFiles((current) => ({ ...current, [requirement.document_type]: file }))} />
            ))}
          </div>
          <div className={styles.modalFooter}><Button variant="ghost" onClick={() => setStep('details')}>Back</Button><Button disabled={missingMandatory.length > 0} icon={<ArrowRight size={16} />} onClick={() => void processDocuments()}>Process documents</Button></div>
          {missingMandatory.length > 0 && <p className={styles.formHint}>Upload all mandatory documents to continue.</p>}
        </div>
      )}

      {step === 'processing' && (
        <div className={styles.form}>
          <div className={styles.notice}><Loader2 className={styles.spin} size={18} /><div><strong>Processing documents</strong><span>Text PDFs use PyMuPDF. Scanned PDFs are sent to the OCR worker, then the AI provider extracts evidence.</span></div></div>
          <div className={styles.processingList}>{processing.map((item) => <ProcessingRow key={item.requirement.document_type} item={item} />)}</div>
          <div className={styles.modalFooter}><span className={styles.formHint}>{busy ? 'Waiting for the processing pipeline...' : 'Processing finished.'}</span></div>
        </div>
      )}

      {step === 'review' && (
        <div className={styles.form}>
          <div className={styles.notice}><CheckCircle2 size={18} /><div><strong>Extraction completed</strong><span>The next page shows the text/AI fields extracted from each uploaded document. Review these values before finishing the project setup.</span></div></div>
          <ExtractionResults processing={processing} />
          <div className={styles.modalFooter}><Button variant="ghost" onClick={() => setStep('documents')}>Back to documents</Button><Button onClick={() => setStep('complete')}>Finish project setup</Button></div>
        </div>
      )}

      {step === 'complete' && (
        <div className={styles.completeState}>
          <div className={styles.successCircle}><CheckCircle2 size={34} /></div>
          <h3>Project setup completed</h3>
          <p>The required documents were uploaded and sent through the document-processing pipeline. Extracted semantic evidence was applied where the AI provider returned a unique value.</p>
          <p className={styles.formHint}>The extracted fields remain available from the project details view for the builder and customer.</p>
          <div className={styles.modalFooter}><Button onClick={onClose}>Open project workspace</Button></div>
        </div>
      )}
    </Modal>
  );
}

function WizardStepIndicator({ active, done, label }: { active: boolean; done: boolean; label: string }) {
  return <span className={`${styles.wizardStep} ${active ? styles.wizardStepActive : ''} ${done ? styles.wizardStepDone : ''}`}>{done ? <CheckCircle2 size={14} /> : null}{label}</span>;
}

function DocumentRequirement({ requirement, file, onFile }: { requirement: RequiredDocument; file?: File; onFile: (file: File) => void }) {
  return (
    <div className={styles.requirementRow}>
      <div className={styles.requirementInfo}><div className={styles.requirementTitle}><strong>{requirement.name}</strong>{requirement.is_mandatory && <Badge variant="danger" size="sm">Mandatory</Badge>}</div><span>{requirement.description}</span><small>{requirement.authority} · {requirement.category}</small></div>
      <label className={styles.fileButton}><UploadCloud size={16} />{file ? file.name : 'Choose file'}<input type="file" accept={requirement.accepted_formats.join(',')} onChange={(event) => { const selected = event.target.files?.[0]; if (selected) onFile(selected); }} /></label>
    </div>
  );
}

function ProcessingRow({ item }: { item: ProcessingItem }) {
  const variant = item.status === 'COMPLETED' ? 'success' : item.status === 'FAILED' ? 'danger' : 'warning';
  return <div className={styles.processingRow}><div><strong>{item.requirement.name}</strong><span>{item.fileName}</span></div><div className={styles.processingStatus}>{item.status === 'PROCESSING' && <Loader2 className={styles.spin} size={15} />}{item.status === 'COMPLETED' && <CheckCircle2 size={15} />}{item.status === 'FAILED' && <AlertCircle size={15} />}<Badge variant={variant}>{item.status}</Badge></div>{item.error && <p className={styles.processingError}>{item.error}</p>}</div>;
}

function ExtractionResults({ processing }: { processing: ProcessingItem[] }) {
  return (
    <div className={styles.extractionResults}>
      {processing.map((item) => {
        const semantic = item.analysis?.evidence.filter((evidence) => evidence.field_name !== 'page_text' && evidence.field_value) || [];
        return (
          <section className={styles.extractionDocument} key={`result-${item.requirement.document_type}`}>
            <div className={styles.extractionDocumentHeader}>
              <div><strong>{item.requirement.name}</strong><span>{item.fileName}</span></div>
              <Badge variant={item.status === 'COMPLETED' ? 'success' : 'danger'}>{item.status}</Badge>
            </div>
            {item.analysis?.summary && <p className={styles.extractionSummary}>{item.analysis.summary}</p>}
            {semantic.length > 0 ? semantic.map((evidence) => (
              <div className={styles.extractionField} key={`${item.requirement.document_type}-${evidence.id}-${evidence.field_name}`}>
                <span>{evidence.field_name.replaceAll('_', ' ')}</span>
                <strong>{evidence.field_value}</strong>
                <small>{evidence.source || 'AI'}{evidence.page_number != null ? ` · page ${evidence.page_number}` : ''}{evidence.confidence != null ? ` · ${Math.round(evidence.confidence * 100)}% confidence` : ''}</small>
              </div>
            )) : (
              <div className={styles.extractionNoData}>{item.status === 'COMPLETED' ? 'No semantic fields were returned. Raw page text may still have been extracted.' : (item.error || 'Document processing failed.')}</div>
            )}
          </section>
        );
      })}
    </div>
  );
}


function Modal({ title, onClose, children, wide = false }: { title: string; onClose: () => void; children: React.ReactNode; wide?: boolean }) {
  return <div className={styles.modalBackdrop}><div className={`${styles.modal} ${wide ? styles.modalWide : ''}`}><div className={styles.modalHeader}><h2>{title}</h2><button type="button" className={styles.closeButton} onClick={onClose} aria-label="Close"><X size={18} /></button></div>{children}</div></div>;
}

function updateProcessing(setter: React.Dispatch<React.SetStateAction<ProcessingItem[]>>, index: number, patch: Partial<ProcessingItem>) {
  setter((current) => current.map((item, itemIndex) => itemIndex === index ? { ...item, ...patch } : item));
}

async function waitForDocumentCompletion(documentId: string): Promise<DocumentDetail> {
  for (let attempt = 0; attempt < 90; attempt += 1) {
    const response = await apiClient.get<DocumentDetail>(`/api/v1/documents/${documentId}`);
    const latest = response.data.versions[0];
    if (latest && ['COMPLETED', 'FAILED'].includes(latest.processing_status)) return { ...response.data, status: latest.processing_status };
    await new Promise((resolve) => window.setTimeout(resolve, 2000));
  }
  throw new Error('Document processing timed out after 3 minutes.');
}

async function waitForAnalysis(documentId: string): Promise<DocumentAnalysis> {
  for (let attempt = 0; attempt < 10; attempt += 1) {
    try {
      const response = await apiClient.get<DocumentAnalysis>(`/api/v1/documents/${documentId}/analysis`);
      return response.data;
    } catch (error: any) {
      if (error.response?.status !== 404 || attempt === 9) throw error;
      await new Promise((resolve) => window.setTimeout(resolve, 1000));
    }
  }
  throw new Error('Analysis result was not available.');
}


async function applyExtractedDetails(projectId: string, currentForm: ProjectFormValues, evidence: EvidenceItem[]) {
  const values = new Map<string, Set<string>>();
  for (const item of evidence) {
    if (!item.field_value || item.field_name === 'page_text') continue;
    const key = item.field_name.toLowerCase();
    if (!values.has(key)) values.set(key, new Set());
    values.get(key)?.add(item.field_value.trim());
  }
  const unique = (keys: string[]) => {
    const matches = keys.flatMap((key) => [...(values.get(key) || [])]);
    return [...new Set(matches)].length === 1 ? [...new Set(matches)][0] : undefined;
  };
  const extractedName = unique(['project_name', 'property_name']);
  const extractedAddress = unique(['address', 'location']);
  const extractedDescription = unique(['summary']);
  const patch: ProjectFormValues = {
    name: extractedName || currentForm.name,
    address: extractedAddress || currentForm.address || null,
    description: extractedDescription || currentForm.description || null,
    project_type: currentForm.project_type,
  };
  if (patch.name !== currentForm.name || patch.address !== currentForm.address || patch.description !== currentForm.description) {
    await apiClient.patch(`/api/v1/projects/${projectId}`, patch);
  }
}
