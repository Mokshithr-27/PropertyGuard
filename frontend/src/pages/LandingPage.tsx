/**
 * PropertyGuard Public Landing Page Component
 * Showcases the platform value proposition, architecture trust boundaries,
 * multi-tier compliance breakdown, deterministic evaluation overview, and call-to-actions.
 */

import { useState, useId } from 'react';
import { Link } from 'react-router-dom';
import {
  ShieldCheck,
  AlertTriangle,
  FileCheck,
  Building2,
  Sparkles,
  Search,
  CheckCircle2,
  XCircle,
  Play,
  Layers,
  ArrowRight,
  Flame,
  Scale,
  Leaf,
  ChevronDown,
  Lock,
  Cpu,
  RefreshCw,
  Sliders,
  History,
  Info
} from 'lucide-react';
import { Navbar } from '../components/layout/Navbar';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import styles from './LandingPage.module.css';

// Preset Property Demos
interface PropertyPreset {
  id: string;
  name: string;
  type: string;
  location: string;
  floors: number;
  plotAreaSqFt: number;
  roadWidthM: number;
  score: number;
  riskLevel: 'LOW RISK' | 'MODERATE RISK' | 'HIGH RISK';
  riskColor: string;
  findings: Array<{
    id: string;
    rule: string;
    severity: 'pass' | 'warning' | 'critical';
    title: string;
    description: string;
    remediation: string;
  }>;
}

const PRESETS: PropertyPreset[] = [
  {
    id: 'cybercity',
    name: 'CyberCity One Tech Park',
    type: 'Commercial IT High-Rise',
    location: 'Hitec City, Hyderabad',
    floors: 34,
    plotAreaSqFt: 185000,
    roadWidthM: 36,
    score: 94,
    riskLevel: 'LOW RISK',
    riskColor: 'var(--color-success)',
    findings: [
      {
        id: 'F-01',
        rule: 'NBC-2016-FIRE-S4',
        severity: 'pass',
        title: 'Fire Engine Setback Clearance Passed',
        description: 'Perimeter setback of 12.4m exceeds minimum required 9.0m for buildings above 60m height.',
        remediation: 'No action required. Meets NBC 2016 Part 4.'
      },
      {
        id: 'F-02',
        rule: 'RERA-TITLE-ENC-09',
        severity: 'pass',
        title: '30-Year Title Search Encumbrance Free',
        description: 'Continuous legal ownership verified from 1994 to date without pending litigation or mortgage hold.',
        remediation: 'Verified through State Registration and Stamps Department records.'
      },
      {
        id: 'F-03',
        rule: 'ZONING-FSI-FAR-12',
        severity: 'warning',
        title: 'Premium FSI Fee Confirmation Pending',
        description: 'Utilized FSI is 3.8 vs base permissible 2.5. Verification of paid municipal betterment charges required.',
        remediation: 'Upload GHMC / Municipal receipt for premium FSI allocation to clear warning.'
      }
    ]
  },
  {
    id: 'emerald',
    name: 'Emerald Palm Residences',
    type: 'Luxury Residential Township',
    location: 'Whitefield, Bangalore',
    floors: 18,
    plotAreaSqFt: 340000,
    roadWidthM: 24,
    score: 76,
    riskLevel: 'MODERATE RISK',
    riskColor: 'var(--color-warning)',
    findings: [
      {
        id: 'F-11',
        rule: 'PCB-ENV-WETLAND-03',
        severity: 'warning',
        title: 'Secondary Canal Buffer Zone Proximity',
        description: 'Eastern boundary is situated 32m from designated stormwater lake canal. Minimum green buffer is 30m.',
        remediation: 'Conduct certified GIS survey to assure permanent no-construction green strip.'
      },
      {
        id: 'F-12',
        rule: 'RERA-ESCROW-SEC4',
        severity: 'pass',
        title: '70% Designated Escrow Account Active',
        description: 'Compliant with RERA Section 4(2)(l)(D) scheduled bank account declaration.',
        remediation: 'Verified via Form 3 Chartered Accountant declaration.'
      },
      {
        id: 'F-13',
        rule: 'STRUCT-IS1893-SEISMIC',
        severity: 'warning',
        title: 'Seismic Zone II Soft-Storey Ductility Review',
        description: 'Stilt parking level requires peer structural review verification for shear wall damping.',
        remediation: 'Submit third-party structural stability certificate from IIT / NIT civil dept.'
      }
    ]
  },
  {
    id: 'metrocrest',
    name: 'Metro Crest Towers',
    type: 'Mixed-Use Retail & Apartments',
    location: 'Sector 62, Noida',
    floors: 28,
    plotAreaSqFt: 98000,
    roadWidthM: 18,
    score: 42,
    riskLevel: 'HIGH RISK',
    riskColor: 'var(--color-danger)',
    findings: [
      {
        id: 'F-21',
        rule: 'FIRE-NOC-HIGHRISE-01',
        severity: 'critical',
        title: 'Provisional Fire NOC Expired Over 90 Days',
        description: 'Provisional Fire Safety Clearance expired on 14-Jan-2026. No final Fire OC renewal on file.',
        remediation: 'Critical: Immediate filing with Chief Fire Officer required before occupancy or sale.'
      },
      {
        id: 'F-22',
        rule: 'BYLAW-ROAD-HEIGHT-04',
        severity: 'critical',
        title: 'Road Width Height Limitation Breach',
        description: 'Proposed 28 storeys (92m) violates permissible height for 18m road width (max allowed 75m).',
        remediation: 'Must seek High-Rise Building Committee special sanction or adjust upper penthouse floor plans.'
      },
      {
        id: 'F-23',
        rule: 'TITLE-DISPUTE-LIT-08',
        severity: 'warning',
        title: 'Active Revenue Court Appeal Disclosed',
        description: 'Civil dispute pending in District Revenue Court concerning parcel #49 boundary claim.',
        remediation: 'Requires legal indemnity bond and title insurance policy rider.'
      }
    ]
  }
];

export function LandingPage() {
  const plotAreaId = useId();
  const roadWidthId = useId();
  const zoneTypeId = useId();

  // Scanner Simulator State
  const [selectedPresetId, setSelectedPresetId] = useState<string>('cybercity');
  const [isScanning, setIsScanning] = useState(false);
  const [scanProgress, setScanProgress] = useState(100);
  const [activeChecklist, setActiveChecklist] = useState({
    zoning: true,
    title: true,
    fire: true,
    env: true,
    structural: true
  });
  const [filterFinding, setFilterFinding] = useState<'all' | 'critical' | 'warning' | 'pass'>('all');

  // Interactive Bylaw Calculator State
  const [calcPlotArea, setCalcPlotArea] = useState<number>(25000);
  const [calcRoadWidth, setCalcRoadWidth] = useState<number>(24);
  const [calcZone, setCalcZone] = useState<'commercial' | 'residential' | 'mixed'>('commercial');

  // FAQ open states
  const [openFaq, setOpenFaq] = useState<number | null>(0);

  const currentPreset = PRESETS.find((p) => p.id === selectedPresetId) || PRESETS[0];

  const handleRunScan = () => {
    setIsScanning(true);
    setScanProgress(10);

    const interval = setInterval(() => {
      setScanProgress((prev) => {
        if (prev >= 95) {
          clearInterval(interval);
          setIsScanning(false);
          return 100;
        }
        return prev + 25;
      });
    }, 250);
  };

  const handleSelectPreset = (id: string) => {
    setSelectedPresetId(id);
    setScanProgress(0);
    setIsScanning(true);
    setTimeout(() => {
      setScanProgress(100);
      setIsScanning(false);
    }, 400);
  };

  // Calculator computations
  const getFsiMultiplier = () => {
    if (calcZone === 'commercial') return calcRoadWidth >= 30 ? 3.5 : calcRoadWidth >= 18 ? 2.75 : 2.0;
    if (calcZone === 'mixed') return calcRoadWidth >= 24 ? 3.0 : 2.25;
    return calcRoadWidth >= 18 ? 2.5 : 1.75;
  };

  const computedFsi = getFsiMultiplier();
  const computedBuiltUp = Math.round(calcPlotArea * computedFsi);
  const frontSetback = (calcRoadWidth * 0.35 + 2).toFixed(1);
  const maxFloorsApprox = Math.floor((computedBuiltUp / (calcPlotArea * 0.45)));

  const filteredFindings = currentPreset.findings.filter((f) => {
    if (filterFinding === 'all') return true;
    return f.severity === filterFinding;
  });

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className={styles.page}>
      <Navbar />

      {/* Hero Section */}
      <section className={styles.heroSection}>
        <div className={styles.heroGlow} />

        <div className={styles.heroContent}>
          <div className={styles.pillBadge}>
            <Sparkles size={14} className={styles.sparkleIcon} />
            <span>Enterprise Property Compliance & Risk Intelligence</span>
            <Badge variant="cyan" size="sm">v2.4 AI Engine</Badge>
          </div>

          <h1 className={styles.heroTitle}>
            Protect Every Property Decision with{' '}
            <span className="gradient-text-cyan">Deterministic AI Compliance</span>.
          </h1>

          <p className={styles.heroSubtitle}>
            PropertyGuard AI cross-examines title deeds, municipal zoning bylaws, environmental clearances,
            and structural certifications in seconds — catching violations before they turn into costly litigations.
          </p>

          <div className={styles.heroActions}>
            <Button
              size="lg"
              variant="glow"
              icon={<Play size={18} />}
              onClick={() => scrollToSection('scanner')}
            >
              Launch Live Scanner
            </Button>
            <Link to="/register">
              <Button size="lg" variant="outline" icon={<ArrowRight size={18} />} iconPosition="right">
                Create Builder Account
              </Button>
            </Link>
            <Link to="/login">
              <Button size="lg" variant="secondary">
                View Interactive Demo
              </Button>
            </Link>
          </div>

          {/* Metrics Ticker */}
          <div className={styles.metricsGrid}>
            <div className={styles.metricCard}>
              <div className={styles.metricValue}>$4.8B+</div>
              <div className={styles.metricLabel}>Assets Evaluated</div>
            </div>
            <div className={styles.metricCard}>
              <div className={styles.metricValue}>14,800+</div>
              <div className={styles.metricLabel}>Documents Audited</div>
            </div>
            <div className={styles.metricCard}>
              <div className={styles.metricValue}>99.4%</div>
              <div className={styles.metricLabel}>Violation Detection</div>
            </div>
            <div className={styles.metricCard}>
              <div className={styles.metricValue}>&lt; 1.8s</div>
              <div className={styles.metricLabel}>Audit Latency</div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Live Risk Scanner Section */}
      <section id="scanner" className={styles.section}>
        <div className={styles.sectionHeader}>
          <span className={styles.sectionPill}>Interactive Simulation</span>
          <h2 className={styles.sectionTitle}>
            Experience the <span className="gradient-text">Real-Time Risk Engine</span>
          </h2>
          <p className={styles.sectionDescription}>
            Select a sample property preset below or toggle compliance verification modules to see how
            PropertyGuard AI parses complex regulations, scores risk, and generates actionable remedies.
          </p>
        </div>

        <div className={styles.simulatorCard}>
          {/* Top Bar Controls */}
          <div className={styles.simulatorTopBar}>
            <div className={styles.simulatorControls}>
              <span style={{ fontSize: '0.8125rem', fontWeight: 600, color: 'var(--color-text-dim)' }}>
                SELECT PROPERTY PRESET:
              </span>
              {PRESETS.map((p) => (
                <button
                  key={p.id}
                  type="button"
                  className={`${styles.presetBtn} ${selectedPresetId === p.id ? styles.presetBtnActive : ''}`}
                  onClick={() => handleSelectPreset(p.id)}
                >
                  {p.name} ({p.riskLevel})
                </button>
              ))}
            </div>

            <Button
              size="sm"
              variant="accent"
              icon={<RefreshCw size={15} className={isScanning ? 'animate-spin' : ''} />}
              onClick={handleRunScan}
              disabled={isScanning}
            >
              {isScanning ? 'Auditing Regulations...' : 'Re-Run AI Audit'}
            </Button>
          </div>

          {/* Simulator Content Body */}
          <div className={styles.simulatorBody}>
            {/* Left: Property Meta & Verification Checklist */}
            <div className={styles.simPanel}>
              <div className={styles.propertyMetaCard}>
                <div className={styles.propertyMetaHeader}>
                  <div>
                    <h3 className={styles.propertyName}>{currentPreset.name}</h3>
                    <span className={styles.propertySub}>{currentPreset.location} • {currentPreset.type}</span>
                  </div>
                  <Badge variant={currentPreset.score >= 80 ? 'success' : currentPreset.score >= 60 ? 'warning' : 'danger'}>
                    {currentPreset.riskLevel}
                  </Badge>
                </div>

                <div className={styles.metaGrid}>
                  <div className={styles.metaItem}>
                    <span className={styles.metaKey}>Total Floors</span>
                    <span className={styles.metaVal}>{currentPreset.floors} Levels</span>
                  </div>
                  <div className={styles.metaItem}>
                    <span className={styles.metaKey}>Plot Footprint</span>
                    <span className={styles.metaVal}>{currentPreset.plotAreaSqFt.toLocaleString()} sq.ft</span>
                  </div>
                  <div className={styles.metaItem}>
                    <span className={styles.metaKey}>Fronting Road</span>
                    <span className={styles.metaVal}>{currentPreset.roadWidthM} Meters Wide</span>
                  </div>
                  <div className={styles.metaItem}>
                    <span className={styles.metaKey}>Digital Audit ID</span>
                    <span className={styles.metaVal} style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem' }}>PG-2026-X94</span>
                  </div>
                </div>
              </div>

              {/* Modules Toggles */}
              <div>
                <h4 style={{ fontSize: '0.875rem', fontWeight: 700, marginBottom: '0.75rem', color: '#E2E8F0', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Layers size={16} color="#38BDF8" />
                  Active AI Compliance Modules
                </h4>

                <div className={styles.modulesList}>
                  <div
                    className={`${styles.moduleItem} ${activeChecklist.zoning ? styles.moduleItemActive : ''}`}
                    onClick={() => setActiveChecklist({ ...activeChecklist, zoning: !activeChecklist.zoning })}
                  >
                    <div className={styles.moduleLeft}>
                      <div className={styles.moduleIconBox}><Building2 size={16} /></div>
                      <div>
                        <div className={styles.moduleTitle}>Municipal Zoning & FSI/FAR Limits</div>
                        <div className={styles.moduleDesc}>Master Plan 2031 & Permissible Density</div>
                      </div>
                    </div>
                    {activeChecklist.zoning ? <CheckCircle2 size={18} color="#10B981" /> : <div style={{ width: 18, height: 18, border: '1px solid var(--color-border)', borderRadius: '50%' }} />}
                  </div>

                  <div
                    className={`${styles.moduleItem} ${activeChecklist.title ? styles.moduleItemActive : ''}`}
                    onClick={() => setActiveChecklist({ ...activeChecklist, title: !activeChecklist.title })}
                  >
                    <div className={styles.moduleLeft}>
                      <div className={styles.moduleIconBox}><Scale size={16} /></div>
                      <div>
                        <div className={styles.moduleTitle}>RERA Title & Encumbrance Screening</div>
                        <div className={styles.moduleDesc}>30-year deed chain & litigation records</div>
                      </div>
                    </div>
                    {activeChecklist.title ? <CheckCircle2 size={18} color="#10B981" /> : <div style={{ width: 18, height: 18, border: '1px solid var(--color-border)', borderRadius: '50%' }} />}
                  </div>

                  <div
                    className={`${styles.moduleItem} ${activeChecklist.fire ? styles.moduleItemActive : ''}`}
                    onClick={() => setActiveChecklist({ ...activeChecklist, fire: !activeChecklist.fire })}
                  >
                    <div className={styles.moduleLeft}>
                      <div className={styles.moduleIconBox}><Flame size={16} /></div>
                      <div>
                        <div className={styles.moduleTitle}>Fire Dept NOC & Setback Calculations</div>
                        <div className={styles.moduleDesc}>NBC 2016 Part 4 high-rise clearances</div>
                      </div>
                    </div>
                    {activeChecklist.fire ? <CheckCircle2 size={18} color="#10B981" /> : <div style={{ width: 18, height: 18, border: '1px solid var(--color-border)', borderRadius: '50%' }} />}
                  </div>

                  <div
                    className={`${styles.moduleItem} ${activeChecklist.env ? styles.moduleItemActive : ''}`}
                    onClick={() => setActiveChecklist({ ...activeChecklist, env: !activeChecklist.env })}
                  >
                    <div className={styles.moduleLeft}>
                      <div className={styles.moduleIconBox}><Leaf size={16} /></div>
                      <div>
                        <div className={styles.moduleTitle}>Environmental & Wetland Buffer Screening</div>
                        <div className={styles.moduleDesc}>Pollution control board & green buffer</div>
                      </div>
                    </div>
                    {activeChecklist.env ? <CheckCircle2 size={18} color="#10B981" /> : <div style={{ width: 18, height: 18, border: '1px solid var(--color-border)', borderRadius: '50%' }} />}
                  </div>
                </div>
              </div>
            </div>

            {/* Right: Score Gauge & Finding Cards */}
            <div className={styles.resultPanel}>
              {isScanning && (
                <div className={styles.scanningBanner}>
                  <RefreshCw size={20} className="animate-spin" color="#38BDF8" />
                  <div style={{ width: '100%' }}>
                    <div className={styles.scanningText}>Analyzing 84 Deterministic Regulatory Rules...</div>
                    <div className={styles.progressBarContainer}>
                      <div className={styles.progressBarFill} style={{ width: `${scanProgress}%` }} />
                    </div>
                  </div>
                </div>
              )}

              {/* Radial Gauge */}
              <div className={styles.scoreHero}>
                <div className={styles.radialGauge}>
                  <svg className={styles.gaugeCircle} viewBox="0 0 100 100">
                    <circle className={styles.gaugeBg} cx="50" cy="50" r="42" />
                    <circle
                      className={styles.gaugeProgress}
                      cx="50"
                      cy="50"
                      r="42"
                      stroke={currentPreset.riskColor}
                      strokeDasharray="264"
                      strokeDashoffset={264 - (264 * (isScanning ? scanProgress : currentPreset.score)) / 100}
                    />
                  </svg>
                  <div className={styles.gaugeInner}>
                    <span className={styles.gaugeNum}>{isScanning ? scanProgress : currentPreset.score}</span>
                    <span className={styles.gaugeUnit}>INDEX / 100</span>
                  </div>
                </div>

                <div className={styles.scoreSummary}>
                  <div className={styles.verdictBadge} style={{ color: currentPreset.riskColor }}>
                    {currentPreset.score >= 80 ? (
                      <CheckCircle2 size={24} />
                    ) : currentPreset.score >= 60 ? (
                      <AlertTriangle size={24} />
                    ) : (
                      <XCircle size={24} />
                    )}
                    {currentPreset.riskLevel}
                  </div>
                  <p style={{ fontSize: '0.875rem', maxWidth: '280px' }}>
                    {currentPreset.score >= 80
                      ? 'Complies with all statutory municipal standards. Ready for development sanction & buyer financing.'
                      : currentPreset.score >= 60
                      ? 'Minor statutory deviations detected. Rectification recommended prior to project phase submission.'
                      : 'Critical compliance failures detected. Immediate regulatory remediation mandated.'}
                  </p>
                </div>
              </div>

              {/* Findings Feed */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
                  <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: '#E2E8F0', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <Search size={16} color="#38BDF8" />
                    Automated Finding Digest ({filteredFindings.length})
                  </h4>

                  {/* Filter tabs */}
                  <div style={{ display: 'flex', gap: '0.25rem' }}>
                    {(['all', 'critical', 'warning', 'pass'] as const).map((lvl) => (
                      <button
                        key={lvl}
                        type="button"
                        style={{
                          background: filterFinding === lvl ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
                          border: filterFinding === lvl ? '1px solid var(--color-accent)' : '1px solid transparent',
                          color: filterFinding === lvl ? '#FFFFFF' : 'var(--color-text-dim)',
                          padding: '0.2rem 0.5rem',
                          borderRadius: 'var(--radius-sm)',
                          fontSize: '0.75rem',
                          fontWeight: 600,
                          cursor: 'pointer',
                          textTransform: 'capitalize'
                        }}
                        onClick={() => setFilterFinding(lvl)}
                      >
                        {lvl}
                      </button>
                    ))}
                  </div>
                </div>

                <div className={styles.findingsContainer}>
                  {filteredFindings.map((finding) => (
                    <div key={finding.id} className={styles.findingCard}>
                      <div className={styles.findingTop}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                          <Badge
                            variant={
                              finding.severity === 'pass'
                                ? 'success'
                                : finding.severity === 'warning'
                                ? 'warning'
                                : 'danger'
                            }
                            size="sm"
                          >
                            {finding.severity.toUpperCase()}
                          </Badge>
                          <span className={styles.findingTitle}>{finding.title}</span>
                        </div>
                        <span style={{ fontSize: '0.75rem', color: 'var(--color-text-dim)', fontFamily: 'var(--font-mono)' }}>
                          {finding.rule}
                        </span>
                      </div>

                      <div className={styles.findingDetail}>{finding.description}</div>

                      <div className={styles.findingRemedy}>
                        <strong>Action:</strong> {finding.remediation}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Bylaw & Permissible FSI Calculator */}
      <section id="calculator" className={styles.section}>
        <div className={styles.sectionHeader}>
          <span className={styles.sectionPill}>Interactive Sandbox</span>
          <h2 className={styles.sectionTitle}>
            Instant <span className="gradient-text">Permissible FSI & Setback</span> Sandbox
          </h2>
          <p className={styles.sectionDescription}>
            Test different plot sizes, road widths, and zoning classifications to dynamically compute
            permissible floor space and mandatory fire setbacks based on municipal bylaws.
          </p>
        </div>

        <div className={styles.calcGrid}>
          {/* Inputs */}
          <div className={styles.calcInputs}>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#FFFFFF', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Sliders size={20} color="#38BDF8" />
              Property Parameters
            </h3>

            <div className={styles.sliderRow}>
              <div className={styles.sliderHeader}>
                <label htmlFor={plotAreaId}>Plot Area (Square Feet)</label>
                <span className={styles.sliderVal}>{calcPlotArea.toLocaleString()} sq.ft</span>
              </div>
              <input
                id={plotAreaId}
                type="range"
                min="5000"
                max="100000"
                step="2500"
                value={calcPlotArea}
                onChange={(e) => setCalcPlotArea(Number(e.target.value))}
                className={styles.rangeInput}
              />
            </div>

            <div className={styles.sliderRow}>
              <div className={styles.sliderHeader}>
                <label htmlFor={roadWidthId}>Fronting Road Width (Meters)</label>
                <span className={styles.sliderVal}>{calcRoadWidth} Meters</span>
              </div>
              <input
                id={roadWidthId}
                type="range"
                min="9"
                max="45"
                step="3"
                value={calcRoadWidth}
                onChange={(e) => setCalcRoadWidth(Number(e.target.value))}
                className={styles.rangeInput}
              />
            </div>

            <div>
              <label htmlFor={zoneTypeId} style={{ fontSize: '0.875rem', fontWeight: 600, color: '#E2E8F0', display: 'block', marginBottom: '0.5rem' }}>
                Zoning Category
              </label>
              <select
                id={zoneTypeId}
                value={calcZone}
                onChange={(e) => setCalcZone(e.target.value as any)}
                style={{
                  width: '100%',
                  padding: '0.75rem 1rem',
                  background: 'rgba(15, 23, 42, 0.9)',
                  border: '1px solid var(--color-border)',
                  borderRadius: 'var(--radius-lg)',
                  color: '#FFFFFF',
                  outline: 'none',
                  fontSize: '0.875rem'
                }}
              >
                <option value="commercial">Commercial / IT Corridor (High Density)</option>
                <option value="residential">Residential High-Density (R-2 Zone)</option>
                <option value="mixed">Mixed-Use Commercial & Residential</option>
              </select>
            </div>

            <div style={{ background: 'rgba(59, 130, 246, 0.08)', padding: '1rem', borderRadius: 'var(--radius-lg)', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <span style={{ fontSize: '0.8125rem', color: '#93C5FD', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Info size={16} />
                Calculated in real-time according to Unified Building Bye-laws (UBBL) & NBC 2016.
              </span>
            </div>
          </div>

          {/* Results */}
          <div className={styles.calcResults}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#FFFFFF' }}>
                Permissible Building Limits
              </h3>
              <Badge variant="cyan">Instant Calculation</Badge>
            </div>

            <div className={styles.resultMetricsGrid}>
              <div className={styles.calcMetricBox}>
                <span className={styles.calcMetricLabel}>Permissible FSI</span>
                <span className={styles.calcMetricVal} style={{ color: '#38BDF8' }}>{computedFsi.toFixed(2)}x</span>
              </div>

              <div className={styles.calcMetricBox}>
                <span className={styles.calcMetricLabel}>Max Permitted Built-up</span>
                <span className={styles.calcMetricVal}>{computedBuiltUp.toLocaleString()} sq.ft</span>
              </div>

              <div className={styles.calcMetricBox}>
                <span className={styles.calcMetricLabel}>Mandatory Front Setback</span>
                <span className={styles.calcMetricVal}>{frontSetback} m</span>
              </div>

              <div className={styles.calcMetricBox}>
                <span className={styles.calcMetricLabel}>Approx. Max Floors</span>
                <span className={styles.calcMetricVal}>{maxFloorsApprox} Storeys</span>
              </div>
            </div>

            <div style={{ background: 'rgba(0, 0, 0, 0.2)', padding: '1.25rem', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-border)' }}>
              <div style={{ fontSize: '0.875rem', fontWeight: 600, color: '#FFFFFF', marginBottom: '0.5rem' }}>
                Key Statutory Prerequisites:
              </div>
              <ul style={{ paddingLeft: '1.25rem', fontSize: '0.8125rem', color: 'var(--color-text-muted)', display: 'flex', flexDirection: 'column', gap: '0.35rem' }}>
                <li>Height exceeds 15m: <strong>Mandatory Chief Fire Officer (CFO) Provisional NOC</strong>.</li>
                <li>Built-up area exceeds 20,000 sq.m: <strong>State Environmental Impact Assessment (SEIAA) clearance</strong>.</li>
                <li>Road width of {calcRoadWidth}m supports high-capacity vehicular ingress & fire tender turning radius.</li>
              </ul>
            </div>

            <Link to="/register" style={{ width: '100%' }}>
              <Button fullWidth variant="glow" icon={<ArrowRight size={16} />} iconPosition="right">
                Run Comprehensive Audit on Your Land Parcel
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Capabilities / Feature Grid */}
      <section id="features" className={styles.section}>
        <div className={styles.sectionHeader}>
          <span className={styles.sectionPill}>Core Capabilities</span>
          <h2 className={styles.sectionTitle}>
            The Complete <span className="gradient-text">PropTech Risk Infrastructure</span>
          </h2>
          <p className={styles.sectionDescription}>
            Engineered from the ground up for real estate developers, institutional property funds,
            and homebuyer due diligence.
          </p>
        </div>

        <div className={styles.featuresGrid}>
          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><Cpu size={24} /></div>
            <h3 className={styles.featureTitle}>Multi-Tier Document OCR</h3>
            <p className={styles.featureDesc}>
              Automatically extracts and indexes surveyor seals, stamp dates, cadastral survey numbers, and municipal sanction numbers from complex legal blueprints and certificates.
            </p>
          </div>

          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><Building2 size={24} /></div>
            <h3 className={styles.featureTitle}>Deterministic Rule Engine</h3>
            <p className={styles.featureDesc}>
              Zero hallucination risk. Rules are defined in a verifiable schema, testing exact numeric parameters (FSI, setbacks, fire clearances) against codified municipal bylaws.
            </p>
          </div>

          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><Scale size={24} /></div>
            <h3 className={styles.featureTitle}>RERA Title & Litigations</h3>
            <p className={styles.featureDesc}>
              Cross-references 30-year ownership chains and court records to flag active revenue disputes, boundary conflicts, or unregistered mortgaged parcels.
            </p>
          </div>

          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><History size={24} /></div>
            <h3 className={styles.featureTitle}>Version-Controlled Audits</h3>
            <p className={styles.featureDesc}>
              Track building modifications across versions. Compare changes between blueprint v1 and sanction v2 with automated diff highlighting.
            </p>
          </div>

          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><Lock size={24} /></div>
            <h3 className={styles.featureTitle}>Tamper-Evident Storage</h3>
            <p className={styles.featureDesc}>
              High-security MinIO object storage with cryptographic hashes for every uploaded certificate, ensuring an immutable legal audit trail.
            </p>
          </div>

          <div className={styles.featureCard}>
            <div className={styles.featureIcon}><FileCheck size={24} /></div>
            <h3 className={styles.featureTitle}>Digital Compliance Passport</h3>
            <p className={styles.featureDesc}>
              Export audit-ready compliance certificates and buyer risk reports signed with verifiable QR verification codes for homebuyer trust.
            </p>
          </div>
        </div>
      </section>

      {/* Interactive FAQ Accordion */}
      <section id="faq" className={styles.section}>
        <div className={styles.sectionHeader}>
          <span className={styles.sectionPill}>Common Questions</span>
          <h2 className={styles.sectionTitle}>
            Frequently Asked <span className="gradient-text">Questions</span>
          </h2>
          <p className={styles.sectionDescription}>
            Everything you need to know about PropertyGuard AI and our regulatory compliance verification.
          </p>
        </div>

        <div className={styles.faqContainer}>
          {[
            {
              q: 'How does PropertyGuard AI evaluate compliance without LLM hallucinations?',
              a: 'PropertyGuard AI combines semantic document extraction with a strictly deterministic rule engine. While AI parses and extracts text from unstructured documents, all compliance checks (FSI limits, setbacks, road widths, fire NOC dates) are computed through mathematical rules against codified municipal bylaws.'
            },
            {
              q: 'Which municipal jurisdictions and building codes are supported?',
              a: 'We currently support National Building Code (NBC 2016), RERA statutory clauses across key states, and municipal building bye-laws for major metropolitan regions. Custom local zoning rules can be configured in our admin rule manager.'
            },
            {
              q: 'Can real estate builders manage multiple projects and version revisions?',
              a: 'Yes. The platform provides complete hierarchical project management (Projects → Buildings → Units → Documents). As architects revise blueprints or obtain new sanctions, versions are created with automatic differential risk re-evaluation.'
            },
            {
              q: 'Can homebuyers or legal auditors use PropertyGuard for due diligence?',
              a: 'Absolutely. PropertyGuard provides specialized persona dashboards for Homebuyers & Investors to verify RERA escrow accounts, title encumbrances, and occupancy certificates prior to entering sales agreements.'
            }
          ].map((item, idx) => (
            <div key={idx} className={styles.faqItem}>
              <button
                type="button"
                className={styles.faqQuestion}
                onClick={() => setOpenFaq(openFaq === idx ? null : idx)}
              >
                <span>{item.q}</span>
                <ChevronDown
                  size={18}
                  style={{
                    transform: openFaq === idx ? 'rotate(180deg)' : 'rotate(0deg)',
                    transition: 'transform 0.2s ease',
                    color: 'var(--color-accent)'
                  }}
                />
              </button>
              {openFaq === idx && (
                <div className={styles.faqAnswer}>
                  {item.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </section>

      {/* Bottom CTA Banner */}
      <section className={styles.ctaBanner}>
        <h2 className={styles.ctaTitle}>
          Ready to Automate Your Property Due Diligence?
        </h2>
        <p className={styles.ctaSubtitle}>
          Join leading real estate builders, financial institutions, and legal teams standardizing on PropertyGuard AI.
        </p>
        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          <Link to="/register">
            <Button size="lg" variant="glow" icon={<ArrowRight size={18} />} iconPosition="right">
              Get Started for Free
            </Button>
          </Link>
          <Link to="/login">
            <Button size="lg" variant="outline">
              Sign In to Dashboard
            </Button>
          </Link>
        </div>
      </section>

      {/* Modern Footer */}
      <footer className={styles.footer}>
        <div className={styles.footerInner}>
          <div className={styles.footerTop}>
            <div className={styles.footerBrand}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                <ShieldCheck size={24} color="#38BDF8" />
                <span style={{ fontSize: '1.2rem', fontWeight: 800, color: '#FFFFFF' }}>PropertyGuard AI</span>
              </div>
              <p style={{ fontSize: '0.875rem', maxWidth: '350px' }}>
                Intelligent property compliance, deterministic risk assessment, and document verification for the modern built environment.
              </p>
            </div>

            <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
              <button type="button" onClick={() => scrollToSection('scanner')} style={{ background: 'none', border: 'none', color: 'var(--color-text-muted)', cursor: 'pointer' }}>
                Live Scanner
              </button>
              <button type="button" onClick={() => scrollToSection('calculator')} style={{ background: 'none', border: 'none', color: 'var(--color-text-muted)', cursor: 'pointer' }}>
                Bylaw Sandbox
              </button>
              <button type="button" onClick={() => scrollToSection('features')} style={{ background: 'none', border: 'none', color: 'var(--color-text-muted)', cursor: 'pointer' }}>
                Capabilities
              </button>
              <Link to="/login" style={{ color: 'var(--color-accent-light)' }}>
                Client Portal
              </Link>
            </div>
          </div>

          <div className={styles.footerBottom}>
            <span>&copy; {new Date().getFullYear()} PropertyGuard AI Technologies Inc. All rights reserved.</span>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span className="badge-live-pulse" />
              <span>All AI & Rule Engine Pipelines Operational</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
