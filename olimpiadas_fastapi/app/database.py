from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://db_user:db_senha@db:5432/db_name')
# Configuração da engine do SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  

def get_db() -> Generator[Session, None, None]:
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()