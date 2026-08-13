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

    def atacar(self, alvo, forca):
        # 1. Checa se quem vai atacar está vivo
        if self.vida < 1:
            print(f"💀  [red]{self.nome}[/] está derrotado e não pode atacar!")
            return

        # 2. Checa se o alvo já está morto
        if alvo.vida < 1:
            print(f"⚠️  [yellow]{alvo.nome}[/] já está derrotado! Não é possível atacá-lo.")
            return

        # 3. Executa o ataque se houver golpes disponíveis
        if self.golpes_restantes > 0:
            dado = randint(1, 6)

            # Mapeia 1 -> 10% até 6 -> 100%
            multiplicadores = {
                1: 0.10,
                2: 0.28,
                3: 0.46,
                4: 0.64,
                5: 0.82,
                6: 1.00,
            }
            porcentagem = multiplicadores[dado]
            dano_final = int(forca * porcentagem)
            
            # Sorteia um golpe da lista do personagem
            golpe_usado = choice(self.lista_golpes)

            print(
                f"⚔️  [green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com "
                f"[blue]{golpe_usado}[/] de força [red]{forca}[/] causando [red]{dano_final}[/] de dano!"
            )

            alvo.receber_dano(dano_final)
            self.golpes_restantes -= 1
        else:
            print(f"[red]{self.nome}[/] não tem golpes disponíveis.")

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 1:
            self.vida = 0
            print(
                f"💥 [blue]{self.nome}[/] recebeu [red]{dano}[/] de dano! "
                f"(Vida: [green]{self.vida}[/])"
            )
            print(f"💀 [bold red]{self.nome} foi derrotado em combate![/]\n")
        else:
            print(
                f"💥 [blue]{self.nome}[/] recebeu [red]{dano}[/] de dano! "
                f"(Vida atual: [green]{self.vida}[/])\n"
            )

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.lista_golpes = [
            "Corte de Espada",
            "Golpe de Escudo",
            "Estocada Brutal",
        ]

    def curar(self):
        if self.vida < 1:
            print(f"💀 [red]{self.nome}[/] está derrotado e não pode se curar!")
            return
            
        cura_maxima = 350
        dado = randint(1, 6)
        multiplicadores = {1: 0.10, 2: 0.28, 3: 0.46, 4: 0.64, 5: 0.82, 6: 1.00}
        
        cura_final = int(cura_maxima * multiplicadores[dado])
        self.vida += cura_final
        
        print(
            f"🛡️ [green]{self.nome}[/] bebeu uma Poção de Cura"
            f"e recuperou [green]{cura_final}[/] de vida! (Vida atual: [green]{self.vida}[/])"
        )


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.lista_golpes = [
            "Bola de Fogo",
            "Raio de Gelo",
            "Relâmpago Arcano",
        ]

    def curar(self):
        if self.vida < 1:
            print(f"💀 [red]{self.nome}[/] está derrotado e não pode se curar!")
            return
            
        cura_maxima = 1000
        dado = randint(1, 6)
        multiplicadores = {1: 0.10, 2: 0.28, 3: 0.46, 4: 0.64, 5: 0.82, 6: 1.00}
        
        cura_final = int(cura_maxima * multiplicadores[dado])
        self.vida += cura_final
        
        print(
            f"🔮 [magenta]{self.nome}[/] usou Magia de Regeneração "
            f"e recuperou [green]{cura_final}[/] de vida! (Vida atual: [green]{self.vida}[/])"
        )