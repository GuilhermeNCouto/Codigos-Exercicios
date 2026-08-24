'''
Diagrama:
Credencial
----------------
+ @senha
- __hash
----------------
+ validar(chave)
'''
import hashlib

class Credencial:

    def __init__(self, senha=""):
        self.__hash = self.senha = senha

    @property
    def senha(self):
        raise PermissionError("Não é permitido recuperar a senha original!")

    @senha.setter
    def senha(self, nova_senha: str):
        self.__hash = hashlib.sha256(nova_senha.encode("utf-8")).hexdigest()

    def validar(self, chave: str) -> bool:
        validacao = self.__hash == hashlib.sha256(chave.encode("utf-8")).hexdigest()
        if validacao:
            return f"Senha Confere!\n{validacao}"
        return f"Senha Incorreta!\n{validacao}"
