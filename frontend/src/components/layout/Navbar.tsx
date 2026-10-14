/**
 * PropertyGuard Top Navigation Bar Component
 * Displays brand logo, active user session details with role badges,
 * and navigation links for Dashboard, Sign In, Register, or Sign Out.
 */

import { Link, useNavigate } from 'react-router-dom';
import { LayoutDashboard, LogOut, ShieldCheck, UserRound } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { Button } from '../common/Button';
import { Badge } from '../common/Badge';
import styles from './Navbar.module.css';

export function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const roles = (user?.roles || []).map((role) => String(role).toUpperCase());
  const label = roles.includes('ADMIN') || roles.includes('SUPER_ADMIN') ? 'Admin' : roles.includes('BUILDER') ? 'Builder' : 'Buyer';
  const variant = label === 'Admin' ? 'purple' : label === 'Builder' ? 'cyan' : 'info';

  return (
    <header className={styles.navbar}>
      <div className={styles.inner}>
        <Link to="/" className={styles.brand}><span className={styles.logoBadge}><ShieldCheck size={20} /></span><span><strong>PropertyGuard</strong><small>Property compliance platform</small></span></Link>
        <div className={styles.actions}>
          {user ? <><div className={styles.userInfo}><span className={styles.avatar}><UserRound size={15} /></span><span className={styles.userDetails}><strong>{user.full_name || user.email}</strong><Badge variant={variant} size="sm">{label}</Badge></span></div><Button size="sm" variant="outline" icon={<LayoutDashboard size={15} />} onClick={() => navigate('/dashboard')}>Dashboard</Button><Button size="sm" variant="ghost" icon={<LogOut size={15} />} onClick={logout}>Sign out</Button></> : <><Link to="/login"><Button size="sm" variant="outline">Sign in</Button></Link><Link to="/register"><Button size="sm">Create account</Button></Link></>}
        </div>
      </div>
    </header>
  );
}
