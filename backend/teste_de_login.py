# script manual pra testar o FirebaseAuthClient sem precisar do endpoint pronto ainda
# roda com: python teste_de_login.py (precisa do .venv ativado e do .env preenchido)

from app.exceptions import CredenciaisInvalidasError
from app.services.firebase_auth import FirebaseAuthClient

cliente = FirebaseAuthClient()

# caso 1: senha certa -> espera receber o dicionário com idToken, localId etc
resultado = cliente.sign_in("teste@studia.com", "123456")
print("login OK:", resultado["email"], "| uid:", resultado["localId"])

# caso 2: senha errada -> espera CAIR no except, não quebrar o script
try:
    cliente.sign_in("teste@studia.com", "senhaerrada")
    print("ERRO: deveria ter dado CredenciaisInvalidasError e não deu")
except CredenciaisInvalidasError:
    print("login com senha errada barrado corretamente")
