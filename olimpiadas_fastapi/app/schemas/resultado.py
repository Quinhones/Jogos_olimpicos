from pydantic import BaseModel
class ResultadoCreate(BaseModel):
   competicao: str
   atleta: str  # Nome do atleta em vez do ID
   valor: float
   unidade: str   
   class Config:
       orm_mode = True