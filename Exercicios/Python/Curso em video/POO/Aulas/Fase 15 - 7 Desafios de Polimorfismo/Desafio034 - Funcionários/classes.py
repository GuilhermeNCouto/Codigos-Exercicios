"""
Crie a seguinte estrutura de classes para
calcular bônus salarial.

Diagrama de classe:
Funcionário {abstract}
----------------
+ nome
- salario
----------------
+ calcular_bonus()

Crie Gerente, Designer e Desenvolvedor (subclasses de Funcionário).
Vão possuir um % de bônus diferente, sendo 10% para dev, 8% para designer
e 15% para gerente.
"""
from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario  # Passa pelo @salario.setter na criação

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return (
            f"{self.nome} ganha R${self.salario:.2f}. "
            f"Seu bônus como {self.__class__.__name__} será de R${self.calcular_bonus():.2f}."
        )

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        if hasattr(self, "_Funcionario__salario") and novo_salario < self.__salario:
            raise ValueError("Você não pode reduzir o salário de um funcionário.")
        self.__salario = novo_salario


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15