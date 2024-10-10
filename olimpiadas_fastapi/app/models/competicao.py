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

   def test_obter_ranking(client):
    # Criar uma competição com o valor correto da modalidade
    response = client.post("/competicoes", json={"nome": "100m Rasos", "modalidade": "100M_RASOS"})
    assert response.status_code == 201  # Certifique-se de que a competição foi criada com sucesso
    # Obter o ranking
    response = client.get("/competicoes/1/ranking")
    # Verificar se a resposta é 200
    assert response.status_code == 200
    # Verificar se a mensagem está correta
    assert "Sem resultados cadastrados para a competição." in response.json()["mensagem"]