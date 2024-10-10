from sqlalchemy.orm import Session
from app.models.atleta import Atleta

class AtletaRepository:
   
   def __init__(self, db: Session):
       self.db = db

   def buscar_por_nome(self, nome: str) -> Atleta:
       return self.db.query(Atleta).filter(Atleta.nome == nome).first()
   
   def salvar(self, nome: str) -> Atleta:
       novo_atleta = Atleta(nome=nome)
       self.db.add(novo_atleta)
       self.db.commit()
       self.db.refresh(novo_atleta)
       return novo_atleta
   
   def buscar_por_ids(self, ids: list):
       return self.db.query(Atleta).filter(Atleta.id.in_(ids)).all()