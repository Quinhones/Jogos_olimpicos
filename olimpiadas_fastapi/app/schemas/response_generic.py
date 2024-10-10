from pydantic import BaseModel
from typing import Optional
class ResponseGeneric(BaseModel):
   mensagem: str
   status: int
  
   class Config:
       orm_mode = True