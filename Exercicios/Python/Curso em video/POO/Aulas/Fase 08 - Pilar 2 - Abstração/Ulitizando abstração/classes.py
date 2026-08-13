from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        
    @abstractmethod
    def estudar(self):
        pass
    
    
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"Aluno {self.nome} matriculado com sucesso!")

    def estudar(self):
        print(f"Aluno {self.nome} está estudando {self.curso} na turma {self.turma}.")
        
        

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Professor {self.nome} está dando aula de {self.especialidade}.")
    
    def estudar(self):
        print(f"Professor {self.nome} está estudando para aprimorar seus conhecimentos.")
    
    
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"Funcionário {self.nome} bateu o ponto.")
        
    def estudar(self):
        print(f"Funcionário {self.nome} está estudando para melhorar suas habilidades no trabalho.")
    
  