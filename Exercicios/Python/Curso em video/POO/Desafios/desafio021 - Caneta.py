'''
Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
podendo escrever frases na cor relativa.
'''

from rich import print
from rich.panel import Panel

class Caneta:
    def __init__(self, cor="default"):
        cores = dict(azul="blue", vermelha="red", verde="green")
        self.cor = cores.get(cor, "default")
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, frase):
        if not self.tampada:
            print(f"[{self.cor}]{frase}[/]", end=" ")
        else:
            print("A caneta está tampada!")

    def quebrar_linha(self, num_linhas):
        for linha in range(num_linhas):
            print("")
c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar() 
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")
