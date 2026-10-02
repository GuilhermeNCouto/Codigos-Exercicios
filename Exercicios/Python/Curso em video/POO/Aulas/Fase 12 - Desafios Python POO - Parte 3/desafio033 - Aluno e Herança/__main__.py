from pessoa import Aluno
from rich import print, inspect

def main():

    a1 = Aluno("Guilherme", 2002, "ADS")

    print(a1.idade)

    inspect(a1, private=True, methods=True)
    
    
if __name__ == '__main__':
    main()