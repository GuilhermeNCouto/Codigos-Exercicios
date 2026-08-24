'''
Crie uma classe que gerencie a hash SHA256 de uma senha.
'''
from criptografia import Credencial
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = input("Digite sua senha: ")
    
    inspect(c, private=True, methods=True)

    print(c.validar("teste"))
    
if __name__ == '__main__':
    main()