from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/"lorem.txt", "r") as arquivo: # Utilizando o with para garantir que se feche sozinho
        print(arquivo.read(), end="\n\n") # Imprime todo o conteúdo do arquivo como uma única string

except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}") # Imprime uma mensagem de erro personalizada

try:
    with open(ROOT_PATH/"utf-8.txt", 'w', encoding="utf-8" ) as arquivo:
        arquivo.write('Arquivo com encoding.')
except IOError as exc:
    pass

