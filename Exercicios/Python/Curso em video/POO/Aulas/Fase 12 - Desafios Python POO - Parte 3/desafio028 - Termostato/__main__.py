'''
Implemente um termostato orientado a objetos.

Temperatura ao ligar - 24°C
Temperatura mínima - 16°C
Temperatura máxima - 30°C
Deve-se alterar 0.5°C por clique/giro.
'''
from termostato import Termostato
from rich import inspect

def main():

    t = Termostato(18.2)
    
    inspect(t, private=True, methods=True)
    
    print(f"A temperatura atual é de {t.ftemperatura}")


if __name__ == '__main__':
    main()