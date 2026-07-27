'''
Crie a classe Churrasco, onde seja possível informar quantas pessoas
vão particilar e mostre quanto de carne deve ser comprado, o custo
total do churrasco e o preço por pessoa.

Consumo padrão: 400g de carne por pessoa
Preço: R$ 82,40/kg
'''
from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome, num_pessoas):
        self.nome = nome
        self.num_pessoas = num_pessoas
        self.consumo_padrao = 400  # em gramas
        self.preco_kg = 82.40  # em reais

    def analisar(self):
        # Calcular a quantidade total de carne necessária
        carne_necessaria = self.num_pessoas * self.consumo_padrao / 1000  # convertendo para kg
        
        # Calcular o custo total do churrasco
        custo_total = carne_necessaria * self.preco_kg

        # Calcular o preço por pessoa
        preco_por_pessoa = custo_total / self.num_pessoas

        # Exibir os resultados
        conteudo = (
            f"Analisando [green]{self.nome}[/] com [blue]{self.num_pessoas} convidados[/]\n"
            f"Cada participante comera {self.consumo_padrao}g e cada Kg custa R$ {self.preco_kg:.2f}\n"
            f"Recomendo [blue]comprar {carne_necessaria:.2f}[/]kg de carne\n"
            f"O custo total será de [green]R$ {custo_total:.2f}[/]\n"
            f"Cada pessoa pagará [yellow]R$ {preco_por_pessoa:.2f}[/] para participar."
        )

        print(Panel(conteudo, title="Análise do Churrasco", width=60))


c1 = Churrasco("Churrasco de Aniversário", 10)
c1.analisar()
