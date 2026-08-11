from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario  
    
aluno1 = Aluno("João", 20, "Engenharia", "A")
aluno1.fazer_aniversario()
aluno1.fazer_matricula()

professor1 = Professor("Maicon", 35, "Matemática", "Doutorado")
professor1.dar_aula()

funcionario1 = Funcionario("Carlos", 28, "Secretário", "Secretaria")
funcionario1.bater_ponto()
