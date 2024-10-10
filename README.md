Instalação e Configuração
Pré-requisitos
1. Python 3.10 ou superior
2. Docker e Docker Compose
3. PostgreSQL (ou via Docker)

4. Passos de Instalação
5. Clone o repositório:
git clone <Link do repositório do github>
cd jogos-olimpicos

1. Instale as dependências:
• Ative seu ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate

• Instale as dependências:
pip install -r requirements.txt

1. Rodando com Docker:
A aplicação está configurada para rodar com Docker. Basta usar o comando:
docker-compose up --build
Isso irá iniciar o servidor FastAPI e o banco de dados PostgreSQL configurado no Docker.

1. Migração do Banco de Dados:
No momento, o sistema utiliza SQLAlchemy para criar automaticamente as tabelas no banco de dados definido. Quando o projeto é inicializado, o FastAPI criará automaticamente as tabelas conforme definidas nos modelos.

Testes
1. Executando Testes Unitários e de Integração:
• Para rodar os testes, utilize o comando:
pytest
Isso irá rodar todos os testes nas pastas tests/test_controller.py e tests/test_service.py.

Formas de testar a API:

Acessar o Swagger UI:
Depois que o servidor estiver rodando, você pode acessar a documentação interativa no seu navegador, indo para a seguinte URL:
http://127.0.0.1:8000/docs
O Swagger UI será carregado, exibindo todos os endpoints disponíveis, bem como as opções para realizar testes diretamente na interface.
Ou utilização de ferramentas como Insomnia e Postman.

Exemplo de Uso da API
1. Criar Competição:
• Endpoint: /competicoes
• Método: POST
• Body:
{
   "nome": "100m Rasos",
   "modalidade": "100M_RASOS"
}
• Resposta:
{
   "mensagem": "Competição '100m Rasos' iniciada.",
   "status": 201
}

1. Adicionar Resultado:
• Endpoint: /competicoes/{competicao_id}/resultados
• Método: POST
• Body:
{
  "competicao": "100m Rasos",
  "atleta": "Joao",
  "value": 10.5,
  "unidade": "s"
}
• Resposta:
{
   "mensagem": "Resultado adicionado com sucesso",
   "value": 10.5
}

1. Obter Ranking:
• Endpoint: /competicoes/{competicao_id}/ranking
• Método: GET
• Resposta:
{
   "mensagem": "Ranking parcial da competição '100m Rasos'",
   "ranking": [
       {
           "atleta": "Joao",
           "pontuacao": 10.5,
           "unidade": "s",
           "posicao": 1
       }
   ]
}

1. Finalizar Competição:
• Endpoint: /competicoes/{competicao_id}/finalizar
• Método: POST
• Resposta:
{
   "mensagem": "A competição '100m Rasos' foi finalizada com sucesso."
}