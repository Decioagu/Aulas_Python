'''
    A import é uma instrução em Python que importar módulos para um programa. 
    Um módulo é um arquivo Python que contém código que pode ser reutilizado em outros programas Python.

    import "module_name"
    Onde "module_name" é o nome do módulo que queremos importar.
'''

# Por exemplo, para importar o módulo math, podemos usar o seguinte código:

import math

x = 16

sqrt_x = math.sqrt(x)

print(sqrt_x)
#-----------------------------------------------------------------------------------------------

'''
    Também podemos importar apenas funções específicas de um módulo. 
    Para fazer isso, usamos a sintaxe from module_name import function_name. 
    Por exemplo, para importar apenas a função sqrt() do módulo math, podemos usar o seguinte código:
'''

from math import sqrt

x = 16

sqrt_x = sqrt(x)

print(sqrt_x)

# OBS: Este código imprimirá o mesmo que o código anterior.
#-----------------------------------------------------------------------------------------------

'''
    Por fim, também podemos importar todos os atributos de um módulo. 
    Para fazer isso, usamos a sintaxe from module_name import *. 
    Por exemplo, para importar todos os atributos do módulo math, podemos usar o seguinte código:
'''

from math import *

x = 16

sqrt_x = sqrt(x)

print(pi)
#-----------------------------------------------------------------------------------------------

# Para apelidar uma função do modulo adicione no final da importação "as" e "apelido", exemplo:

from math import sqrt as raiz

x = 16

raiz_quadrada = raiz(x)

print(raiz_quadrada)
#-----------------------------------------------------------------------------------------------

import pprint
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 50, },
    {'nome': 'p5', 'preco': 5, },
]

print(*produtos, sep='\n') # desempacotar lista
print()
print(produtos, sep='\n') # desempacotar lista
print()
pprint.pprint(produtos) # desempacotar lista
#-----------------------------------------------------------------------------------------------

from teste import titulo

titulo('Décio Santana de Aguiar'.upper())
