"""
PropertyGuard Password Security & Hashing
-----------------------------------------
Provides password hashing and verification using secure modern password hashing
schemes (pwdlib Argon2 / Bcrypt algorithms).
"""

from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)