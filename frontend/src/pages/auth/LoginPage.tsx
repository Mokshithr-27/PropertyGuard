/**
 * PropertyGuard Login Page Component
 * Provides user login credentials input, authenticates via POST /api/v1/auth/login,
 * stores the JWT token, and redirects to the dashboard.
 */

import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ArrowRight, Lock, Mail, ShieldCheck } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { apiClient } from '../../api/client';
import { Button } from '../../components/common/Button';
import { Input } from '../../components/common/Input';

export function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const submit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true); setError('');
    try {
      const response = await apiClient.post('/api/v1/auth/login', { email, password });
      await login(response.data.access_token);
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed. Check your email and password.');
    } finally { setLoading(false); }
  };

  return <div style={pageStyle}><div style={authCardStyle}><div style={brandStyle}><span style={logoStyle}><ShieldCheck size={22} /></span><div><strong>PropertyGuard</strong><small>Secure property compliance</small></div></div><h1>Sign in</h1><p style={subtitleStyle}>Use your registered PropertyGuard account.</p>{error && <div style={errorStyle}>{error}</div>}<form onSubmit={submit} style={{display:'flex',flexDirection:'column',gap:'1rem'}}><Input label="Email" type="email" value={email} onChange={(e)=>setEmail(e.target.value)} icon={<Mail size={16}/>} required/><Input label="Password" type="password" value={password} onChange={(e)=>setPassword(e.target.value)} icon={<Lock size={16}/>} required/><Button type="submit" fullWidth size="lg" isLoading={loading} icon={<ArrowRight size={16}/>}>Sign in</Button></form><p style={footerStyle}>New to PropertyGuard? <Link to="/register">Create an account</Link></p></div></div>;
}

const pageStyle: React.CSSProperties = { minHeight:'100vh', display:'grid', placeItems:'center', padding:'1.5rem', background:'#f6f8fb' };
const authCardStyle: React.CSSProperties = { width:'min(440px,100%)', padding:'2rem', background:'#fff', border:'1px solid #e1e6ee', borderRadius:'16px', boxShadow:'0 18px 45px rgba(16,24,40,.1)' };
const brandStyle: React.CSSProperties = { display:'flex', alignItems:'center', gap:'.7rem', marginBottom:'1.8rem' };
const logoStyle: React.CSSProperties = { width:40,height:40,display:'grid',placeItems:'center',borderRadius:10,background:'#eef4ff',color:'#2563eb' };
const subtitleStyle: React.CSSProperties = { margin:'.35rem 0 1.4rem',fontSize:'.88rem' };
const errorStyle: React.CSSProperties = { padding:'.75rem',marginBottom:'1rem',background:'#fff1f2',border:'1px solid #fecaca',borderRadius:8,color:'#991b1b',fontSize:'.82rem' };
const footerStyle: React.CSSProperties = { marginTop:'1.3rem',textAlign:'center',fontSize:'.82rem' };
