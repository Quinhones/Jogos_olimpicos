from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import UniqueConstraint

class Competicao(Base):
    __tablename__ = "competicoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False, unique=True)
    modalidade = Column(String, nullable=False)
    status = Column(String, default="aberta", nullable=False)
    
    resultados = relationship("Resultado", back_populates="competicao")

    __table_args__ = (UniqueConstraint('nome', name='uq_nome_competicao'),)
