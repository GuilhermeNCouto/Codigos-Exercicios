from abc import ABC, abstractmethod

"""
RESUMO DE OURO: ABSTRAÇÃO VS FLEXIBILIDADE
------------------------------------------
1. MÉTODO ABSTRATO (@abstractmethod): 
   - É uma "cláusula obrigatória" do contrato.
   - O Python PROÍBE a criação do objeto se o filho não implementar esse método.
   - Use quando o sistema QUEBRA se aquela informação não existir (ex: ligar()).

2. COMO TRATAR O QUE É "OPCIONAL" OU "GENÉRICO":
   - Opção A (Cumprir com None): O filho implementa o método, mas retorna None.
   - Opção B (Super): O filho chama o super().metodo() se o pai tiver um valor padrão.
   - Opção C (Remover Abstração): Se não é vital para TODOS, deixe como um método 
     comum (concreto) na classe pai. O filho herda o padrão e só muda se quiser.

DICA: Abstração serve para GARANTIR segurança. Herança serve para REAPROVEITAR código.
"""

# Exemplo de 'Genérico' usando o comportamento do Pai:
# @property
# def marca(self):
#     return super().marca or "Genérico"

# --- OPÇÃO A: OBRIGATÓRIO, MAS ACEITA "NONE" ---
# O contrato exige que o filho se manifeste, mesmo que seja para dizer "não tenho".
class ControleRemotoA(ABC):
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleSemMarca(ControleRemotoA):
    @property
    def marca(self):
        return None  # Cumpriu a obrigação, mas devolveu vazio.


# --- OPÇÃO B: OBRIGATÓRIO COM PADRÃO NO PAI ---
# O pai dá uma sugestão, mas o filho AINDA É OBRIGADO a escrever o método.
class ControleRemotoB(ABC):
    @property
    @abstractmethod
    def marca(self):
        return "Genérico"

class ControlePadrao(ControleRemotoB):
    @property
    def marca(self):
        # Ele usa o que o pai sugeriu sem precisar inventar nada.
        return super().marca


# --- OPÇÃO C: TOTALMENTE OPCIONAL (SEM ABSTRAÇÃO) ---
# O pai já entrega o método pronto. O filho só mexe se quiser ser diferente.
class ControleRemotoC(ABC):
    @property
    def marca(self): # <--- Note que NÃO tem o @abstractmethod aqui
        return "Genérico"

class ControlePreguicoso(ControleRemotoC):
    pass # Não precisa escrever NADA sobre marca, já herdou o "Genérico"

class ControleRemotoD(ABC):
    @property
    @abstractmethod
    def marca(self):
        return "Genérico"

class ControleTV(ControleRemotoD):
    @property
    def marca(self):
        # Tenta pegar o valor do pai. Se o pai retornar algo 'Falso' ou 'Vazio',
        # ele assume o que está depois do 'or'.
        return super().marca or "Marca Desconhecida"

# Se super().marca fosse None, a saída seria "Marca Desconhecida"