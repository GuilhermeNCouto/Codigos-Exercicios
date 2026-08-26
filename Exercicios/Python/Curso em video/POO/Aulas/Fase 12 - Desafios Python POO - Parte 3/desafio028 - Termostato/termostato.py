'''
Diagrama de classe:
Termostato
----------
- __temperatura
+ @temperatura : permite alterar a temperatura (com validação)
+ ftemperatura : retorna a temperatura formatada
'''

class Termostato():
    
    def __init__(self, temperatura=24):
        self.temperatura = temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        # Arredonda para 0.5 e trava no intervalo [16.0, 30.0]
        valor_arredondado = round(float(valor) * 2) / 2
        self.__temperatura = max(16.0, min(valor_arredondado, 30.0))
    
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"