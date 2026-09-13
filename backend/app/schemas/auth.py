"""Schemas (formatos de dados) do fluxo de autenticação.

Um schema descreve o "contrato" do endpoint: quais campos entram na requisição
e quais campos saem na resposta. O Pydantic valida automaticamente os dados
recebidos — se algo estiver faltando ou no formato errado, a requisição nem
chega na nossa lógica.
"""

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    """Dados que o cliente (tela de login) envia para POST /auth/login."""

    # EmailStr garante que o valor tem formato de e-mail válido (item do checklist).
    email: EmailStr = Field(..., description="E-mail cadastrado do usuário")
    # min_length cobre senha vazia; 6 é o mínimo que o próprio Firebase exige.
    senha: str = Field(..., min_length=6, description="Senha de acesso")

    # Exemplo que aparece pré-preenchido no Swagger (/docs).
    model_config = {
        "json_schema_extra": {
            "examples": [{"email": "teste@studia.com", "senha": "123456"}]
        }
    }


class LoginResponse(BaseModel):
    """Dados devolvidos quando o login dá certo (HTTP 200)."""

    mensagem: str = Field(..., description="Mensagem amigável de sucesso")
    id_usuario: str = Field(..., description="Identificador do usuário no Firebase (uid)")
    email: EmailStr
    token: str = Field(..., description="Token JWT emitido pelo Firebase; enviar nas próximas requisições")
    expira_em: int = Field(..., description="Validade do token em segundos")


class ErrorResponse(BaseModel):
    """Formato único para respostas de erro (400, 401, 500)."""

    detalhe: str
