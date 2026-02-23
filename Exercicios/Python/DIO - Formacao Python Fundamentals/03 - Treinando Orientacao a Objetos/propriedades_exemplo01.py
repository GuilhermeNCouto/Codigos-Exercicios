class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        # Se o usuário passar None ou 0, podemos interpretar como um reset
        if value is None:
            self._x = 0
        else:
            # Garante que estamos somando números
            self._x = (self._x or 0) + (value or 0)

    @x.deleter
    def x(self):
        # Se alguém usar 'del', o código não quebra e reseta com segurança
        self._x = 0
        print("Aviso: O valor de x foi resetado via deleter.")

# --- Testando a robustez ---
foo = Foo(10)
print(foo.x)  # Saída: 10

foo.x = None    # Reset via Setter
print(foo.x)    # Saída: 0

foo.x = 20      # Soma normal
print(foo.x)    # Saída: 20
del foo.x       # Reset via Deleter (Evita o AttributeError)
print(foo.x)    # Saída: 0