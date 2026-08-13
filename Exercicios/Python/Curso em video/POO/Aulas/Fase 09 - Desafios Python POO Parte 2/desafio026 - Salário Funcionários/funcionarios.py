'''
-------Superclasse-------
Funcionario {abstract}
-------------------------
+ nome
+ salario_bruto
+ salario_liquido
+ sal_min = 1612
+ inss = 7.5
-------------------------
+ calc_sal() {abstract}
+ analisar_sal()
-------------------------

-------Subclasses--------

Horista
-------------------------
+ valor_hora
+ horas_trabalhadas
-------------------------
+ calc_sal()
-------------------------

Mensalista
-------------------------
-------------------------
+ calc_sal()
'''
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.text import Text


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario_liquido = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        # Garante que o salário seja calculado antes da análise
        self.calc_sal()

        # Calcula a equivalência em salários mínimos
        qtd_sal_min = self.salario_liquido / self.sal_min


        # Monta a mensagem formatada
        mensagem = (
            f"O salário de [bold yellow]{self.nome}[/] ([cyan]{self.__class__.__name__}[/]) "
            f"é de [bold green]R$ {self.salario_liquido:.2f}[/] e corresponde a "
            f"[bold magenta]{qtd_sal_min:.1f} salários mínimos[/]."
        )

        painel = Panel(
            mensagem,
            title=" Análise de Salário ",
            width=55,
        )

        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calc_sal(self):
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
        self.salario_liquido = self.salario_bruto - (self.salario_bruto * (self.inss / 100))


class Mensalista(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calc_sal(self):
        self.salario_bruto = self.salario_mensal
        self.salario_liquido = self.salario_bruto - (self.salario_bruto * (self.inss / 100))