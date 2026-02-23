class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("O motor foi ligado.")

    def __str__(self):
        return "\n".join([f"{k.upper():>15}: {v}" for k, v in vars(self).items()])

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"O caminhão está {'carregado' if self.carregado else 'vazio'}.")










'''
moto = Motocicleta("Vermelha", "XYZ-1234", 2)
moto.ligar_motor()

carro = Carro("Azul", "ABC-5678", 4)
carro.ligar_motor()
'''


caminhao = Caminhao("Branco", "DEF-9012", 6, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)