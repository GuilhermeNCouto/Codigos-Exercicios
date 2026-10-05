class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} fez um PUDIM de leite condensado com calda")

    def fritar_coxinha(self):
        print(f"{self.nome} fritou uma COXINHA no óleo de soja")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} fez um PUDIM de Leite Ninho com Nutella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} fritou uma COXINHA na Air Fryer")