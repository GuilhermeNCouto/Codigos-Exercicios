from classes import *

def main():

    a1 = DOCX("Prova", 256_000)
    a2 = PDF("Contrato", 1_512_000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)

    print(a1.nome_completo)
    print(a2.nome_completo)

if __name__ == '__main__':
    main()