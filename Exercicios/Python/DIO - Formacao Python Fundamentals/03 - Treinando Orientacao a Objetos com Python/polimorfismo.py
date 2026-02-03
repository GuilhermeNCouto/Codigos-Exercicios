class Passaro:
    def voar(self): 
        print("Voando...")

class Pardal(Passaro):
    pass

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")

def plano_de_voo(objeto_passaro):
    objeto_passaro.voar()



plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())

