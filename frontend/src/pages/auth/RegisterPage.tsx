import { useState, useId } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Shield, Eye, EyeOff, Building2, UserCheck, Briefcase, Mail, Lock, User as UserIcon, Phone, ArrowRight } from 'lucide-react';
import { apiClient } from '../../api/client';
import { useAuth } from '../../context/AuthContext';
import { Button } from '../../components/common/Button';
import { Input } from '../../components/common/Input';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '../../components/common/Card';

export function RegisterPage() {
  const termsCheckboxId = useId();

  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [phone, setPhone] = useState('');
  const [role, setRole] = useState<'buyer' | 'builder' | 'admin'>('builder');
  const [terms, setTerms] = useState(false);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const { loginDemo } = useAuth();

  const getPasswordStrength = () => {
    if (password.length === 0) return { score: 0, label: '', color: 'transparent' };
    if (password.length < 6) return { score: 1, label: 'Too short', color: 'var(--color-danger)' };
    if (password.length < 9) return { score: 2, label: 'Moderate', color: 'var(--color-warning)' };
    return { score: 3, label: 'Strong & Secure', color: 'var(--color-success)' };
  };

  const strength = getPasswordStrength();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    if (!terms) {
      setError('You must accept the terms of service to create an account');
      return;
    }

    setIsLoading(true);

    try {
      await apiClient.post('/api/v1/auth/register', {
        email,
        password,
        full_name: fullName,
        phone: phone || null,
      });
      navigate('/login');
    } catch (err: any) {
      const msg = err.response?.data?.detail || 'Registration failed. If offline, use Quick Demo Login below.';
      setError(typeof msg === 'string' ? msg : JSON.stringify(msg));
    } finally {
      setIsLoading(false);
    }
  };

  const handleDemoLogin = (r: 'builder' | 'buyer' | 'admin') => {
    loginDemo(r);
    navigate('/dashboard');
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem 1.5rem',
        background: 'var(--color-bg)',
        position: 'relative'
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: '15%',
          width: '550px',
          height: '400px',
          background: 'radial-gradient(circle, rgba(6, 182, 212, 0.12) 0%, rgba(59, 130, 246, 0.06) 50%, transparent 80%)',
          filter: 'blur(60px)',
          pointerEvents: 'none'
        }}
      />

      <Link to="/" style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem', textDecoration: 'none' }}>
        <div
          style={{
            width: '42px',
            height: '42px',
            borderRadius: 'var(--radius-lg)',
            background: 'linear-gradient(135deg, #1E293B, #0F172A)',
            border: '1px solid rgba(59, 130, 246, 0.4)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#38BDF8',
            boxShadow: '0 0 15px rgba(59, 130, 246, 0.25)'
          }}
        >
          <Shield size={24} />
        </div>
        <span style={{ fontSize: '1.4rem', fontWeight: 800, color: '#FFFFFF' }}>PropertyGuard AI</span>
      </Link>

      <Card
        variant="glass"
        style={{
          width: '100%',
          maxWidth: '520px',
          border: '1px solid rgba(59, 130, 246, 0.25)',
          boxShadow: '0 25px 60px -15px rgba(0, 0, 0, 0.8)'
        }}
      >
        <CardHeader style={{ textAlign: 'center', borderBottom: 'none', paddingBottom: '0.25rem' }}>
          <CardTitle style={{ fontSize: '1.4rem' }}>Create Your Account</CardTitle>
          <CardDescription>
            Join institutional builders and investors ensuring verified property compliance
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.15rem' }}>
            {/* Role Cards Selector */}
            <div>
              <span style={{ fontSize: '0.8125rem', fontWeight: 600, color: '#E2E8F0', display: 'block', marginBottom: '0.5rem' }}>
                Select Your Primary Organization Role
              </span>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.5rem' }}>
                <button
                  type="button"
                  onClick={() => setRole('builder')}
                  style={{
                    background: role === 'builder' ? 'rgba(59, 130, 246, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                    border: role === 'builder' ? '1px solid var(--color-accent)' : '1px solid var(--color-border)',
                    borderRadius: 'var(--radius-lg)',
                    padding: '0.65rem 0.5rem',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '0.25rem',
                    cursor: 'pointer',
                    color: role === 'builder' ? '#FFFFFF' : 'var(--color-text-muted)'
                  }}
                >
                  <Building2 size={18} color={role === 'builder' ? '#38BDF8' : 'currentColor'} />
                  <span style={{ fontSize: '0.75rem', fontWeight: 600 }}>Builder</span>
                </button>

                <button
                  type="button"
                  onClick={() => setRole('buyer')}
                  style={{
                    background: role === 'buyer' ? 'rgba(59, 130, 246, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                    border: role === 'buyer' ? '1px solid var(--color-accent)' : '1px solid var(--color-border)',
                    borderRadius: 'var(--radius-lg)',
                    padding: '0.65rem 0.5rem',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '0.25rem',
                    cursor: 'pointer',
                    color: role === 'buyer' ? '#FFFFFF' : 'var(--color-text-muted)'
                  }}
                >
                  <UserCheck size={18} color={role === 'buyer' ? '#38BDF8' : 'currentColor'} />
                  <span style={{ fontSize: '0.75rem', fontWeight: 600 }}>Buyer</span>
                </button>

                <button
                  type="button"
                  onClick={() => setRole('admin')}
                  style={{
                    background: role === 'admin' ? 'rgba(59, 130, 246, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                    border: role === 'admin' ? '1px solid var(--color-accent)' : '1px solid var(--color-border)',
                    borderRadius: 'var(--radius-lg)',
                    padding: '0.65rem 0.5rem',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '0.25rem',
                    cursor: 'pointer',
                    color: role === 'admin' ? '#FFFFFF' : 'var(--color-text-muted)'
                  }}
                >
                  <Briefcase size={18} color={role === 'admin' ? '#38BDF8' : 'currentColor'} />
                  <span style={{ fontSize: '0.75rem', fontWeight: 600 }}>Auditor</span>
                </button>
              </div>
            </div>

            <Input
              label="Full Name or Entity"
              placeholder="e.g. Rohith Sharma / Apex Builders"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              icon={<UserIcon size={16} />}
              required
            />

            <Input
              label="Work Email Address"
              type="email"
              placeholder="name@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              icon={<Mail size={16} />}
              required
            />

            <Input
              label="Phone Number (Optional)"
              type="tel"
              placeholder="+91 98765 43210"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              icon={<Phone size={16} />}
            />

            <div>
              <Input
                label="Create Password"
                type={showPassword ? 'text' : 'password'}
                placeholder="At least 8 characters"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                icon={<Lock size={16} />}
                rightElement={
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    style={{ background: 'none', border: 'none', color: 'var(--color-text-dim)', cursor: 'pointer', padding: '0.25rem' }}
                  >
                    {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                  </button>
                }
                required
                minLength={8}
              />
              {password && (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: '0.35rem' }}>
                  <div style={{ display: 'flex', gap: '4px', width: '120px' }}>
                    {[1, 2, 3].map((step) => (
                      <div
                        key={step}
                        style={{
                          height: '4px',
                          flex: 1,
                          borderRadius: '2px',
                          backgroundColor: step <= strength.score ? strength.color : 'rgba(255,255,255,0.1)'
                        }}
                      />
                    ))}
                  </div>
                  <span style={{ fontSize: '0.75rem', color: strength.color, fontWeight: 600 }}>
                    {strength.label}
                  </span>
                </div>
              )}
            </div>

            <Input
              label="Confirm Password"
              type="password"
              placeholder="Re-enter password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              icon={<Lock size={16} />}
              required
            />

            <label
              htmlFor={termsCheckboxId}
              style={{ display: 'flex', alignItems: 'flex-start', gap: '0.65rem', fontSize: '0.8125rem', color: 'var(--color-text-muted)', cursor: 'pointer' }}
            >
              <input
                id={termsCheckboxId}
                type="checkbox"
                checked={terms}
                onChange={(e) => setTerms(e.target.checked)}
                style={{ marginTop: '0.2rem', accentColor: 'var(--color-accent)' }}
              />
              <span>
                I agree to the <a href="#terms" style={{ color: 'var(--color-accent-light)' }}>Terms of Service</a>, RERA disclosure guidelines, and privacy policy.
              </span>
            </label>

            {error && (
              <div
                style={{
                  background: 'var(--color-danger-bg)',
                  border: '1px solid var(--color-danger-border)',
                  color: 'var(--color-danger)',
                  padding: '0.75rem',
                  borderRadius: 'var(--radius-md)',
                  fontSize: '0.8125rem'
                }}
              >
                {error}
              </div>
            )}

            <Button
              type="submit"
              fullWidth
              variant="glow"
              size="lg"
              isLoading={isLoading}
              icon={<ArrowRight size={16} />}
              iconPosition="right"
            >
              Complete Registration
            </Button>
          </form>

          {/* Quick Demo Option */}
          <div style={{ marginTop: '1.5rem', borderTop: '1px solid var(--color-border)', paddingTop: '1.25rem', textAlign: 'center' }}>
            <span style={{ fontSize: '0.75rem', color: 'var(--color-text-dim)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.04em' }}>
              Want to skip signup and explore instantly?
            </span>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem', marginTop: '0.75rem' }}>
              <Button size="xs" variant="outline" onClick={() => handleDemoLogin('builder')}>
                Demo Builder
              </Button>
              <Button size="xs" variant="outline" onClick={() => handleDemoLogin('buyer')}>
                Demo Buyer
              </Button>
              <Button size="xs" variant="outline" onClick={() => handleDemoLogin('admin')}>
                Demo Auditor
              </Button>
            </div>
          </div>

          <div style={{ textAlign: 'center', fontSize: '0.875rem', marginTop: '1.5rem', color: 'var(--color-text-dim)' }}>
            Already have an account?{' '}
            <Link to="/login" style={{ color: 'var(--color-accent-light)', fontWeight: 600 }}>
              Sign in
            </Link>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
