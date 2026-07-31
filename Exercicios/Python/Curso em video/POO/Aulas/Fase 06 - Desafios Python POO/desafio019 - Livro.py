'''
Crie a classe Livro, que vai simular a passagem de páginas de um livro,
considerando também se o usuário chegou ao fim da leitura.
'''
from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1
        
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas}[/] páginas no total.\nVocê agora está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_paginas(self, qtd_avancar = 1):
        count = 0
        for pg in range(0, qtd_avancar, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward:", end=" ")
                sleep(0.5)
                count += 1
        print(f"[blue]Você avançou {count} página(s) e agora está na [yellow]página {self.pagina_atual}[/][/]")
        
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao fim do livro '{self.titulo}'![/]")
        

    def fim_do_livro(self) -> bool:
        return self.pagina_atual == self.total_paginas
    
    
l1 = Livro("Dicas do Guigas", 12)
l1.avancar_paginas()
l1.avancar_paginas(2)
l1.avancar_paginas(2)
l1.avancar_paginas(9)