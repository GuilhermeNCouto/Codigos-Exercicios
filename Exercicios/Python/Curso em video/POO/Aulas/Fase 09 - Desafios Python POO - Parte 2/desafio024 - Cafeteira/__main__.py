'''
Simule uma cafeteria orientada a objetos.
'''
from rich import print
from cafeteria import Cafe, Cha, Leite


def main():
    bebida1 = Cafe()
    bebida1.preparar()
    print()
    bebida2 = Cha()
    bebida2.preparar()
    print()
    bebida3 = Leite()
    bebida3.preparar()


if __name__ == '__main__':
    main()
    