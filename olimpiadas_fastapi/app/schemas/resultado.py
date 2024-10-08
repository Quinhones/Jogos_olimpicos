from pydantic import BaseModel, validator
from typing import Optional
from enum import Enum
# from app.schemas.competicao import ModalidadeEnum

class UnidadeEnum(str, Enum):
    SEGUNDOS = "s"
    METROS = "m"

class ResultadoCreate(BaseModel):
    competicao_id: int
    atleta_id: int
    valor: float
    unidade: UnidadeEnum

    @validator('unidade')
    def validate_unidade(cls, value, values, **kwargs):
        # Aqui você pode adicionar validações adicionais se necessário
        return value

    class Config:
        orm_mode = True

class ResultadoRead(BaseModel):
    id: int
    competicao_id: int
    atleta_id: int
    numero_tentativas: Optional[int] = 1
    unidade: UnidadeEnum
    valor: float

    class Config:
        orm_mode = True

class ResultadoResponse(BaseModel):
    mensagem: str
    resultado: ResultadoRead

    class Config:
        orm_mode = True
