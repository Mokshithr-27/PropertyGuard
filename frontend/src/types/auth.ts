export interface User {
  id: string;
  email: string;
  full_name: string;
  phone: string | null;
  is_active: boolean;
  is_email_verified: boolean;
  role?: 'builder' | 'buyer' | 'admin';
  roles?: string[];
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}
