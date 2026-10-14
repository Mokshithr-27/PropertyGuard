"""
PropertyGuard Password Security & Hashing
-----------------------------------------
Provides password hashing and verification using secure modern password hashing
schemes (pwdlib Argon2 / Bcrypt algorithms).
"""

from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_hash_password__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_hash_password__mutmut)
def hash_password(password: str) -> str:
    return password_hash.hash(password)


def x_hash_password__mutmut_orig(password: str) -> str:
    return password_hash.hash(password)


def x_hash_password__mutmut_1(password: str) -> str:
    return password_hash.hash(None)

mutants_x_hash_password__mutmut['_mutmut_orig'] = x_hash_password__mutmut_orig # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_1'] = x_hash_password__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_verify_password__mutmut)
def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def x_verify_password__mutmut_orig(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def x_verify_password__mutmut_1(password: str, hashed_password: str) -> bool:
    return password_hash.verify(None, hashed_password)


def x_verify_password__mutmut_2(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, None)


def x_verify_password__mutmut_3(password: str, hashed_password: str) -> bool:
    return password_hash.verify(hashed_password)


def x_verify_password__mutmut_4(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, )

mutants_x_verify_password__mutmut['_mutmut_orig'] = x_verify_password__mutmut_orig # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_1'] = x_verify_password__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_2'] = x_verify_password__mutmut_2 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_3'] = x_verify_password__mutmut_3 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_4'] = x_verify_password__mutmut_4 # type: ignore # mutmut generated