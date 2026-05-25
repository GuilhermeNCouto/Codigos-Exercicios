from pathlib import Path

ROOT_PATH = Path(__file__).parent

arquivo = open(ROOT_PATH/"lorem.txt", "r")
arquivo.close()

print(arquivo.read())
