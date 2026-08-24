'''
Simule uma cafeteria orientada a objetos.

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
from rich import print
from cafeteria import Cafe


def main():
    bebida1 = Cafe()
    bebida1.preparar()
#    print()
#    bebida2 = Cha()
#    bebida2.preparar()
#    print()
#    bebida3 = Leite()
#    bebida3.preparar()


if __name__ == '__main__':
    main()
    