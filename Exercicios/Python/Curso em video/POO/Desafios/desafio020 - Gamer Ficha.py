'''
Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos
de uma pessoa. Crie Também um método que permita mostrar a ficha desse gamer.
'''

from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        # Lista de jogos com o controle e o nome em azul
        lista_jogos = "\n".join(f":video_game: [blue]{jogo}[/]" for jogo in self.favoritos)
        
        conteudo = (
            f"Nome real: [black on blue]{self.nome}[/]\n"
            f"Jogos Favoritos:\n{lista_jogos}"
        )
        
        print(Panel(conteudo, title=f"Jogador <{self.nick}>", width=40))


j1 = Gamer("Guilherme Couto", "xDeathNyan")
j1.add_favoritos("Gears of War")
j1.add_favoritos("Skyrim")
j1.add_favoritos("Forza Horizon")
j1.add_favoritos("Rocket League")
j1.ficha()

j2 = Gamer("Le Thau", "Psychokiller")
j2.add_favoritos("The Witcher 3")
j2.add_favoritos("Cyberpunk 2077")
j2.ficha()
