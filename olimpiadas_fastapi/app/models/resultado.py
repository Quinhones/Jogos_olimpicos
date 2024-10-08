from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    
    competicao_id = Column(Integer, ForeignKey("competicoes.id"), nullable=False)
    atleta_id = Column(Integer, ForeignKey("atletas.id"), nullable=False)
    
    numero_tentativas = Column(Integer, nullable=False, default=1)
    unidade = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    # Relacionamentos
    competicao = relationship("Competicao", back_populates="resultados")
    atleta = relationship("Atleta", back_populates="resultados")
