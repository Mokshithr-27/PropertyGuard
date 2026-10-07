import type { ReactNode, CSSProperties } from 'react';
import clsx from 'clsx';
import styles from './Card.module.css';

interface CardProps {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
  variant?: 'default' | 'glass' | 'interactive' | 'glow' | 'subtle';
  onClick?: () => void;
}

export function Card({ children, className, style, variant = 'glass', onClick }: CardProps) {
  return (
    <div
      className={clsx(styles.card, styles[variant], onClick && styles.clickable, className)}
      style={style}
      onClick={onClick}
    >
      {children}
    </div>
  );
}

export function CardHeader({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <div className={clsx(styles.header, className)} style={style}>
      {children}
    </div>
  );
}

export function CardTitle({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <h3 className={clsx(styles.title, className)} style={style}>
      {children}
    </h3>
  );
}

export function CardDescription({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <p className={clsx(styles.description, className)} style={style}>
      {children}
    </p>
  );
}

export function CardContent({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <div className={clsx(styles.content, className)} style={style}>
      {children}
    </div>
  );
}

export function CardFooter({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <div className={clsx(styles.footer, className)} style={style}>
      {children}
    </div>
  );
}
