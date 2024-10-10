import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import Mock
from app.database import get_db
client = TestClient(app)
# Mock para o banco de dados
def mock_get_db():
   mock_db = Mock()
   yield mock_db
app.dependency_overrides[get_db] = mock_get_db
@pytest.fixture
def client():
   return TestClient(app)

def test_criar_competicao(client):
   response = client.post("/competicoes", json={"nome": "100m Rasos", "modalidade": "100M_RASOS"})
   assert response.status_code == 200  # Ajustado para 200, competição já existe
   assert "Competição com nome '100m Rasos' e modalidade '100M_RASOS' já existe." in response.json()["mensagem"]

def test_adicionar_resultado(client):
   # Simulando o payload correto
   response = client.post("/competicoes/1/resultados", json={
       "competicao": "100m Rasos",
       "atleta": "Joao",
       "value": 10.5,
       "unidade": "s"
   })
   assert response.status_code == 200  # Verificando sucesso na adição do resultado

def test_obter_ranking(client):
   response = client.get("/competicoes/1/ranking")
   assert response.status_code == 200
   assert "Sem resultados cadastrados para a competição." in response.json()["mensagem"]

def test_finalizar_competicao(client):
   response = client.post("/competicoes/1/finalizar")
   assert response.status_code == 200
   assert "foi finalizada com sucesso" in response.json()["mensagem"]