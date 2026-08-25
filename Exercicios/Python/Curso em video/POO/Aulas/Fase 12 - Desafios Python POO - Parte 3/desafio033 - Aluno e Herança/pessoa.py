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

class Pessoa():
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento
        
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, valor):
        self._nascimento = valor
        