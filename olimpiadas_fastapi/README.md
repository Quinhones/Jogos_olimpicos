# API Jogos Olímpicos

Este projeto é uma API para gerenciar competições dos Jogos Olímpicos, permitindo criar competições, registrar resultados e gerar rankings.

## *Pré-requisitos*

Antes de começar, você precisará ter o *Python* instalado na sua máquina.
---

## *Como rodar o projeto localmente*

Siga os passos abaixo para rodar o projeto na sua máquina local:

### 1. *Clone o repositório*

Abra o terminal e execute o seguinte comando para clonar o repositório:

```bash
git clone <URL_DO_REPOSITORIO>

Entre na pasta do projeto:

cd SEU_REPOSITORIO

## 2. Crie um ambiente virtual

Crie e ative um ambiente virtual para o projeto. Isso é importante para garantir que as dependências do projeto não conflitem com outras dependências no seu sistema.

No Windows:

python -m venv venv
venv\Scripts\activate

No macOS/Linux:

python3 -m venv venv
source venv/bin/activate

## 3. Instale as dependências

Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

pip install -r requirements.txt

## 4. Rode a aplicação

Depois de instalar as dependências, você pode iniciar a aplicação com o comando:

uvicorn app.main:app --reload

Isso vai rodar o servidor de desenvolvimento do FastAPI, que estará disponível no endereço:

http://127.0.0.1:8000

## 5. Acesse a documentação da API

O FastAPI gera automaticamente uma interface interativa de documentação da API, disponível em:

	•	http://127.0.0.1:8000/docs (Swagger UI)
	•	http://127.0.0.1:8000/redoc (OpenAPI)


## Aqui estão algumas regras das competições para ajudar o usuário: 

Nesta API, você pode criar e gerenciar diferentes tipos de competições. As competições implementadas incluem:

Modalidades Suportadas:

	1.	100m rasos (menor tempo vence)
	2.	Lançamento de dardo (maior distância vence)

Regras de Competição por Modalidade:

	•	100m rasos:
	•	Cada atleta pode competir apenas uma vez por fase.
	•	O menor tempo registrado é o vencedor.
	•	A unidade para registrar o tempo deve ser segundos (s). Qualquer outra unidade resultará em erro.
	•	Lançamento de dardo:
	•	Cada atleta tem direito a três tentativas.
	•	O resultado final é calculado com base na melhor tentativa do atleta.
	•	A unidade para registrar a distância deve ser metros (m). Qualquer outra unidade resultará em erro.

Regras de Encerramento e Ranking:

	•	Uma competição pode ser encerrada manualmente por meio da API.
	•	Antes de a competição ser encerrada, a API retornará um ranking parcial.
	•	Após o encerramento, o ranking final será gerado, e o primeiro colocado será marcado como “CAMPEÃO!!!”.
	•	Se o ranking for visualizado antes do encerramento, o primeiro colocado será marcado como “Campeão parcial”, e uma mensagem indicará que o ranking ainda é parcial.


## Como testar a API

Você pode usar ferramentas como Postman ou Insomnia para testar os endpoints da API.

Exemplos de Endpoints

1. Criar uma competição:

	•	POST /competicao
	•	Exemplo de payload:

{
  "nome": "fase 1",
  "modalidade": "100m rasos"
}

{
  "nome": "semifinal",
  "modalidade": "lançamento de dardo"
}



2. Registrar um resultado:

	•	POST /resultado
	•	Exemplo de payload:

{
  "competicao": "fase 1",
  "atleta": "João",
  "value": 9.58,
  "unidade": "s"
}

Obs os ids utilizados para as cmopetições foram determinados como:
1 = 100m rasos
2 = lançamento de dardo

3. Obter o ranking de uma competição:

	•	GET /ranking/{competicao_id}

4. Finalizar uma competição:

	•	POST /finalizar/{competicao_id}

Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Detalhes Importantes:

	1.	Pré-requisitos: Certifique-se de que o Python está instalado.
	2.	Configuração do ambiente: Criação e ativação de ambiente virtual e instalação das dependências.
	3.	Rodando o projeto: Iniciar o servidor da API FastAPI.
	4.	Testando a API: Utilize ferramentas como Postman ou Insomnia para fazer as requisições e testar os endpoints.
