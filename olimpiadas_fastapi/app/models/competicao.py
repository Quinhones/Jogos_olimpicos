from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from app.schemas.enums.status_competicao_enum import StatusCompeticaoEnum
from app.schemas.enums.modalidade_enum import ModalidadeEnum  
class Competicao(Base):
   __tablename__ = "competicoes"

   id = Column(Integer, primary_key=True, index=True)
   nome = Column(String, nullable=False)
   modalidade = Column(Enum(ModalidadeEnum), nullable=False)  
   status = Column(Enum(StatusCompeticaoEnum), nullable=False, default=StatusCompeticaoEnum.ABERTA)   
   resultados = relationship("Resultado", back_populates="competicao")
   
   def adicionar_resultado(self, resultado):
       self.resultados.append(resultado)

  