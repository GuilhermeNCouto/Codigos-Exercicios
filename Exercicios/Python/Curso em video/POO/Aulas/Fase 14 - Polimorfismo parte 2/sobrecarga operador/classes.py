class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self) -> str:
        return f"Você tem R${self.saldo:,.2f} na carteira."
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Não é permitido alterar o saldo dessa maneira.")

    def __eq__(self, other):
        return True if self.__saldo == other.__saldo else False

    def __iadd__(self, valor:int|float):
        self.__saldo += valor
        return self

    def __isub__(self, valor:int|float):
        self.__saldo -= valor
        return self

    def __le__(self, other):
        return True if self.__saldo <= other.__saldo else False
