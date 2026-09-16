import os
from contextlib import asynccontextmanager
from datetime import date
from typing import Optional

from fastapi import FastAPI, HTTPException
from psycopg import OperationalError
from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row
from pydantic import BaseModel


def build_database_url() -> str:
    if url := os.environ.get("DATABASE_URL"):
        return url

    host = os.environ.get("POSTGRES_HOST", "db")
    port = os.environ.get("POSTGRES_PORT", "5432")
    db = os.environ.get("POSTGRES_DB", "metas")
    user = os.environ.get("POSTGRES_USER", "usuario")
    password = os.environ.get("POSTGRES_PASSWORD", "senha")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


pool = ConnectionPool(build_database_url(), open=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open()
    try:
        yield
    finally:
        pool.close()


app = FastAPI(title="Controle de Metas", lifespan=lifespan)


class MetaOut(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    prioridade: int
    prazo: date
    dias_restantes: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metas", response_model=list[MetaOut])
def listar_metas():
    sql = """
        SELECT id,
               titulo,
               descricao,
               prioridade,
               prazo,
               (prazo - CURRENT_DATE) AS dias_restantes
        FROM metas
        ORDER BY prazo, prioridade
    """
    try:
        with pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(sql)
                return cur.fetchall()
    except OperationalError:
        raise HTTPException(status_code=503, detail="Banco de dados indisponivel")
