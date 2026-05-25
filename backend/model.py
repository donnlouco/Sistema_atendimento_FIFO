from pydantic import BaseModel
from typing import Optional


class Cliente(BaseModel):
    nome: str
    idade: int
    horario_chegada: Optional[str] = None
    
class CancelarRequest(BaseModel):
    nome: str