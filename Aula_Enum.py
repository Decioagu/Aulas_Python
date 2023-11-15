# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
"""
    O módulo enum em Python fornece uma maneira fácil de criar enumerações personalizadas. 
    Uma enumeração é um tipo de dado que consiste em um conjunto de valores nomeados. 
    Os valores de enumeração são geralmente constantes e são usados para representar 
    diferentes estados ou opções de um sistema.
"""

from enum import Enum

class Cores(Enum):
    VERMELHO = 1
    AZUL = 2
    AMARELO = 3

class Semaforo:
    def __init__(self, cor):
        self.cor = cor

    def mudar_cor(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

semaforo = Semaforo(Cores.AZUL)

print(semaforo.get_cor())
#-----------------------------------------------------------------------------------------------

import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)