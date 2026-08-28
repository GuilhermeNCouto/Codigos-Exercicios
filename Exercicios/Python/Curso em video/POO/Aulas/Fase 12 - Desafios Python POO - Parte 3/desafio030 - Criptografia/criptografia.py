'''
Diagrama:
Credencial
----------------
+ @senha
- __hash
----------------
+ validar(chave)
'''
from hashlib import sha256


class Credencial:

    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        raise PermissionError("Não é permitido recuperar a senha original!")

    @senha.setter
    def senha(self, chave: str):
        if not isinstance(chave, str) or len(chave) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres!")
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()

    def validar(self, chave: str) -> str:
        chave_hash = sha256(chave.encode("utf-8")).hexdigest()
        
        if self.__hash == chave_hash:
            return "Senha Confere!"
            
        return "Senha Incorreta!"