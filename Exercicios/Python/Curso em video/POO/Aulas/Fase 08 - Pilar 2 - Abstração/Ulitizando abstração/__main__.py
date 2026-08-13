from rich import print, inspect
from classes import Aluno, Professor, Funcionario
    
def main():
    aluno1 = Aluno("João", 20, "Engenharia", "A")
    aluno1.fazer_aniversario()
    aluno1.fazer_matricula()
    aluno1.estudar()

    print("\n")
    
    professor1 = Professor("Maicon", 35, "Matemática", "Doutorado")
    professor1.dar_aula()
    professor1.estudar()
    
    print("\n")

    funcionario1 = Funcionario("Carlos", 28, "Secretário", "Secretaria")
    funcionario1.bater_ponto()
    funcionario1.estudar()

if __name__ == "__main__":
    main()
    