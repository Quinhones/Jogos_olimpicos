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

   def obter_ranking(self):
        if self.modalidade == "LANCAMENTO_DARDO":
            # Para lançamento de dardo, pega o melhor resultado de cada atleta
            resultados_agrupados = {}
            for resultado in self.resultados:
                if resultado.atleta_id not in resultados_agrupados:
                    resultados_agrupados[resultado.atleta_id] = resultado
                else:
                    if resultado.valor > resultados_agrupados[resultado.atleta_id].valor:
                        resultados_agrupados[resultado.atleta_id] = resultado
            ranking = sorted(resultados_agrupados.values(), key=lambda r: r.valor, reverse=True)
        else:
            # Para 100m, ordena pelo menor tempo
            ranking = sorted(self.resultados, key=lambda r: r.valor)
        return [(resultado.atleta, resultado) for resultado in ranking]
   
   def finalizar(self):
       self.status = StatusCompeticaoEnum.ENCERRADA