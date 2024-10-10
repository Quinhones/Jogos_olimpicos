import os
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from app.controller.competicao_controller import router as competicao_router
from app.models.competicao import Competicao
from app.models.atleta import Atleta
from app.models.resultado import Resultado
from app.database import Base  

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://db_user:db_senha@db:5432/db_name')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def wait_for_db_connection(retries=5, delay=5):
   for _ in range(retries):
       try:
           connection = engine.connect()
           connection.close()
           print("Conexão com o banco de dados estabelecida.")
           return True
       except OperationalError:
           print(f"Banco de dados não está pronto. Tentando novamente em {delay} segundos...")
           time.sleep(delay)
   raise ConnectionError("Não foi possível conectar ao banco de dados após várias tentativas.")

app = FastAPI()

app.include_router(competicao_router)

@app.on_event("startup")
def startup_event():
   wait_for_db_connection()  
   print("Criando tabelas no banco de dados...")
   try:
       Base.metadata.create_all(bind=engine)  
       print("Tabelas criadas.")
       
       with engine.connect() as connection:
           result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
           tables = result.fetchall()
           print("Tabelas no banco de dados:", [table[0] for table in tables])
   except Exception as e:
       print(f"Ocorreu um erro ao criar as tabelas: {e}")

@app.get("/")
def read_root():
   return {"message": "API rodando corretamente"}