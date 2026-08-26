'''
Implemente a seguinte estrutura de diagrama de classes.

----------------------------
    Pessoa {absctract}
----------------------------
# _nome
# _nascimento
+ @Nascimento
+ @idade
----------------------------
----------------------------

----------------------------
       ALuno(Pessoa)
----------------------------
+ cursos_oficiais
# _curso
+ @curso
----------------------------
+ add_curso(curso)
----------------------------
'''
from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):

    ano_atual = datetime.now().year


    def __init__(self, nome, nascimento):
        self._nome = nome
        self.nascimento = nascimento
        
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, valor):
        if not (1910 <= valor <= self.ano_atual):
            raise ValueError(f"Ano {valor} é inválido.")
        self._nascimento = valor
    
    @property
    def idade(self):
        return self.ano_atual - self._nascimento
    
    @idade.setter
    def idade(self, valor):
        raise PermissionError("Não é possível alterar a idade. Mude o ano de nascimento.")


class Aluno(Pessoa):

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
        self.curso = curso


    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, valor):
        if valor not in self.cursos_oficiais:
            raise ValueError(f"{valor} não é um curso oficial.")
        self._curso = valor
        
    def add_curso(self, curso):
        if curso in self.cursos_oficiais:
            raise ValueError(f"{curso} já é um curso oficial.")
        self.cursos_oficiais.append(curso.upper())