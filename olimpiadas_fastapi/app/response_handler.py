from fastapi.responses import JSONResponse

class ResponseGeneric:
   def __init__(self, mensagem: str, status: int):
       self.mensagem = mensagem
       self.status = status
       
def create_response(response, status_code=200):
   
   if isinstance(response, ResponseGeneric):
       
       return JSONResponse(content={"mensagem": response.mensagem}, status_code=response.status)
   
   return JSONResponse(content=response.dict(), status_code=status_code)