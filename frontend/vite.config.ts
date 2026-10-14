/**
 * PropertyGuard Frontend - Vite Build Configuration
 * Configures the Vite development server and React plugin with Fast Refresh.
 */

import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
