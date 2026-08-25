from pessoa import Pessoa
from rich import print, inspect

def main():
    
    a1 = Pessoa("Guilherme", 2002)
    
    inspect(a1, private=True, methods=True)
    
if __name__ == '__main__':
    main()