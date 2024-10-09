from sqlalchemy.orm import Session
from app.models.atleta import Atleta

class AtletaRepository:
   def __init__(self, db: Session):
       self.db = db
       
   def buscar_por_nome(self, nome: str):
       return self.db.query(Atleta).filter(Atleta.nome == nome).first()