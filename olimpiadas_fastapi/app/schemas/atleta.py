from pydantic import BaseModel, validator
from typing import Optional, List
from app.schemas.resultado import ResultadoRead

class AtletaCreate(BaseModel):
    nome: str

    @validator('nome')
    def nome_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("O nome do atleta não pode estar vazio")
        return value

    class Config:
        orm_mode = True

class AtletaResponse(BaseModel):
    id: int
    nome: str
    resultados: Optional[List['ResultadoRead']] = []

    class Config:
        orm_mode = True

# Necessário para referência circular
AtletaResponse.update_forward_refs()
