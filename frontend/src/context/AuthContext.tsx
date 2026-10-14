/**
 * PropertyGuard Authentication Context & Session Provider
 * Manages user state, login tokens in localStorage, session validation (/auth/me),
 * role normalization, and logout cleanup across the application tree.
 */

import { createContext, useContext, useState, useEffect, type ReactNode } from 'react';
import type { User } from '../types/auth';
import { apiClient } from '../api/client';

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  login: (token: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

function normalizeUser(data: User): User {
  const roles = data.roles || [];
  const normalizedRoles = roles.map((role) => String(role).toUpperCase());
  let role: User['role'] = 'buyer';
  if (normalizedRoles.includes('ADMIN') || normalizedRoles.includes('SUPER_ADMIN')) role = 'admin';
  else if (normalizedRoles.includes('BUILDER')) role = 'builder';
  return { ...data, role, roles: normalizedRoles };
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const fetchUser = async () => {
    try {
      const response = await apiClient.get<User>('/api/v1/auth/me');
      setUser(normalizeUser(response.data));
    } catch {
      setUser(null);
      localStorage.removeItem('access_token');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (localStorage.getItem('access_token')) void fetchUser();
    else setIsLoading(false);
  }, []);

  const login = async (token: string) => {
    localStorage.setItem('access_token', token);
    await fetchUser();
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setUser(null);
    window.location.href = '/login';
  };

  return <AuthContext.Provider value={{ user, isLoading, login, logout }}>{children}</AuthContext.Provider>;
}

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};
