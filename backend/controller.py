from fastapi import APIRouter
from pydantic import BaseModel
from main import

rota = APIRouter(prefix="/", tags=["Rotas"])

class Cliente(BaseModel):
    nome: str
    idade: int
    
@rota.post("/fila")
async def inserir_fila(dados: Cliente):
    
