'''
Crie uma classe que represente um retângulo
pelas suas medidas e área.
'''
from retangulo import Retangulo
from rich import print, inspect

def main():
    r = Retangulo()
    
    r.altura = 10
    r.base = 5
    
    r.medidas = (9,3)
    
    #inspect(r, private=True, methods=True)
    
    print(r.medidas)
    
if __name__ == '__main__':
    main()