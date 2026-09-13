# Studia — Backend (FastAPI)

API em Python responsável pela autenticação e pelas regras de negócio do Studia.

## Como rodar

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # e preencha a chave do Firebase
uvicorn app.main:app --reload
```

A documentação interativa (Swagger) fica em <http://localhost:8000/docs>.
