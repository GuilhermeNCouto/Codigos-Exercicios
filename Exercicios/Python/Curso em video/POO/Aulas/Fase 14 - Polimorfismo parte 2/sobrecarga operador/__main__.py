from classes import *

def main():

    c1 = Carteira(180)
    c2 = Carteira(100)

    print(c1 == c2)

    c1 += 50
    c1 -= 20

    print(c1)

    print(c1 <= c2)

if __name__ == '__main__':
    main()