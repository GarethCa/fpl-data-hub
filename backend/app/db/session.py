from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use env var if set, else fallback local dev URL
# Format: postgresql+psycopg2://user:password@host:port/dbname
DATABASE_URL = getenv(
    "DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/fpl"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Import models and create tables if they do not exist.
    Intended for early development only; replace with Alembic migrations later.
    """
    # Local import to avoid circular dependency (models import Base from this module)
    from app.db import models  # noqa: F401

    Base.metadata.create_all(bind=engine)


# Automatically create tables in dev unless disabled
if getenv("AUTO_CREATE_DB", "1") == "1":
    print("AUTO_CREATE_DB is set; initializing database...")
    init_db()
