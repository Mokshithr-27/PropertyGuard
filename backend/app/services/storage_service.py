"""
PropertyGuard Storage Initialization Service
--------------------------------------------
Provides high-level helpers to initialize application storage buckets and directories.
"""

from app.integrations.storage import ensure_bucket


def initialize_storage() -> None:
    """Initialize required object storage resources."""
    ensure_bucket()