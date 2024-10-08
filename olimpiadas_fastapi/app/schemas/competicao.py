from pydantic import BaseModel, validator
from typing import Optional, List
from app.schemas.resultado import ResultadoRead
from app.schemas.enums.modalidade_enum import ModalidadeEnum

class CompeticaoCreate(BaseModel):
    nome: str
    modalidade: ModalidadeEnum

    @validator('nome')
    def nome_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("O nome da competição não pode estar vazio")
        return value

    class Config:
        orm_mode = True

class CompeticaoResponse(BaseModel):
    id: int
    nome: str
    status: str
    modalidade: str
    resultados: Optional[List[ResultadoRead]] = []

    class Config:
        orm_mode = True
        use_enum_values = True
