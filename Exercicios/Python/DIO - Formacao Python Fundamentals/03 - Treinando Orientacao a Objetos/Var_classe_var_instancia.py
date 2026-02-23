class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


a1 = Estudante("Guilherme", 56451)
a2 = Estudante("Leticia", 17323)

print(a1)
print(a2)
Estudante.escola = "DIO - Digital Innovation One"
a3 = Estudante("André", 99876)
print(a1)
print(a2)
print(a3)
a1.escola = "Outra Escola"
print(a1)
print(a2)
print(a3)
