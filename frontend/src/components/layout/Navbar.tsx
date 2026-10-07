import { Link, useNavigate } from 'react-router-dom';
import { Shield, Sparkles, LogOut, LayoutDashboard, UserCheck } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { Button } from '../common/Button';
import { Badge } from '../common/Badge';
import styles from './Navbar.module.css';

interface NavbarProps {
  activeTab?: string;
  onNavigateSection?: (sectionId: string) => void;
}

export function Navbar({ onNavigateSection }: NavbarProps) {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleScrollOrNav = (sectionId: string) => {
    if (onNavigateSection) {
      onNavigateSection(sectionId);
    } else {
      navigate(`/#${sectionId}`);
    }
  };

  return (
    <header className={styles.navbar}>
      <div className={styles.inner}>
        {/* Brand */}
        <Link to="/" className={styles.brand}>
          <div className={styles.logoBadge}>
            <Shield className={styles.logoIcon} size={22} />
            <Sparkles className={styles.sparkleIcon} size={11} />
          </div>
          <div className={styles.brandText}>
            <span className={styles.brandMain}>PropertyGuard</span>
            <span className={styles.brandTag}>AI</span>
          </div>
        </Link>

        {/* Status Pill */}
        <div className={styles.statusContainer}>
          <span className="badge-live-pulse" />
          <span className={styles.statusText}>AI Rule Engine v2.4 Active</span>
        </div>

        {/* Center Nav Links */}
        <nav className={styles.navLinks}>
          <button
            type="button"
            className={styles.navLink}
            onClick={() => handleScrollOrNav('scanner')}
          >
            Live Risk Scanner
          </button>
          <button
            type="button"
            className={styles.navLink}
            onClick={() => handleScrollOrNav('features')}
          >
            Compliance Capabilities
          </button>
          <button
            type="button"
            className={styles.navLink}
            onClick={() => handleScrollOrNav('calculator')}
          >
            Bylaw Sandbox
          </button>
          <button
            type="button"
            className={styles.navLink}
            onClick={() => handleScrollOrNav('faq')}
          >
            FAQ
          </button>
        </nav>

        {/* Actions */}
        <div className={styles.actions}>
          {user ? (
            <div className={styles.userSection}>
              <div className={styles.userInfo}>
                <div className={styles.userAvatar}>
                  <UserCheck size={16} />
                </div>
                <div className={styles.userDetails}>
                  <span className={styles.userName}>{user.full_name || user.email.split('@')[0]}</span>
                  <Badge variant={user.role === 'builder' ? 'cyan' : user.role === 'admin' ? 'purple' : 'info'} size="sm">
                    {user.role}
                  </Badge>
                </div>
              </div>

              <Link to="/dashboard">
                <Button size="sm" variant="glow" icon={<LayoutDashboard size={15} />}>
                  Dashboard
                </Button>
              </Link>
              <Button
                size="sm"
                variant="ghost"
                onClick={logout}
                title="Sign out"
                icon={<LogOut size={15} />}
              >
                Logout
              </Button>
            </div>
          ) : (
            <div className={styles.authButtons}>
              <Link to="/login">
                <Button size="sm" variant="ghost">
                  Sign In
                </Button>
              </Link>
              <Link to="/register">
                <Button size="sm" variant="primary">
                  Get Started
                </Button>
              </Link>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
