"""
PropertyGuard Storage Initialization Service
--------------------------------------------
Provides high-level helpers to initialize application storage buckets and directories.
"""

from app.integrations.storage import ensure_bucket


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def initialize_storage() -> None:
    """Initialize required object storage resources."""
    ensure_bucket()