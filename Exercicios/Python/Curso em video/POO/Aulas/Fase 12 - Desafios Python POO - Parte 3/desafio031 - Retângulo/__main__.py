'''
Crie uma classe que represente um retângulo
pelas suas medidas e área.
'''
from retangulo import Retangulo
from rich import print, inspect

def main():
    r = Retangulo(15, 15)
    
    try:
        r.base = 25
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    try:
        r.altura = -5
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    
    
    
    r.medidas = (9,3)
    
    #inspect(r, private=True, methods=True)
    
    print(r.medidas)
    
if __name__ == '__main__':
    main()