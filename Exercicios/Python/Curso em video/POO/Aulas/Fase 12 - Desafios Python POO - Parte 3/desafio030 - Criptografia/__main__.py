'''
Crie uma classe que gerencie a hash SHA256 de uma senha.
'''
from criptografia import Credencial
from rich import print, inspect

def main():

    c = Credencial()

    try:
        c.senha = input("Digite sua senha: ").strip()
    except ValueError as e:
        print(e)
        return

    #inspect(c, private=True, methods=True)

    try:
        print(c.senha)
    except PermissionError as e:
        print(e)


    print(c.validar(input('Confirme a senha: ').strip()))

    
if __name__ == '__main__':
    main()