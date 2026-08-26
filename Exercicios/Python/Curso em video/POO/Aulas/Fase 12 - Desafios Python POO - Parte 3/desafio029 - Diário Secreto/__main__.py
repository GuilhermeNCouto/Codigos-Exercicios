'''
Simule um diário secreto orientado a objetos.
'''
from diario import Diario
from rich import inspect

def main():
    d = Diario("Cafeina")
    
    
    d.escrever("Primeiramensagem")
    d.escrever("Olá, mundo!")
    d.escrever("Terceira mensagem")
    
    #inspect(d, private=True, methods=True)

    try:
        print(d.senha)
    except PermissionError as e:
        print(e)

    try:
        d.ler("Cafeina")
    except PermissionError as e:
        print(e)

    try:
        d.senha = "Livros"
    except PermissionError as e:
        print(e)

if __name__ == '__main__':
    main()