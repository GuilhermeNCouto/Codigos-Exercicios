'''
Implemente um programa que calcule a área e o perímetro de polígonos.
'''

from rich import print
from poligonos import Quadrado, Triangulo

def main():
    
    p1 = Quadrado(12)

    print(f"Perímetro do quadrado: {p1.perimetro():.1f}")
    print(f"Área do quadrado: {p1.area():.1f}")


    p2 = Triangulo(10, 5)
    print(f"Perímetro do triângulo: {p2.perimetro():.1f}")
    print(f"Área do triângulo: {p2.area():.1f}")


if __name__ == '__main__':
    main()