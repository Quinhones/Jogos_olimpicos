from pydantic import BaseModel
from typing import List
class AtletaRanking(BaseModel):
   atleta: str
   pontuacao: float
   unidade: str
   posicao: int
class RankingResponse(BaseModel):
   mensagem: str
   ranking: List[AtletaRanking]
   class Config:
       orm_mode = True