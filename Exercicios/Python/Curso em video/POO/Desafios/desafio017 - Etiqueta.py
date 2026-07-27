from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        # Formatando o preço no padrão clássico antes de aplicar os pontos
        p_str = f"R$ {self.preco:,.2f}"
        
        conteudo = (
            f"{self.nome:^36}\n"
            f"{'-' * 36}\n"
            f"{p_str:.^36}"
        )
        
        print(Panel(conteudo, title="Produto", width=40))

# Testando a classe
p1 = Produto("Notebook", 2500.00)
p2 = Produto("Smartphone", 1500.00)

p1.etiqueta()
p2.etiqueta()