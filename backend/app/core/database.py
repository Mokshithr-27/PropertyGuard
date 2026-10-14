"""
PropertyGuard Database Session & ORM Base Setup
------------------------------------------------
Initializes the SQLAlchemy engine with connection pool pinging, configures the
SessionLocal factory for database transactions, and defines the DeclarativeBase.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass