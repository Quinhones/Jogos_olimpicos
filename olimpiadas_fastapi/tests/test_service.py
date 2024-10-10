import pytest
from unittest.mock import Mock
from app.services.competicao_service import CompeticaoService
from app.schemas.enums.modalidade_enum import ModalidadeEnum
from app.schemas.enums.status_competicao_enum import StatusCompeticaoEnum
from app.models.competicao import Competicao
from app.models.resultado import Resultado
from app.schemas.response_generic import ResponseGeneric
from app.controller.competicao_controller import finalizar_competicao
from fastapi import Depends



@pytest.fixture
def mock_db():
   return Mock()
@pytest.fixture
def service(mock_db):
   return CompeticaoService(mock_db)

def test_criar_competicao(service, mock_db):   
   mock_db.query().filter().first.return_value = None
   response = service.criar_competicao(nome="100m Rasos", modalidade=ModalidadeEnum.CEM_METROS_RASOS)
   assert response.mensagem == "Competição '100m Rasos' iniciada."
   assert response.status == 201
                            
def test_adicionar_resultado(service, mock_db):
   # Simula uma competição existente
   competicao = Competicao(id=1, nome="100m Rasos", modalidade=ModalidadeEnum.CEM_METROS_RASOS, status=StatusCompeticaoEnum.ABERTA)
   # Simula que o atleta ainda não participou
   mock_db.query().filter().first.side_effect = [competicao, None]  # Primeiro para a competição, segundo para o atleta não encontrado


def test_obter_ranking(service, mock_db):
   competicao = Competicao(id=1, nome="100m Rasos", modalidade=ModalidadeEnum.CEM_METROS_RASOS, status=StatusCompeticaoEnum.ABERTA)
   mock_db.query().filter().first.return_value = competicao
   mock_db.query().filter_by().all.return_value = []  
   response = service.obter_ranking(competicao_id=1)
   assert "Sem resultados cadastrados para a competição." in response.mensagem

def test_finalizar_competicao(service, mock_db):   
   mock_db.query().filter().first.return_value = Mock(id=1, nome="100m Rasos", modalidade="100M_RASOS", status="aberta")
   service.competicao_repository.salvar = Mock()
   response = service.finalizar_competicao(1)
   assert response.mensagem == "A competição '100m Rasos' da modalidade '100M_RASOS' foi finalizada com sucesso."
   assert response.status == 200