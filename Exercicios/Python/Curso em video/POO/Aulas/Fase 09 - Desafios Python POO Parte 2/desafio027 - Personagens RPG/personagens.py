'''
-------Superclasse-------
Personagem {abstract}
-------------------------
+ nome
+ vida
+ golpes
-------------------------
+ atacar(alvo, forca)
+ receber_dano(dano)
+ curar() abstract
-------------------------

-------Subclasses--------
Guerreiro
Mago
-------------------------
'''
from abc import ABC, abstractmethod
from random import choice, randint
from rich import print


class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes_restantes = 3
        self.lista_golpes = []  # Cada classe filha vai preencher a sua

    def atacar(self, alvo, forca=100):
        # 1. Checa se quem vai atacar está vivo
        if self.vida < 1:
            print(f"💀  [red]{self.nome}[/] está derrotado e não pode atacar!")
            return

        # 2. Checa se o alvo já está morto
        if alvo.vida < 1:
            print(f"⚠️  [yellow]{alvo.nome}[/] já está derrotado. Não é possível atacá-lo!")
            return

        # 3. Checa se o personagem ainda tem golpes disponíveis
        if self.golpes_restantes < 1:
            print(f"[red]{self.nome}[/] não tem golpes disponíveis.")
            return
            
        dano_final = randint(1, forca)  # Dano aleatório entre 1 e a força do ataque
            
        # Sorteia um golpe da lista do personagem
        golpe_usado = choice(self.lista_golpes)

        print(
            f"⚔️  [green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com "
            f"[blue]{golpe_usado}[/] de força [red]{forca}[/]!"
            )

        alvo.receber_dano(dano_final)
        self.golpes_restantes -= 1
            

    def receber_dano(self, dano):
        self.vida -= dano

        # 1. Ajusta a vida se cair abaixo de 1
        if self.vida < 1:
            self.vida = 0
                
        # 2. Imprime o status do dano para todos (vivo ou morto)
        print(f"💥 [blue]{self.nome}[/] recebeu [red]{dano}[/] de dano! (Vida atual: [green]{self.vida}[/])")

        # 3. Imprime a caveira se morreu, ou apenas quebra a linha
        if self.vida == 0:
            print(f"💀 [bold red]{self.nome} foi derrotado em combate![/]\n")
        else:
            print("") # Adiciona a quebra de linha
            
            
    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.lista_golpes = ["Corte de Espada","Golpe de Escudo","Estocada Brutal",]

    def curar(self):
        if self.vida < 1:
            print(f"💀 [red]{self.nome}[/] está derrotado e não pode se curar!")
            return
                  
        cura = randint(1, 350)  # Cura aleatória entre 1 e 350
        
        self.vida += cura
        
        print(
            f"🛡️  [green]{self.nome}[/] bebeu uma Poção de Cura "
            f"e recuperou [green]{cura}[/] de vida! (Vida atual: [green]{self.vida}[/])"
        )
        print("")  # Adiciona a quebra de linha


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.lista_golpes = ["Bola de Fogo","Raio de Gelo","Relâmpago Arcano",]

    def curar(self):
        if self.vida < 1:
            print(f"💀 [red]{self.nome}[/] está derrotado e não pode se curar!")
            return
            
        cura = randint(1, 1000)  # Cura aleatória entre 1 e 1000
        
        self.vida += cura
        
        print(
            f"🔮 [magenta]{self.nome}[/] usou Magia de Regeneração "
            f"e recuperou [green]{cura}[/] de vida! (Vida atual: [green]{self.vida}[/])"
        )
        print("")  # Adiciona a quebra de linha