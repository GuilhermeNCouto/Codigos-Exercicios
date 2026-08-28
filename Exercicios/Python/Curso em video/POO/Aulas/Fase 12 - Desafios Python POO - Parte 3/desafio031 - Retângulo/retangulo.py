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

    def __init__(self, base=1, altura=1):
        self._area = None

        self.base = base
        self.altura = altura

    # Base
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Base deve ser um número.")
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
        if not isinstance(valor, (int, float)):
            raise TypeError("Altura deve ser um número.")
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
        raise PermissionError(
            "A área não pode ser definida manualmente, ela é calculada automaticamente."
        )

    # Medidas
    @property
    def medidas(self):
        return f"Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores):
        if not isinstance(valores, (tuple, list)) or len(valores) != 2:
            raise TypeError("Medidas deve ser uma tupla ou lista com 2 valores: (base, altura).")
        
        base, altura = valores
        self.base = base
        self.altura = altura