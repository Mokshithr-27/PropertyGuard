/**
 * PropertyGuard Badge UI Component
 * Renders status indicators and tags with configurable variants (success, warning, danger, info, etc.) and dot indicators.
 */

import type { ReactNode } from 'react';
import clsx from 'clsx';
import styles from './Badge.module.css';

interface BadgeProps {
  children: ReactNode;
  variant?: 'success' | 'warning' | 'danger' | 'info' | 'cyan' | 'purple' | 'default';
  size?: 'sm' | 'md' | 'lg';
  dot?: boolean;
  className?: string;
}

export function Badge({
  children,
  variant = 'default',
  size = 'md',
  dot = false,
  className,
}: BadgeProps) {
  return (
    <span className={clsx(styles.badge, styles[variant], styles[size], className)}>
      {dot && <span className={clsx(styles.dot, styles[`dot_${variant}`])} />}
      {children}
    </span>
  );
}
