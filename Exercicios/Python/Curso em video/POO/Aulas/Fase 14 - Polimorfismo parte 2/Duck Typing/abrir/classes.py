class Porta:

    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta.")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca e e separe as partes sobre uma frigideira.")

class Pedra:
    pass


#Metodo pythonico polimórfico Duck Typing
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Problema ao abrir objeto tipo {objeto.__class__.__name__}")


