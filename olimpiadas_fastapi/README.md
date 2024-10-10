# API de Competições
Esta é uma API desenvolvida com FastAPI para gerenciar competições esportivas. A aplicação permite a criação de competições, cadastro de resultados e obtenção de rankings.
## Requisitos
- Python 3.9 ou superior
- Docker
- Docker Compose
## Estrutura do Projeto
app/
├── controller/
├── models/
├── repositories/
├── schemas/
├── services/
├── main.py
└── database.py
## Configuração do Banco de Dados
A aplicação utiliza o PostgreSQL como banco de dados, que é configurado via Docker.
### Variáveis de Ambiente
Para conectar ao banco de dados, certifique-se de que as seguintes variáveis de ambiente estão definidas no seu arquivo `.env` ou diretamente no seu ambiente:
DATABASE_URL=postgresql://db_user:db_senha@db:5432/db_name
### Executando a Aplicação
1. **Clone o repositório:**
  ```bash
  git clone https://github.com/seu_usuario/seu_repositorio.git
  cd seu_repositorio
2. Construir e iniciar os containers:
docker-compose up --build

3. Acessar a API:
A API estará disponível em http://localhost:8000.
4. Documentação da API:
A documentação da API pode ser acessada em http://localhost:8000/docs.
Endpoints Principais
Criar Competição
• URL: /competicoes
• Método: POST
• Request Body:
{
 "nome": "Nome da Competição",
 "modalidade": "CEM_METROS_RASOS"
}

• Response:
{
 "id": 1,
 "nome": "Nome da Competição",
 "modalidade": "CEM_METROS_RASOS",
 "status": "aberta"
}

Cadastrar Resultado
• URL: /resultados
• Método: POST
• Request Body:
{
 "competicao_id": 1,
 "atleta_id": 1,
 "valor": 9.58,
 "unidade": "segundos"
}

• Response:
{
 "id": 1,
 "competicao_id": 1,
 "atleta_id": 1,
 "valor": 9.58,
 "unidade": "segundos"
}

Finalizar Competição
• URL: /competicoes/{competicao_id}/finalizar
• Método: POST
• Response:
{
 "id": 1,
 "nome": "Nome da Competição",
 "modalidade": "CEM_METROS_RASOS",
 "status": "encerrada"
}

Obter Ranking
• URL: /competicoes/{competicao_id}/ranking
• Método: GET
• Response:
[
 {
   "atleta_id": 1,
   "resultado": 9.58,
   "unidade": "segundos"
 },
 {
   "atleta_id": 2,
   "resultado": 10.10,
   "unidade": "segundos"
 }
]