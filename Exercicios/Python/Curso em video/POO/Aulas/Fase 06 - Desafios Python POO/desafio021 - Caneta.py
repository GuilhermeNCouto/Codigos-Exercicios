'''
Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
podendo escrever frases na cor relativa.
'''

from rich import print
from rich.panel import Panel

class Caneta:
    
    MAPA_CORES = {
        "azul": "blue",
        "vermelha": "red",
        "vermelho": "red",
        "verde": "green"
    }
    
    def __init__(self, cor="default"):
        self.cor = self.MAPA_CORES.get(cor.lower().strip(), "default")
        self.tampada = True

    def destampar(self):
        self.tampada = False
        
    def tampar(self):
        self.tampada = True

    def escrever(self, frase):
        if not self.tampada:
            print(f"[{self.cor}]{frase}[/]", end=" ")
        else:
            print(f":prohibited: [{self.cor}]caneta[/] está tampada!")

    def quebrar_linha(self, num_linhas):
        print("\n" * num_linhas, end="")
            
            
c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar() 
c2.destampar()
c3.destampar()

c1.escrever("Vamos nessa!")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")
