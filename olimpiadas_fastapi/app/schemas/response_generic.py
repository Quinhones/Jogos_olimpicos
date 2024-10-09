from pydantic import BaseModel
from typing import Any, Optional
class ResponseGeneric(BaseModel):
   mensagem: str
   data: Optional[Any] = None
   status: Optional[int] = None