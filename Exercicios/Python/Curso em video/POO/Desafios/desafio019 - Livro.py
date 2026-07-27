'''
Crie a classe Livro, que vai simular a passagem de páginas de um livro,
considerando também se o usuário chegou ao fim da leitura.
'''
from rich import print

class Livro:
    def __init__(self, nome, num_paginas):
        self.nome = nome
        self.num_paginas = num_paginas
        self.pagina_atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.nome}[/]' que tem [green]{self.num_paginas}[/] páginas no total.\nVocê agora está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_paginas(self, qtd_avancar):
        de_onde_saiu = self.pagina_atual
        self.pagina_atual = min(self.pagina_atual + qtd_avancar, self.num_paginas)
        
        # Calcula quantas páginas foram puladas de verdade
        avanco_real = self.pagina_atual - de_onde_saiu
        
        # Se o usuário já estava no fim e tentou avançar mais, avisa e para
        if avanco_real == 0:
            print("[yellow]Você já terminou o livro! Não há mais páginas para avançar.[/]")
            return

        # Cria a trilha usando apenas o avanço real
        passo_a_passo = " ▶ ".join(f"Pág{p}" for p in range(de_onde_saiu + 1, self.pagina_atual + 1))
        trilha_final = f"{passo_a_passo} ▶ " if passo_a_passo else ""
        
        # Mostra o avanço real em vez de 'qtd_avancar'
        print(f"{trilha_final}[blue] Você avançou {avanco_real} páginas e agora está na[/] [yellow]página {self.pagina_atual}[/]")
        
        if self.pagina_atual == self.num_paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '[red]{self.nome}'[/]")


l1 = Livro("Dicas do Guigas", 8)
l1.avancar_paginas(2)
l1.avancar_paginas(2)
l1.avancar_paginas(9)