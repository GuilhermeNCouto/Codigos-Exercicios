'''
Crie classes capazes de calcular fretes de veículos diferentes.
'''

from fretes import Moto, Caminhao, Drone
from rich import print
from rich.table import Table

def main():
    
    dist = int(input("Digite a distância da entrega (em Km): "))
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    #entrega = Caminhao(dist)
    #print(f"Frete de [yellow]{type(entrega).__name__}[/] em [blue]{dist}Km[/]: [green]{entrega.calc_frete()}[/]")

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Frete", justify="center")

    for tipo in viagem:
        tabela.add_row(
            f"[blue]{dist}Km[/]",
            f"[yellow]{type(tipo).__name__}[/]",
            f"[green]{tipo.calc_frete()}[/]"
        )
    
    print(tabela)

if __name__ == '__main__':
    main()
