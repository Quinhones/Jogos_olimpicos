from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from app.schemas.enums.status_competicao_enum import StatusCompeticaoEnum
from app.models.resultado import Resultado  # Certifique-se de que o caminho está correto
class Competicao(Base):
   __tablename__ = 'competicoes'
   id = Column(Integer, primary_key=True, index=True)
   nome = Column(String, index=True)
   modalidade = Column(String, index=True)  # Altere para o tipo de dados adequado
   status = Column(Enum(StatusCompeticaoEnum), default=StatusCompeticaoEnum.ABERTA)
   # Definindo a relação
   resultados = relationship("Resultado", back_populates="competicao")