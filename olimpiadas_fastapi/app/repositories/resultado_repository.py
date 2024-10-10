from sqlalchemy.orm import Session
from app.models.resultado import Resultado  
class ResultadoRepository:
   def __init__(self, db: Session):
       self.db = db
   
   def buscar_tentativas_por_competicao_e_atleta(self, competicao_id: int, atleta_id: int):
       return self.db.query(Resultado).filter_by(competicao_id=competicao_id, atleta_id=atleta_id).all()
  
   def atleta_ja_participou(self, competicao_id: int, atleta_id: int):
       return self.db.query(Resultado).filter_by(competicao_id=competicao_id, atleta_id=atleta_id).first()
   
   def buscar_por_competicao(self, competicao_id: int):
       return self.db.query(Resultado).filter(Resultado.competicao_id == competicao_id).all()