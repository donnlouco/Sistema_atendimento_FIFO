from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from node import fila_sistema, historico_sistema
from model import Cliente, CancelarRequest
from datetime import datetime

rota = APIRouter(tags=["Fila de Clientes"])

    
@rota.post("/clientes")
async def cadastrar_cliente(cliente: Cliente):
    cliente.horario_chegada = datetime.now().strftime("%H:%M:%S")
    fila_sistema.enqueue(cliente)
    return {"mensagem": "Cliente adicionado à fila"}
    
@rota.get("/fila")
async def listar_fila():
    return {
        "total": fila_sistema._size,
        "fila": fila_sistema.to_list()
    }
    
@rota.get("/historico")
async def listar_historico():
    return {
        "historico": historico_sistema
    }
    
@rota.post("/fila/chamar")
async def remover_primeiro():
    cliente = fila_sistema.dequeue()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Nenhum cliente na fila.")
        
    historico_sistema.append({
        "nome": cliente.nome,
        "horario_atendimento": datetime.now().strftime("%H:%M:%S")
    })
    
    return {"cliente": cliente}
    
@rota.post("/fila/cancelar")
async def remover_especifico(req: CancelarRequest):
    sucesso = fila_sistema.remove_specific(req.nome)
    
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado na fila.")
        
    return {"mensagem": f"Cliente {req.nome} removido da fila com sucesso."}