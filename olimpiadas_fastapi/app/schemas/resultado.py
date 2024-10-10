from pydantic import BaseModel
class ResultadoCreate(BaseModel):
   competicao: str
   atleta: str
   value: float
   unidade: str
class ResultadoResponse(BaseModel):
   competicao: str
   atleta: str
   value: float
   unidade: str
   mensagem: str = "Resultado do atleta adicionado"