'''
Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle
simples:

canal = "< e >"
volume = "+ e -"
liga/desliga = "@"
'''

from rich import print
from rich.panel import Panel

class ControleRemoto:
    
    def __init__(self):
        self.canal = 1
        self.volume = 5
        self.ligado = True
        return self.liga_desliga()

    def liga_desliga(self):
        if self.ligado:
            self.ligado = False
            print(Panel(":prohibited:[red] A TV está desligada![/]", title="[ TV ]", width=30))
        else:
            self.ligado = True
            print(Panel(":tv:[green] A TV está ligada![/]", title="[ TV ]", width=30))

    def tela(self):
        tela = panel(f"[blue]Canal: {self.canal}[/]\n[green]Volume: {self.volume}[/]", title="[ TV ]", width=30)

controle = ControleRemoto()
