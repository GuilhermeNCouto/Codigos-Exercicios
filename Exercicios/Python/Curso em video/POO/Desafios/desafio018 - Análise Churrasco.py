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
    
    #atributos da classe
    consumo_padrao = 400  # em gramas
    preco_kg = 82.40  # em reais
    
    
    def __init__(self, nome, num_pessoas):
        self.nome = nome
        self.num_pessoas = num_pessoas
        
    def __str__(self):
        return f"Este é o churrasco {self.nome} com {self.num_pessoas} convidados."


    def calcular_atd_carne(self) -> float:
        return self.num_pessoas * self.__class__.consumo_padrao / 1000  # convertendo para kg

    def calcular_custo_total(self) -> float:
        return self.calcular_atd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.num_pessoas
    
    def analisar(self):

        # Exibir os resultados
        conteudo = (
            f"Analisando [green]{self.nome}[/] com [blue]{self.num_pessoas} convidados[/]\n"
            f"Cada participante comera {self.__class__.consumo_padrao}g e cada Kg custa R$ {self.__class__.preco_kg:,.2f}\n"
            f"Recomendo [blue]comprar {self.calcular_atd_carne():,.2f}[/]kg de carne\n"
            f"O custo total será de [green]R$ {self.calcular_custo_total():,.2f}[/]\n"
            f"Cada pessoa pagará [yellow]R$ {self.calcular_custo_individual():,.2f}[/] para participar."
        )

        painel = Panel(conteudo, title="Análise do Churrasco", width=60)
        print(painel)

c1 = Churrasco("Churrasco de Aniversário", 15)
print(c1)
c1.analisar()
