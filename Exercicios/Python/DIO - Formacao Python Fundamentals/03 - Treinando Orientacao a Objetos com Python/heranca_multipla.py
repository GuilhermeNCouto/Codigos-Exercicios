class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return "\n".join([f"{k.upper():>15}: {v}" for k, v in vars(self).items()])


class Mamifero(Animal):
    def __init__(self, cor_pelo="Indefinida", **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico="Indefinida", **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass



class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.mro())
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)
        



#gato = Gato(nro_patas=4, cor_pelo="Laranja")
#print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="Marrom", cor_bico="Preto")
print(ornitorrinco)
