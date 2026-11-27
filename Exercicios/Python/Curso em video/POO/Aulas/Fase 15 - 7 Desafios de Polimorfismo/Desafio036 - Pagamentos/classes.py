from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor: float = 0.0):
        self.valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._valor = float(novo_valor)

    @property
    def fvalor(self) -> str:
        formatado = f"{self.valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {formatado}"

    @abstractmethod
    def pagar(self, quantia: float) -> float:
        pass


class Boleto(Pagamento):
    def pagar(self, quantia: float) -> float:
        self.valor = quantia
        return self.valor


class Credito(Pagamento):
    def pagar(self, quantia: float) -> float:
        self.valor = quantia
        return self.valor


class Pix(Pagamento):
    def pagar(self, quantia: float) -> float:
        self.valor = quantia
        return self.valor


def finalizar_compra(tipo: Pagamento, quantia: float) -> None:
    tipo.pagar(quantia)
    print(f"Pagamento CONFIRMADO de {tipo.fvalor} via {tipo.__class__.__name__}")