"""
PropertyGuard Database Health Diagnostic Check
------------------------------------------------
Provides a quick connectivity test function executing 'SELECT 1' against the
configured PostgreSQL database engine.
"""

from sqlalchemy import text

from app.core.database import engine


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()