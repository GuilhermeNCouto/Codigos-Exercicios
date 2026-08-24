'''
Termostato

Temperatura ao ligar - 24°C
Temperatura mínima - 16°C
Temperatura máxima - 30°C
Deve-se alterar 0.5°C por clique/giro.

Diagrama de classe:

Termostato
----------
- __temperatura
+ @temperatura : permite alterar a temperatura (com validação)
+ ftemperatura : retorna a temperatura formatada
'''

class Termostato():
    
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura % 0.5 != 0:
            raise ValueError(f"Temperatura de {temperatura} é inválida!")
        
        if temperatura < 16:
            self.__temperatura = 16
        elif temperatura > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura
    
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"