# backend/app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

from dotenv import load_dotenv
load_dotenv()

# Read DATABASE_URL from environment (Render sets this for managed DB)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # fallback for local Docker compose / local dev
    DATABASE_URL = "postgresql+psycopg2://chatuser:chatpass@db:5432/mini_chat"

# Render (and some providers) return "postgres://", SQLAlchemy expects "postgresql+psycopg2://"
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://", 1)

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    # create tables if they don't exist (simple approach)
    Base.metadata.create_all(bind=engine)
