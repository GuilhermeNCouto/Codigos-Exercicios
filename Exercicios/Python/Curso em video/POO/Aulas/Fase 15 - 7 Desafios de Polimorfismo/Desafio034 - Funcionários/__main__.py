from classes import *

def main():

    funcionarios = [
        Desenvolvedor("Guigas", 3000),
        Designer("Matheus", 2000),
        Gerente("Thau", 5000)
        ]

    try:
        funcionarios[0].salario = 2500
    except Exception as erro:
        print(f"ERRO: {erro}")

    for funcionario in funcionarios:
        print(funcionario)

if __name__ == '__main__':
    main()