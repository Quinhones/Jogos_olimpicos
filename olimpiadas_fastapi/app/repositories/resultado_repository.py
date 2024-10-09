from sqlalchemy.orm import Session
from app.models.resultado import Resultado

class ResultadoRepository:   
   def __init__(self, db: Session):
       self.db = db

   def add_resultado(self, competicao_id: int, atleta_id: int, valor: float, unidade: str):
       resultado = Resultado(competicao_id=competicao_id, atleta_id=atleta_id, valor=valor, unidade=unidade)
       self.db.add(resultado)
       self.db.commit()
       self.db.refresh(resultado)
       return resultado
   
   def get_resultados_by_competicao(self, competicao_id: int):
       return self.db.query(Resultado).filter(Resultado.competicao_id == competicao_id).all()
   
