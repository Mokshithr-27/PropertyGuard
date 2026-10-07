import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Shield, Eye, EyeOff, Building2, UserCheck, Briefcase, ArrowRight, Lock, Mail } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { apiClient } from '../../api/client';
import { Button } from '../../components/common/Button';
import { Input } from '../../components/common/Input';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '../../components/common/Card';

export function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const { login, loginDemo } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      const response = await apiClient.post('/api/v1/auth/login', { email, password });
      await login(response.data.access_token);
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed. Please verify credentials or use Quick Demo Login below.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDemoLogin = async (role: 'builder' | 'buyer' | 'admin') => {
    setError('');
    setIsLoading(true);
    try {
      await loginDemo(role);
      navigate('/dashboard');
    } catch (err: any) {
      console.error('Demo login error:', err);
      navigate('/dashboard');
    } finally {
      setIsLoading(false);
    }
  };


  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '1.5rem',
        position: 'relative',
        background: 'var(--color-bg)'
      }}
    >
      {/* Background ambient glow */}
      <div
        style={{
          position: 'absolute',
          top: '20%',
          width: '500px',
          height: '350px',
          background: 'radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(6, 182, 212, 0.05) 60%, transparent 80%)',
          filter: 'blur(50px)',
          pointerEvents: 'none'
        }}
      />

      {/* Brand Header */}
      <Link to="/" style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '2rem', textDecoration: 'none' }}>
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
          maxWidth: '460px',
          border: '1px solid rgba(59, 130, 246, 0.25)',
          boxShadow: '0 20px 50px -10px rgba(0, 0, 0, 0.7)'
        }}
      >
        <CardHeader style={{ textAlign: 'center', borderBottom: 'none', paddingBottom: '0.5rem' }}>
          <CardTitle style={{ fontSize: '1.4rem' }}>Welcome Back</CardTitle>
          <CardDescription>
            Sign in to access your property compliance portal
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <Input
              label="Email Address"
              type="email"
              placeholder="name@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              icon={<Mail size={16} />}
              required
            />

            <Input
              label="Password"
              type={showPassword ? 'text' : 'password'}
              placeholder="••••••••"
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
            />

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

            <Button type="submit" fullWidth variant="glow" size="lg" isLoading={isLoading} icon={<ArrowRight size={16} />} iconPosition="right">
              Sign In
            </Button>
          </form>

          {/* Quick Demo Login Option */}
          <div style={{ marginTop: '2rem', borderTop: '1px solid var(--color-border)', paddingTop: '1.5rem' }}>
            <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 700, color: 'var(--color-text-dim)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '1rem' }}>
              ⚡ Instant 1-Click Demo Login
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.5rem' }}>
              <Button
                variant="outline"
                size="sm"
                onClick={() => handleDemoLogin('builder')}
                icon={<Building2 size={13} />}
              >
                Builder
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => handleDemoLogin('buyer')}
                icon={<UserCheck size={13} />}
              >
                Buyer
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => handleDemoLogin('admin')}
                icon={<Briefcase size={13} />}
              >
                Auditor
              </Button>
            </div>
          </div>

          <div style={{ textAlign: 'center', fontSize: '0.875rem', marginTop: '1.75rem', color: 'var(--color-text-dim)' }}>
            Don't have an account?{' '}
            <Link to="/register" style={{ color: 'var(--color-accent-light)', fontWeight: 600 }}>
              Create an account
            </Link>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
