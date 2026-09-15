# erros próprios pra não deixar o httpx/Firebase vazar exceções genéricas pro resto do código

class CredenciaisInvalidasError(Exception):
    pass


class FirebaseIndisponivelError(Exception):
    pass
