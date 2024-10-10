from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
class Resultado(Base):
   __tablename__ = 'resultados'
   id = Column(Integer, primary_key=True, index=True)
   competicao_id = Column(Integer, ForeignKey('competicoes.id'))
   atleta_id = Column(Integer, ForeignKey('atletas.id'))
   valor = Column(Float, nullable=False)
   unidade = Column(String, nullable=False)
   competicao = relationship("Competicao", back_populates="resultados")
   atleta = relationship("Atleta", back_populates="resultados")