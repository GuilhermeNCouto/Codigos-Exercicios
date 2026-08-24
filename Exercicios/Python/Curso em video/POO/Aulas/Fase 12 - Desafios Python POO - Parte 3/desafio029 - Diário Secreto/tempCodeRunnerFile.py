'''
Simule um diário secreto orientado a objetos.
'''
from diario import Diario
from rich import inspect

def main():
    d = Diario("Cafeina")
    
    
    d.escrever("Primeiramensagem")
    #d.escrever("Olá, mundo!")
    #d.escrever("Terceira mensagem")
    inspect(d)

if __name__ == '__main__':
    main()