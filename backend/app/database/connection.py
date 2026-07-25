"""Database Connection and Configuration"""

from sqlalchemy import create_engine, event
from sqlalchemy.exc import StatementError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

from app.config import settings

# Create engine with connection pooling
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    poolclass=QueuePool,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=3600,   # Recycle connections after 1 hour
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Declarative base for models
Base = declarative_base()


def get_db():
    """Dependency injection for database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Event listeners
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Set SQLite pragmas if using SQLite"""
    if "sqlite" in settings.DATABASE_URL:
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
