from classes import *

def main():
    
    p1 = Mae("Marta")
    p2 = Filha("Joana")
    p3 = Filho("Pedrinho")

    p1.fazer_pudim()
    p1.fritar_coxinha()

    p2.fazer_pudim()
    p2.fritar_coxinha()

    p3.fazer_pudim()
    p3.fritar_coxinha()
    
if __name__ == '__main__':
    main()