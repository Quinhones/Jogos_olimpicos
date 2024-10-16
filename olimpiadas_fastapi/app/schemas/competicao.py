from pydantic import BaseModel
from app.schemas.enums.modalidade_enum import ModalidadeEnum
class CompeticaoCreate(BaseModel):
   nome: str
   modalidade: ModalidadeEnum
   class Config:
       orm_mode = True
class CompeticaoResponse(BaseModel):
   id: int
   nome: str
   modalidade: ModalidadeEnum
   status: str  
   class Config:
       orm_mode = True