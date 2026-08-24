'''
Diagrama:
Retangulo
----------
# _base
# _altura
# _area
+ @base
+ @altura
+ @area
+ @medidas
'''

class Retangulo:

    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        self._area = None

    # Base
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor < 1:
            raise ValueError("Valor inválido para a base.")
        self._base = valor
        self._area = None  # Invalida o cache/reseta para None quando as medidas mudam

    # Altura
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor < 1:
            raise ValueError("Valor inválido para a altura.")
        self._altura = valor
        self._area = None  # Invalida o cache/reseta para None quando as medidas mudam

    # Área
    @property
    def area(self):
        # Calcula sob demanda multiplicando base por altura
        return self._base * self._altura

    @area.setter
    def area(self, valor):
        raise AttributeError(
            "A área não pode ser definida manualmente, ela é calculada automaticamente."
        )

    # Medidas
    @property
    def medidas(self):
        return f"Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores):
        base, altura = valores
        self.base = base
        self.altura = altura