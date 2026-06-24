from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from model import Historico_atendimento
from node import fila_sistema
from schema import CancelarRequest, Cliente, HistoricoResponse

FUSO_BR = ZoneInfo("America/Sao_Paulo")


def para_fuso_br(data: datetime) -> datetime:
    if data.tzinfo is None:
        data = data.replace(tzinfo=timezone.utc)
    return data.astimezone(FUSO_BR)


rota = APIRouter(tags=["Fila de Clientes"])

    
@rota.post("/clientes")
async def cadastrar_cliente(cliente: Cliente):
    cliente.horario_chegada = datetime.now(FUSO_BR).strftime("%H:%M:%S")
    fila_sistema.enqueue(cliente)
    return {"mensagem": "Cliente adicionado à fila"}
    
@rota.get("/fila")
async def listar_fila():
    return {
        "total": fila_sistema._size,
        "fila": fila_sistema.to_list()
    }
    
@rota.get("/historico")
async def listar_historico(db: Session = Depends(get_db)):
    registros = db.query(Historico_atendimento).order_by(Historico_atendimento.data.desc()).all()

    historico = [
        HistoricoResponse(
            nome=registro.nomeCliente,
            tipo=registro.tipo or "N/A",
            horario_atendimento=para_fuso_br(registro.data).strftime("%d/%m/%Y %H:%M"),
        )
        for registro in registros
    ]

    return {"historico": historico}
    
@rota.post("/fila/chamar")
async def remover_primeiro(db: Session = Depends(get_db)):
    cliente = fila_sistema.dequeue()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Nenhum cliente na fila.")
    
    novo_usuario = Historico_atendimento(
        nomeCliente=cliente.nome,
        tipo=cliente.tipo,
        data=datetime.now(FUSO_BR),
    )
        
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return {"cliente": cliente}
    
@rota.post("/fila/cancelar")
async def remover_especifico(req: CancelarRequest):
    sucesso = fila_sistema.remove_specific(req.nome)
    
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado na fila.")
        
    return {"mensagem": f"Cliente {req.nome} removido da fila com sucesso."}