/**
 * PropertyGuard Input UI Component
 * Accessible form text input component with support for labels, error messages,
 * helper hints, leading icons, and right-side elements.
 */

import { forwardRef, type InputHTMLAttributes, type ReactNode } from 'react';
import clsx from 'clsx';
import styles from './Input.module.css';

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  hint?: string;
  icon?: ReactNode;
  rightElement?: ReactNode;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, hint, icon, rightElement, className, id, ...props }, ref) => {
    return (
      <div className={clsx(styles.wrapper, className)}>
        {label && (
          <label htmlFor={id} className={styles.label}>
            {label}
          </label>
        )}
        <div className={styles.inputContainer}>
          {icon && <div className={styles.leftIcon}>{icon}</div>}
          <input
            ref={ref}
            id={id}
            className={clsx(
              styles.input,
              icon && styles.hasLeftIcon,
              rightElement && styles.hasRightElement,
              error && styles.inputError
            )}
            {...props}
          />
          {rightElement && <div className={styles.rightElement}>{rightElement}</div>}
        </div>
        {error && <span className={styles.errorText}>{error}</span>}
        {hint && !error && <span className={styles.hintText}>{hint}</span>}
      </div>
    );
  }
);
Input.displayName = 'Input';
