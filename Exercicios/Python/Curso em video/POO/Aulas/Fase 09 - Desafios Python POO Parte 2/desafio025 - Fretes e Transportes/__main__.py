'''
Crie classes capazes de calcular fretes de veículos diferentes.
'''

from fretes import Moto, Caminhao, Drone
from rich import print

def main():
    dist = 80
    entrega = Drone(dist)
    
    print(f"Frete de [yellow]{type(entrega).__name__}[/] em [blue]{dist}Km[/]: [green]{entrega.calc_frete()}[/]")

if __name__ == '__main__':
    main()
