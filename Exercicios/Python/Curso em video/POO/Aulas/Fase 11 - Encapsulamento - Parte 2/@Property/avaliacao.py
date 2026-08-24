class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self.nota = nota # ✅ Passa pelo @nota.setter e valida já na inicialização!
    
    #Criando atributo validável
    @property
    def nota(self):
        return self._nota #getter
    
    @nota.setter
    def nota(self, nota): #setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")
       