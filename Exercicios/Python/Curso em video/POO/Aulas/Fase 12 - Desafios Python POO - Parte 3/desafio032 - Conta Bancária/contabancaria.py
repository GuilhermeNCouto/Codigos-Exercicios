'''
Diagrama:
---------------------------
      ContaBancaria
---------------------------
# _id
# _titular
- __saldo
- __hash
+ @nome
---------------------------
+ validar_senha(chave)
+ pede_senha()
+ sacar(valor,chave)
+ depositar(valor)
---------------------------
'''
import hashlib
from pwinput import pwinput


class ContaBancaria:
    def __init__(self, id, titular, saldo=0.0, hash_senha=None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo

        # Se passou uma senha na criação, faz o hash. Se não, pede o texto e faz o hash.
        if hash_senha is not None:
            self.__hash = hashlib.sha256(str(hash_senha).encode("utf-8")).hexdigest()
        else:
            senha_pura = self.pede_senha()
            self.__hash = hashlib.sha256(senha_pura.encode("utf-8")).hexdigest()

        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:.2f}")

    # --- PROPRIEDADE NOME ---

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome):
        if self.validar_senha(self.pede_senha()):
            self._titular = novo_nome
            print(f"✅ Nome alterado para {self._titular}")
        else:
            print("❌ Senha incorreta. Não foi possível alterar o nome.")

    # --- MÉTODOS DO DIAGRAMA ---

    def pede_senha(self) -> str:
        return pwinput(prompt="Senha: ", mask="*")

    def validar_senha(self, chave: str) -> bool:
        if not chave or not isinstance(chave, str):
            return False
        chave_hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()
        return self.__hash == chave_hash

    def sacar(self, valor: float, chave: str = None):
        senha_digitada = chave if chave is not None else self.pede_senha()

        if not self.validar_senha(senha_digitada):
            print("❌ Senha incorreta! Operação de saque cancelada.")
            return False

        if valor <= 0:
            print("❌ Valor de saque inválido.")
            return False

        if valor > self.__saldo:
            print("❌ Saldo insuficiente.")
            return False

        self.__saldo -= valor
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.__saldo:.2f}")
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            print("❌ Valor de depósito inválido.")
            return False

        self.__saldo += valor
        print(f"✅ Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.__saldo:.2f}")
        return True