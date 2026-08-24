'''
--------Superclasse-------
BebidaQuente {abstract}
--------------------------
--------------------------
+ preparar()
+ ferver_agua()
+ misturar() {abstract}
+ servir() {abstract}
--------------------------

--------Subclasses--------
Café
Chá
Leite
--------------------------
'''


from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.text import Text


class BebidaQuente(ABC):

    def preparar(self):
        conteudo = Text()
        
        # Linha inicial antes dos passos
        conteudo.append("☕ Iniciando o preparo...\n\n", style="bold yellow")

        conteudo.append("🔥 1. ", style="bold yellow")
        conteudo.append(f"{self.ferver_agua()}\n")

        conteudo.append("🌀 2. ", style="bold cyan")
        conteudo.append(f"{self.misturar()}\n")

        conteudo.append("☕ 3. ", style="bold magenta")
        conteudo.append(f"{self.servir()}\n\n")

        conteudo.append("✨ Bebida pronta!", style="bold green")

        painel = Panel(
            conteudo,
            title=f"[bold white on blue] ☕ {self.__class__.__name__} [/]",
            border_style="bright_blue",
            padding=(1, 2),
            width=65,
        )

        print(painel)

    def ferver_agua(self):
        return "Fervendo água a 100° C."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass
    
    
class Cafe(BebidaQuente):
    def misturar(self):
        return "Passando água pressurizada pelo pó de café moído."

    def servir(self):
        return "Servindo o café na xícara."

class Cha(BebidaQuente):
    def misturar(self):
        return "Megulhando o sachê de ervas na água."

    def servir(self):
        return "Servindo o chá na caneca de porcelana."
    
class Leite(BebidaQuente):
    def misturar(self):
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "Servindo o leite na caneca grande, já com café."