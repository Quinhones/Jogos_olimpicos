from sqlalchemy.orm import Session
from app.models.competicao import Competicao
from app.models.resultado import Resultado
from app.models.atleta import Atleta
class CompeticaoRepository:
   def __init__(self, db: Session):
       self.db = db
   
   def salvar(self, competicao: Competicao):
       self.db.add(competicao)
       self.db.commit()
       self.db.refresh(competicao)
   
   def buscar_por_id(self, competicao_id: int) -> Competicao:
       return self.db.query(Competicao).filter(Competicao.id == competicao_id).first()
   
   def buscar_por_nome_e_modalidade(self, nome: str, modalidade: str) -> Competicao:
       return self.db.query(Competicao).filter(Competicao.nome == nome, Competicao.modalidade == modalidade).first()
   
   def listar_competicoes(self):
       return self.db.query(Competicao).all()
   
   def salvar_resultado(self, resultado: Resultado):
       self.db.add(resultado)
       self.db.commit()
       self.db.refresh(resultado)
   
   def buscar_resultados_por_competicao(self, competicao_id: int):
       return self.db.query(Resultado).filter(Resultado.competicao_id == competicao_id).all()
   
   def buscar_atleta_por_nome(self, nome: str) -> Atleta:
       return self.db.query(Atleta).filter(Atleta.nome == nome).first()
  
   def verificar_atleta_na_competicao(self, competicao_id: int, atleta_id: int) -> bool:
       return self.db.query(Resultado).filter(Resultado.competicao_id == competicao_id, Resultado.atleta_id == atleta_id).first() is not None