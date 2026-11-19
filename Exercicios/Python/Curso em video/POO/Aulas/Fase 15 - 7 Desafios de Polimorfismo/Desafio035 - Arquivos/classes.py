"""
Crie um simulador que gerencia a abertura de diferentes tipos de arquivos.

Classe principal:
Arquivo {abstract}
-----------------
+ nome
# _extensao
+ tamanho
+ @nome_completo
-----------------
+ abrir()

Subclasses:
PDF
--------------

"""

from abc import ABC, abstractmethod

class Arquivo(ABC):

    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        pass

    @abstractmethod
    def abrir_arquivo(self):
        pass


class DOCX(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = ".docx"

    def abrir_arquivo(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Microsoft Word.')

    @property
    def nome_completo(self):
        return f'{self.nome}.docx ({self.tamanho / (1024 ** 2):.2f}MB)'

class PDF(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = ".pdf"

    def abrir_arquivo(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Acrobat Reader.')

    @property
    def nome_completo(self):
        return f'{self.nome}.pdf ({self.tamanho / (1024 ** 2):.2f}MB)'


def abrir_arquivo(arquivo):
    return arquivo.abrir_arquivo()