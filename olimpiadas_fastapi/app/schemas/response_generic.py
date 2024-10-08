from pydantic import BaseModel
from typing import Optional

class ResponseGeneric(BaseModel):
    status: int
    mensagem: str
    data: Optional[dict] = None

    class Config:
        orm_mode = True