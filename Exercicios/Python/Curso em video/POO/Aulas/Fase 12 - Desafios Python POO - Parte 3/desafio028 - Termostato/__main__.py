'''
Implemente um termostato orientado a objetos.
'''
from termostato import Termostato
from rich import inspect

def main():
    t = Termostato()
    
    t.temperatura = 18.5
    
    inspect(t, private=True, methods=True)
    
    print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == '__main__':
    main()