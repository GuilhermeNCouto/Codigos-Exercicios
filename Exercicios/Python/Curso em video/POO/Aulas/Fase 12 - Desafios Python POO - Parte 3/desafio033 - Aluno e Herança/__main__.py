from pessoa import Aluno
from rich import print, inspect

def main():

    a1 = Aluno("Guilherme", 2002, "ADS")

    a1.add_curso("MKT")

    a1.curso = "MKT"

    inspect(a1, private=True, methods=True)
    
    
if __name__ == '__main__':
    main()