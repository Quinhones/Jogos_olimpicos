from pydantic import BaseModel

class RankingResponse(BaseModel):
    atleta: str
    posicao: int
    valor: float

    class Config:
        orm_mode = True
