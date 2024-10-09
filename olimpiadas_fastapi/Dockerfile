# Usando a imagem oficial do Python
FROM python:3.9
# Definindo o diretório de trabalho dentro do container
WORKDIR /app
# Copiando o arquivo de dependências
COPY requirements.txt .
# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt
# Copiando o restante do código
COPY . .
# Adicionando um atraso de 10 segundos para garantir que o banco de dados esteja pronto
CMD sleep 10 && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload