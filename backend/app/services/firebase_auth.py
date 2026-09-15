import httpx

from app.config import settings
from app.exceptions import CredenciaisInvalidasError, FirebaseIndisponivelError

# mensagens que o Firebase manda quando o problema é email/senha errados
ERROS_DE_CREDENCIAL = {"EMAIL_NOT_FOUND", "INVALID_PASSWORD", "INVALID_LOGIN_CREDENTIALS", "USER_DISABLED"}


class FirebaseAuthClient:
    def __init__(self):
        self.api_key = settings.firebase_web_api_key
        self.base_url = settings.firebase_auth_base_url

    def sign_in(self, email: str, senha: str) -> dict:
        url = f"{self.base_url}/accounts:signInWithPassword?key={self.api_key}"

        try:
            resposta = httpx.post(
                url,
                json={"email": email, "password": senha, "returnSecureToken": True},
                timeout=10,
            )
        except httpx.RequestError:
            # sem internet, Firebase fora do ar, DNS bugado... qualquer coisa que não seja resposta HTTP cai aqui
            raise FirebaseIndisponivelError("não foi possível conectar ao Firebase")

        dados = resposta.json()

        if resposta.status_code == 200:
            return dados

        # deu erro, mas o Firebase respondeu — olha o código pra saber se foi o usuário que errou
        codigo = dados.get("error", {}).get("message", "")
        if codigo in ERROS_DE_CREDENCIAL:
            raise CredenciaisInvalidasError("e-mail ou senha incorretos")

        raise FirebaseIndisponivelError(f"erro do Firebase: {codigo}")
