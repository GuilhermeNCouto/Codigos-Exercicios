'''
Simule o sistema de batalha entre personagens de um RPG.
'''
from personagens import Guerreiro, Mago

def __main__():
    
    p1 = Guerreiro('Arus', 1000)
    p2 = Mago('Jenica', 500)

    p1.atacar(p2, 550)
    
    p2.curar()
    
    p2.atacar(p1, 800)
    
    p1.curar()
    
    p2.atacar(p1, 800)
    p2.atacar(p1, 800)
    
if __name__ == '__main__':
    __main__()