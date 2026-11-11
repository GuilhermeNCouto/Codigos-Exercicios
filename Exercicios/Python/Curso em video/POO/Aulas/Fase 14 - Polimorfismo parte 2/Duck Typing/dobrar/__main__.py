from classes import *

def main():

    numero = Numero(350)
    texto = Texto("Guigas.bet")
    lista = Lista([3,4,5])
    papel = Papel()
    casa = Casa()

    tente_dobrar(numero)
    tente_dobrar(texto)
    tente_dobrar(lista)
    tente_dobrar(papel)
    tente_dobrar(casa)

    print(numero)
    print(texto)
    print(lista)
    print(papel)
    print(casa)

if __name__ == '__main__':
    main()