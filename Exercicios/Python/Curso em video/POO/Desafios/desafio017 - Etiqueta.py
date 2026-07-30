'''
Crie a classe Produto, onde podemos cadastrar nome e preço.
Crie também um método que mostre a etiqueta do produto com o nome centralizado e o preço formatado.
'''
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precoFormatado = f"R$ {self.preco:,.2f}"
        # Adiciona o sinal de "R$" e formata o preço
        conteudo += f"{precoFormatado.center(30, '.')}"
        
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)

# Testando a classe
p1 = Produto("Notebook", 2500.00)
p2 = Produto("Smartphone", 1500.00)

p1.etiqueta()
p2.etiqueta()