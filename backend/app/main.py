"""Ponto de entrada da API do Studia.

Para rodar em desenvolvimento (dentro da pasta backend/):
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

app = FastAPI(
    title="Studia API",
    description="Backend do Studia — autenticação e gestão de objetivos/metas.",
    version="0.1.0",
)

@app.get("/health", tags=["infra"])
def health_check() -> dict:
    """Endpoint simples para verificar se a API está no ar."""
    return {"status": "ok"}
