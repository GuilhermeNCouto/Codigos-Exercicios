'''
Crie a estrutura capaz de calcular salários de funcionários diferentes.
'''

from funcionarios import Horista, Mensalista

def main():
    f1 = Horista('João', 20, 160)
    f1.calc_sal()
    f1.analisar_sal()
    
    f2 = Mensalista('Maria', 6000)
    f2.calc_sal()
    f2.analisar_sal()
    
    
if __name__ == '__main__':
    main()
    