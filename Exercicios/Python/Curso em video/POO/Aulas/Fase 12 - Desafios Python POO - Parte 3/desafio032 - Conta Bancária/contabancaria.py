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


class ContaBancaria:
    def __init__(self, id, titular, saldo=0.0, hash_senha=None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo

        if hash_senha is not None:
            senha_str = str(hash_senha).strip()
            if len(senha_str) < 8:
                raise ValueError("A senha fornecida deve ter no mínimo 8 dígitos.")
            self.__hash = hashlib.sha256(senha_str.encode("utf-8")).hexdigest()
        else:
            senha_pura = self.pede_senha("Cadastre uma senha (mínimo 8 dígitos): ")
            self.__hash = hashlib.sha256(senha_pura.encode("utf-8")).hexdigest()

        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:.2f}")

    def __str__(self):
        return f"Conta {self._id}\nTitular: {self._titular}\nSaldo: R${self.__saldo:.2f}"


    # --- PROPRIEDADE NOME ---

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome):
        print("🔐 Confirme sua senha para alterar o nome:")
        # Usa exclusivamente pede_senha() para capturar a credencial
        if self.validar_senha(self.pede_senha("Senha atual: ")):
            self._titular = novo_nome
            print(f"✅ Nome alterado para {self._titular}")
        else:
            print("❌ Senha incorreta. Não foi possível alterar o nome.")

    # --- MÉTODOS ---

    def pede_senha(self, prompt: str = "Senha: ") -> str:
        """Centraliza o pwinput e valida o tamanho mínimo de 8 caracteres."""
        from pwinput import pwinput  # Import isolado exclusivamente aqui dentro

        while True:
            senha = pwinput(prompt=prompt, mask="*").strip()
            if len(senha) >= 8:
                return senha
            print("⚠️ Senha inválida! A senha precisa ter pelo menos 8 dígitos.")

    def validar_senha(self, chave: str) -> bool:
        if not chave or not isinstance(chave, str):
            return False
        chave_hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()
        return self.__hash == chave_hash

    def sacar(self, valor: float, chave: str = None):
        # Se não enviou chave via argumento, pede interativamente usando pede_senha()
        senha_digitada = chave if chave is not None else self.pede_senha("Senha para saque: ")

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