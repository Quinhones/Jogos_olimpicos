## Requisitos
 
- Python 3.7 ou superior
- FastAPI
- Uvicorn
- (Opcional) Insomnia/Postman para testes
  
## Instalação
 
1. *Clone o repositório*:
  bash
  git clone <URL_DO_REPOSITORIO>
  cd project
 
2. **Crie um ambiente virutal**:
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
 
3. **Instale as dependencias**:
pip install fastapi uvicorn
 
4. **Rodando a aplicação**:
uvicorn controller.api:app --reload
 
O servidor estará disponível em http://127.0.0.1:8000.
 

