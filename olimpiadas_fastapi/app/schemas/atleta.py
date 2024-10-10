from pydantic import BaseModel

class AtletaCreate(BaseModel):
   nome: str
   class Config:
       orm_mode = True
class AtletaResponse(BaseModel):
   id: int
   nome: str
   class Config:
       orm_mode = True