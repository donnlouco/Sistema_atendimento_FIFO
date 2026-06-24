from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, DateTime, Integer, String

from database import Base

FUSO_BR = ZoneInfo("America/Sao_Paulo")


class Historico_atendimento(Base):
    __tablename__ = "historicoatendimento"

    id = Column(Integer, primary_key=True, index=True)
    nomeCliente = Column(String(255))
    tipo = Column(String(50))
    data = Column(DateTime, default=lambda: datetime.now(FUSO_BR))
    
    