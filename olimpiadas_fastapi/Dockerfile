# Use uma imagem base do Python
FROM python:3.9

# Cria um diretório para a aplicação
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .

# Instala as dependências sem tentar atualizar o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]