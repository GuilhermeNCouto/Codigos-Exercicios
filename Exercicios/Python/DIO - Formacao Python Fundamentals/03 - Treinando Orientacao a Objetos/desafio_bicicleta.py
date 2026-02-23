class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=29):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro


    def __str__(self):
    # Criando uma string formatada diretamente do dicionário de atributos
        return "\n".join([f"{k.upper():>10}: {v}" for k, v in vars(self).items()])
    
    def buzinar(self):
        print("Buzina: plim plim!")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("A bicicleta está em movimento.")
    
    


'''
b1 = Bicicleta("Vermelha", "Mountain Bike", 2021, 1500.00)
print(f"Print direto do objeto bicicleta:\n{b1}\n")
print("Buzinando a bicicleta:")
b1.buzinar()
print("\nColocando a bicicleta em movimento:")
b1.correr()
print("\n")
b1.parar()
'''

b2 = Bicicleta("Azul", "Speed", 2020, 2500.00, aro=26)
print(b2)

