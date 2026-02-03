import functools

'''Introspecção em Decoradores: É a capacidade de um objeto saber sobre
seus próprios atributos em tempo de execução. Em Python, isso é
facilitado por atributos especiais como __name__ e __doc__, que fornecem
informações sobre o nome e a documentação de funções e classes. Ao criar
decoradores, é importante preservar esses atributos para que a função
decorada mantenha suas propriedades originais. Isso pode ser feito usando
o módulo functools e o decorador @functools.wraps, que copia os
atributos da função original para a função decorada. Dessa forma, a
introspecção continua funcionando corretamente, permitindo que os
desenvolvedores acessem informações sobre a função decorada, como seu
nome e documentação, facilitando a depuração e a manutenção do código.
'''

def duplicar_resultado(func):
    '''
    Docstring para duplicar_resultado
    
    :param func: Função a ser decorada
    :return: Função decorada que duplica o resultado da função original
    '''
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return envelope

@duplicar_resultado
def aprender(tecnologia):
    """Função que imprime a tecnologia que está sendo aprendida."""
    print(f'Estou aprendendo {tecnologia}!')
    return tecnologia.upper()


tecnologia = aprender('Python')
print(tecnologia)  # Saída: PYTHON
print(aprender.__name__)  # Saída: aprender
print(aprender.__doc__)   # Saída: Função que imprime a tecnologia que está sendo aprendida.

