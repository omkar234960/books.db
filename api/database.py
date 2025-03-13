from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
MYSQL_USER = "root"
MYSQL_PASSWORD = "OMK@r2176"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "books_db"

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
