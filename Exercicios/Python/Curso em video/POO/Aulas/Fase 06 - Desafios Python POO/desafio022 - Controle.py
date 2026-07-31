'''
Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle
simples:

canal = "< e >"
volume = "+ e -"
liga/desliga = "@"
'''

import os
from readchar import readchar
from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False
    
    def liga_desliga(self):
        self.ligado = not self.ligado
    
    def aumentar_canal(self):
        if self.ligado:
            if self.canal_atual == self.__class__.canal_max:
                self.canal_atual = self.__class__.canal_min
            else:
                self.canal_atual += 1

    def diminuir_canal(self):
        if self.ligado:
            if self.canal_atual == self.__class__.canal_min:
                self.canal_atual = self.__class__.canal_max
            else:
                self.canal_atual -= 1
    
    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual != self.__class__.volume_max:
                self.volume_atual += 1
                
    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual != self.__class__.volume_min:
                self.volume_atual -= 1
            
    def mostrar_tv(self):
        if not self.ligado:
            conteudo = ":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f"{canal} "
                    
            conteudo += "\nVOLUME = " + "[black on red] [/]" * self.volume_atual + "[black on white] [/]" * (self.volume_max - self.volume_atual)
            
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)
        
controle = ControleRemoto()

while True:
    # Limpa o terminal antes de desenhar a TV (funciona no Windows e Linux/Codespaces)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    controle.mostrar_tv()
    
    print("\n[ @: Liga | <: Ch- | >: Ch+ | -: Vol- | +: Vol+ | 0: Sair ]\n")
    
    # Espera apenas 1 tecla e já joga direto para o match, sem pedir Enter!
    comando = readchar()
    
    match comando:
        case '0':
            break
        case '@':
            controle.liga_desliga()
        case '<':
            controle.diminuir_canal()
        case '>':
            controle.aumentar_canal()
        case '-':
            controle.diminuir_volume()
        case '+':
            controle.aumentar_volume()