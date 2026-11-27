"""
Crie classes para validadores de dados,
com os exemplos a seguir.


Validador {abstract}
--------------------
--------------------
+ validar()
--------------------


Subsclasses:

Usuário:
    - de 5 a 20 caracteres
    - Letras minúsculas
    - Números
    - Símbolo de sublinhado

Senha:
    - Minimo de 8 caracteres
    - Ao menos uma letra maiúscula
    - Ao menos um símbolo

Email:
    - Apenas uma @
    - Usuário pode conter letras, números e alguns símbolos
    - Os domínios contêm pontos
    - O TLD encerra com ponto e pelo menos 2 letras
"""