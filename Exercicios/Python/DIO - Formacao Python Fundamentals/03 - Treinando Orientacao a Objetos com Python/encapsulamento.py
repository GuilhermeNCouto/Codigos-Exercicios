class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia # PUBLICO: Livre acesso
        self._limite = 500             # PROTECTED: Avisa "não mexa", mas permite acesso
        self.__saldo = saldo           # PRIVATE: O Python "esconde" (Name Mangling)


    def depositar(self, valor):
        # Uso interno do atributo privado
        self.__saldo += valor

    def sacar(self, valor):
        # Exemplo de uso de MÉTODO privado para validar a operação
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente.")

    # MÉTODO PRIVADO: Só faz sentido dentro da classe Conta
    def __pode_sacar(self, valor):
        return self.__saldo >= valor

    def mostrar_saldo(self):
        return self.__saldo

# --- Testando o comportamento ---

conta = Conta("0001", 100)

# 1. Acesso ao Público: OK
print(f"Agência: {conta.nro_agencia}")

# 2. Tentativa de acesso ao Privado: ERRO
try:
    print(conta.__saldo) 
except AttributeError:
    print("Erro: Não é possível acessar '__saldo' diretamente. Ele é privado!")

# 3. O jeito certo: Via método público
print(f"Saldo atual: {conta.mostrar_saldo()}")