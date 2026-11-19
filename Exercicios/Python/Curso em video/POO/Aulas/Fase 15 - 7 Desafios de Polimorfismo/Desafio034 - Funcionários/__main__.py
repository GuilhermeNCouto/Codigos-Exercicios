from classes import *
from rich import inspect

def main():

    dev = Desenvolvedor("Guigas", 3000)
    #dev.salario = 2500
    print(dev)

    des = Designer("Matheus", 2000)
    print(des)

    ger = Gerente("Thau", 5000)
    print(ger)

    inspect(ger, methods=True, private=True)
    inspect(des, methods=True, private=True)
    inspect(dev, methods=True , private=True)


if __name__ == '__main__':
    main()