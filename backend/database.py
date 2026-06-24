import os
import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:9626@localhost:5433/filaEstrutura",
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)


print("Conectando ao banco de dados PostgreSQL...")
for tentativa in range(10):  
    try:
        conexao_teste = engine.connect()
        conexao_teste.close()
        print("Conectado ao PostgreSQL com sucesso!")
        break
    except OperationalError:
        print(f"Banco de dados inicializando... Tentativa {tentativa + 1}/10. Aguardando 3 segundos.")
        time.sleep(3)
else:
    raise RuntimeError("Não foi possível conectar ao banco de dados após várias tentativas.")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    import model 

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()