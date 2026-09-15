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

## Testando o cliente do Firebase manualmente

Antes de existir o endpoint, dá pra testar a classe `FirebaseAuthClient` direto:

```bash
cd backend
source .venv/bin/activate
python teste_de_login.py
```
