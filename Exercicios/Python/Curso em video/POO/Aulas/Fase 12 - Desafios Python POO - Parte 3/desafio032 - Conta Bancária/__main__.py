'''
Aprimore o exercício da ContaBancaria, aplicando
conceitos de encapsulamento.
'''
from contabancaria import ContaBancaria
from rich import print, inspect

def main():
    print("Criando a conta...")

    # 1. Ao instanciar, ele vai pedir a criação da senha mascarada com '*****'
    conta = ContaBancaria(101, "Carlos", 1000.0)


    
    print("\n--- Realizando Depósito ---")
    conta.depositar(350.0)

    print("\n--- Realizando Saque ---")
    # Não precisa passar a senha aqui, a própria classe solicita via pwinput
    conta.sacar(200.0)

    print("\n--- Alterando Nome ---")
    conta.nome = input("Novo nome: ")
    
    inspect(conta, private=True, methods=True)
    
if __name__ == '__main__':
    main()