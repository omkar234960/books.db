import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.getenv("VERCEL") == "1":
    DATABASE_URL = "sqlite:///:memory:"
else:
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'books.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
