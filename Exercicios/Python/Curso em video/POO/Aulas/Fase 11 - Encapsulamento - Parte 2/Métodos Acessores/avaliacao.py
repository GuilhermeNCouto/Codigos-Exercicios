class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo Protected (protegido #)
    
    # Métodos Acessores
    def get_nota(self): # Método Getter
        return self._nota
    
    def set_nota(self, nota): # Método Setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")