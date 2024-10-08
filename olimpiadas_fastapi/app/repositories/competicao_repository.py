from sqlalchemy.orm import Session
from app.models.competicao import Competicao
from app.models.resultado import Resultado

class CompeticaoRepository:
    def _init_(self, db: Session):
        self.db = db

    def criar_competicao(self, competicao: Competicao):
        self.db.add(competicao)
        self.db.commit()
        self.db.refresh(competicao)
        return competicao

    def encontrar_competicao(self, competicao_id: int):
        return self.db.query(Competicao).filter(Competicao.id == competicao_id).first()

    def find_by_name(self, nome: str):
        return self.db.query(Competicao).filter(Competicao.nome == nome).first()

    def get_resultados_by_competicao(self, competicao_id: int):
        return self.db.query(Resultado).filter(Resultado.competicao_id == competicao_id).all()

    def add_resultado(self, resultado: Resultado):
        self.db.add(resultado)
        self.db.commit()
        self.db.refresh(resultado)
        return resultado
    
    def listar_competicoes(self):
        return self.db.query(Competicao).all()