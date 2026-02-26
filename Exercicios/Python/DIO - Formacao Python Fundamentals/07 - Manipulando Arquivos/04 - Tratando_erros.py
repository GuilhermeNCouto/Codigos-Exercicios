from pathlib import Path

ROOT_PATH = Path(__file__).parent # Obtém o caminho do diretório onde o arquivo está localizado

try:
    arquivo = open("meuarquivo.py") # Tenta abrir um arquivo que não existe
except FileNotFoundError as exc: # Captura a exceção FileNotFoundError e armazena a mensagem de erro na variável exc
    print("Arquivo não encontrado!") # Imprime uma mensagem de erro personalizada
    print(exc) # Imprime a mensagem de erro original, que inclui detalhes sobre o erro, como o tipo de exceção e a mensagem associada
except IsADirectoryError as exc: # Captura a exceção IsADirectoryError e armazena a mensagem de erro na variável exc
    print("O caminho especificado é um diretório, não um arquivo!") # Imprime uma mensagem de erro personalizada
    print(exc) # Imprime a mensagem de erro original, que inclui detalhes sobre o erro, como o tipo de exceção e a mensagem associada
except IOError as exc: # Captura qualquer outra exceção relacionada a entrada/saída e armazena a mensagem de erro na variável exc
    print(f"Erro ao abrir o arquivo {exc.filename}!") # Imprime uma mensagem de erro personalizada
    print(exc) # Imprime a mensagem de erro original, que inclui detalhes sobre o erro, como o tipo de exceção e a mensagem associada
except Exception as exc: # Captura qualquer outra exceção genérica e armazena a mensagem de erro na variável exc
    print("Ocorreu um erro inesperado!") # Imprime uma mensagem de erro personalizada
    print(exc) # Imprime a mensagem de erro original, que inclui detalhes sobre o erro, como o tipo de exceção e a mensagem associada

'''try:
    arquivo = open(ROOT_PATH / "Novo_diretorio") # Tenta abrir um diretório como se fosse um arquivo, o que gera uma exceção IsADirectoryError
except IsADirectoryError as exc: # Captura a exceção IsADirectoryError e armazena a mensagem de erro na variável exc
    print("O caminho especificado é um diretório, não um arquivo!") # Imprime uma mensagem de erro personalizada
    print(exc) # Imprime a mensagem de erro original, que inclui detalhes sobre o erro, como o tipo de exceção e a mensagem associada
'''