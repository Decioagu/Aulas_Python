# CRIAR UMA TUPLA
a = ('a',)
print(a , type(a))
b = tuple('b')
print(b , type(b))
x = tuple()
print(x, type(x))
x = 'A',
print(x , type(x))
#-----------------------------------------------------------------------------------------------

# APAGAR OU DELETAR UMA TUPLA
s = ('c','a','b')
del s
#-----------------------------------------------------------------------------------------------

# DESEMPACOTAMENTO
x = ('A','B','C')
print(x)
a, b, c = x
print(a, b, c, '=', x)
print(a)
print(b)
print(c)
print(*x)
#-----------------------------------------------------------------------------------------------

# MOSTRA UMA TUPLA EM FORMA ORDENADA
teste = ('C','A','B')
print(sorted(teste))
print(teste)
teste = '*',
print(teste, type(teste))
#-----------------------------------------------------------------------------------------------

# UNIR TUPLA
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
# c ≠ b
c = a + b
d = b + a
print(c)
print(d)
#-----------------------------------------------------------------------------------------------

# MOSTRA A POSIÇÃO EM QUE UM ELEMENTO APARECE NA TUPLA
x = (2, 5, 4, 1, 8, 5, 2)
print(f'TUPLA = {x}')
print(f'O número 8 aparece  {x.index(8) + 1}º na TUPLA')
print(f'O número 1 aparece  {x.index(1) + 1}º na TUPLA')
print(f'O número 2 aparece  {x.index(2) + 1}º na TUPLA')
print(f'O número 2 aparece  {x.index(2, 1) + 1}º na TUPLA')
print(f'O número 5 aparece  {x.index(5, 2) + 1}º na TUPLA')
print(f'O número 5 aparece  {x.index(5, 0, 2) + 1}º na TUPLA') # x.index(número, inicio, parada)
# print(f'O número 9 aparece  {x.index(9) + 1}º na TUPLA') # gera erro não consta na tupla
try:
    print(f'O número 9 aparece  {x.index(9) + 1}º na TUPLA')
except ValueError:
    print('"9" NÃO esta na tupla')

print('<==========================================================>')

z = ('A','B','C', 'D', 'D')
print(f'TUPLA = {z}')
# print(f'Letra A  {z.index('A') + 1}º') # erro
print('Letra C ' + str(z.index('C') + 1) +'º')
print('Letra D ' + str(z.index('D') + 1) +'º')
# print('Letra Z ' + str(z.index('Z') + 1) +'º') # ERRO
try:
    print('Letra Z ' + str(z.index('Z') + 1) +'º')
except ValueError:
    print('"Z" NÃO esta na tupla')
#-----------------------------------------------------------------------------------------------

# CONTA A QUANTIDADE DE VEZES QUE ELEMENTO DEFINIDO APARECE NA TUPLA 
z = (2, 5, 4, 1, 8, 5, 2)
print(f'TUPLA = {z}')
print(f'Número 5 aparece {z.count(5)} vezes na TUPLA')
print(f'Número 3 aparece {z.count(3)} vezes na TUPLA') # não ocorre erro de exceção

print('<==========================================================>')

X = ('A','B','C', 'D', 'D')
print(f'TUPLA = {X}')
print(f'Esta TUPLA contem {len(X)} elementos')
print('Letra "A" aparece ' + str(X.count('A')) + ' vezes')
print('Letra "F" aparece ' + str(X.count('F')) + ' vezes') # não ocorre erro de exceção
print('Letra "D" aparece ' + str(X.count('D')) + ' vezes')
#-----------------------------------------------------------------------------------------------

# MOSTRA A POSIÇÃO DE UMA TUPLA EM ORDEM COMO SE FOSSE UMA LISTA
x = ('f', 'd', 'b', 'c', 'g', 'a', 'e')
print(sorted(x))
#-----------------------------------------------------------------------------------------------

# CONTAGEM E POSIÇÃO DE UM ELEMENTO NA TUPLA
tupla = (3, 2, 3, 3)
for posição, valor in enumerate(tupla, start=1):
    if valor == 3:
        print(f'O valor {valor} apareceu na {posição}ª posição.')
#-----------------------------------------------------------------------------------------------

# NAMEDTUPLES (aula 271)
""" 
    # namedtuples - tuplas imutáveis com nomes para valores
    # Usamos namedtuples para criar classes de objetos que são apenas um
    # agrupamento de atributos, como classes normais sem métodos, ou registros de
    # bases de dados, etc.
    # As namedtuples são imutáveis assim como as tuplas.
    # https://docs.python.org/3/library/collections.html#collections.namedtuple
    # https://docs.python.org/3/library/typing.html#typing.NamedTuple
    # https://brasilescola.uol.com.br/curiosidades/baralho.htm
"""
from collections import namedtuple

Carta = namedtuple('Carta', ['naipe', 'valor'] )

espadas = Carta('ESPADAS', 'DAMA')

print(espadas)

print(espadas[0])
print(espadas.naipe)

print(espadas[1])
print(espadas.valor)

for valor in espadas:
    print(valor, end= ' => ')
print()

'''
    O método _asdict() em Python é um método especial que retorna um dicionário contendo 
    os campos de uma instância de namedtuple como chaves e seus valores correspondentes como valores.
'''
dicionario = espadas._asdict()
print (f'{dicionario=}')

print('<==========================================================>')

from collections import namedtuple

Carta = namedtuple(
    'Carta', ['naipe', 'valor'],
    defaults=['NAIPE', 'VALOR'] # valor padrão
)

espadas = Carta('ESPADAS')

print(espadas)

ouro = Carta()
print(ouro)

'''
    _fields em Python é um atributo de classes e namedtuples que contém uma tupla com os nomes 
    dos campos da classe ou namedtuple. Os campos são definidos na definição da classe ou namedtuple 
    e são usados para acessar e manipular os dados da classe ou namedtuple.
'''
print(espadas._fields) # ver valor padrão
print(ouro._fields) # ver valor padrão

'''
    _field_defaults em Python é um atributo de namedtuples que contém os valores padrão 
    dos campos da namedtuple. Os valores padrão são especificados no construtor da namedtuple 
    e são usados quando um campo não é fornecido na criação da instância da namedtuple.
'''
print(espadas._field_defaults) # ver valor padrão
print(ouro._field_defaults) # ver valor padrão

print('<==========================================================>')

from typing import NamedTuple

class Carta(NamedTuple):
    naipe: str = 'NAIPE'
    valor: str = 'VALOR'

espadas = Carta('ESPADAS', 'DAMA')

print(espadas)

print(espadas[0])
print(espadas.naipe)

print(espadas[1])
print(espadas.valor)

dicionario = espadas._asdict() # formatação para dicionario
print (f'{dicionario=}') 

print(espadas._fields) # ver valor padrão
print(espadas._field_defaults) # ver valor padrão
#-----------------------------------------------------------------------------------------------
