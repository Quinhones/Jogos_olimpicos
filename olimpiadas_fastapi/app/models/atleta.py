from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
class Atleta(Base):
   __tablename__ = 'atletas'
   id = Column(Integer, primary_key=True, index=True)
   nome = Column(String, index=True)
   #
   resultados = relationship("Resultado", back_populates="atleta")