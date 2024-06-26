'''
Generator expression em Python é uma expressão que retorna um objeto gerador. 
É semelhante a uma compreensão de lista, mas em vez de criar uma lista, 
cria um objeto gerador que pode ser iterado para produzir os valores no gerador.

A sintaxe da Generator expression é a seguinte:

Exemplo Python:
>>> (expression for item in iterable if condition)

Onde:

    * expression é o valor que será retornado para cada item no iterable.
    * iterable é uma sequência iterável de objetos.
    * condition é uma expressão booleana opcional. Se for fornecida, apenas os itens do iterable 
      para os quais a expressão for avaliada como True serão incluídos no gerador.

Exemplo Python:
>>> (x for x in range(11) if x % 2 == 0)
    <generator object <genexpr> at 0x7f4092688d50>

Exemplo Python:
>>> for number in (x for x in range(11) if x % 2 == 0):
    print(number)
'''

import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
print(iterable)
print(iterator) # não é possível acesso direto dos itens
for x in range(5):
    print(x)

lista = [n for n in range(100)] # lista
generator = (n for n in range(100)) # compacta range em um local na memória (economiza memória)
# getsizeof() é uma função em Python retorna o tamanho de um objeto em bytes
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator) # não é possível acesso direto dos itens
print(next(generator))
print(next(generator))
print(next(generator))

# OU 

# for n in generator:
#     print(n)

# --------------------------------------------------------------
'''
    Em Python, o "yield" é uma palavra-chave que é usada para criar geradores. 
    Geradores são objetos que podem ser iterados, mas que não armazenam todos 
    os seus valores na memória ao mesmo tempo. Isso os torna mais eficientes do 
    que listas ou tuplas, que precisam armazenar todos os seus valores antes de 
    poderem ser iterados.
'''
def gerador():
  yield 1
  yield 2
  yield 3

gerador = gerador()

print(gerador) # não é possível acesso direto dos itens
print(next(gerador))
print(next(gerador))
print(next(gerador))
# print(next(gerador)) # solicitar um novo print haverá erro

print('===================================================================')

# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=20)

# print(*gen)
for n in gen:
    print(n)
# --------------------------------------------------------------