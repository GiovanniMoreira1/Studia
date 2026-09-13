"""Configurações da aplicação lidas de variáveis de ambiente / arquivo .env."""

import os

from dotenv import load_dotenv

# Lê o arquivo .env (se existir) e joga os valores em os.environ.
load_dotenv()


class Settings:
    """Agrupa as configurações num único objeto em vez de espalhar os.getenv pelo código."""

    def __init__(self) -> None:
        self.firebase_web_api_key: str = os.getenv("FIREBASE_WEB_API_KEY", "")
        self.firebase_auth_emulator_host: str = os.getenv("FIREBASE_AUTH_EMULATOR_HOST", "")

    @property
    def firebase_auth_base_url(self) -> str:
        """URL base da REST API do Firebase Authentication (Identity Toolkit).

        Se o emulador estiver configurado, aponta para ele; senão, para o Firebase real.
        """
        if self.firebase_auth_emulator_host:
            return f"http://{self.firebase_auth_emulator_host}/identitytoolkit.googleapis.com/v1"
        return "https://identitytoolkit.googleapis.com/v1"


# Instância única usada pelo resto da aplicação.
settings = Settings()
