import { createContext, useContext, useState, useEffect, type ReactNode } from 'react';
import type { User } from '../types/auth';
import { apiClient } from '../api/client';

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  login: (token: string) => Promise<void>;
  loginDemo: (role?: 'builder' | 'buyer' | 'admin') => Promise<void>;
  logout: () => void;

}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const fetchUser = async () => {
    try {
      const response = await apiClient.get<User>('/api/v1/auth/me');
      let role: 'builder' | 'buyer' | 'admin' = 'buyer';
      const email = response.data.email.toLowerCase();
      const roles = response.data.roles || [];

      if (roles.includes('ADMIN') || roles.includes('SUPER_ADMIN') || email.includes('admin')) {
        role = 'admin';
      } else if (roles.includes('BUILDER') || email.includes('builder')) {
        role = 'builder';
      }

      setUser({ ...response.data, role });
    } catch (error) {
      // Check if demo user exists in storage
      const demoUser = localStorage.getItem('demo_user');
      if (demoUser) {
        setUser(JSON.parse(demoUser));
      } else {
        setUser(null);
        localStorage.removeItem('access_token');
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      fetchUser();
      return;
    }

    const demoUser = localStorage.getItem('demo_user');
    if (demoUser) {
      try {
        setUser(JSON.parse(demoUser));
      } catch {
        localStorage.removeItem('demo_user');
      }
      setIsLoading(false);
      return;
    }

    setIsLoading(false);
  }, []);


  const login = async (token: string) => {
    localStorage.removeItem('demo_user');
    localStorage.setItem('access_token', token);
    await fetchUser();
  };

  const loginDemo = async (role: 'builder' | 'buyer' | 'admin' = 'builder') => {
    const creds = {
      builder: {
        email: 'builder@propertyguard.ai',
        password: 'PropertyGuard2026!',
        name: 'Apex Infra Developers'
      },
      buyer: {
        email: 'buyer@propertyguard.ai',
        password: 'PropertyGuard2026!',
        name: 'Rohith Urban Investor'
      },
      admin: {
        email: 'admin@propertyguard.ai',
        password: 'PropertyGuard2026!',
        name: 'State Regulatory Officer'
      }
    };

    const target = creds[role];
    const demoData: User = {
      id: `usr-demo-${role}`,
      email: target.email,
      full_name: target.name,
      phone: '+91 98765 43210',
      is_active: true,
      is_email_verified: true,
      role
    };

    localStorage.setItem('demo_user', JSON.stringify(demoData));
    localStorage.setItem('active_persona', role === 'admin' ? 'auditor' : role);
    setUser(demoData);

    try {
      const res = await apiClient.post('/api/v1/auth/login', {
        email: target.email,
        password: target.password
      });
      if (res.data?.access_token) {
        localStorage.setItem('access_token', res.data.access_token);
        await fetchUser();
      }
    } catch (err) {
      console.warn(`Backend login token note for ${role}:`, err);
    }
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('demo_user');
    localStorage.removeItem('active_persona');
    setUser(null);
    window.location.href = '/login';
  };


  return (
    <AuthContext.Provider value={{ user, isLoading, login, loginDemo, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
