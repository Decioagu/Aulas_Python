"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2)) # round(numero, quantidade dígitos)

print('===================================')
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

print('===================================')

import math
N = 2.54159265359
print(N)
print(math.trunc(N)) #.Print parte inteira apos "."
print(round(N)) #......Print parte inteira arrendondado + ou - "N.5"
print(round(N, 1)) #...Print 1 casa decimal apos "."
print(round(N, 2)) #...Print 2 casa decimal apos "."
print(round(N, 3)) #...Print 3 casa decimal apos "."
print(f'{N:.0f}') #....Print parte inteira arrendondado + ou - "N.5"
print(f'{N:.1f}') #....Print 1 casa decimal apos "."
print(f'{N:.2f}') #....Print 1 casa decimal apos "."
print(f'{N:.3f}') #....Print 1 casa decimal apos "."
print(f'{N:5.0f}') #...Print parte inteira arrendondado + ou - "N.5", com 5 espaço afastamento
print(f'{N:10.1f}') #..Print 1 casa decimal apos ".", com 10 espaço afastamento
print(f'{N:15.2f}') #..Print 2 casa decimal apos ".", com 15 espaço afastamento
print(f'{N:20.3f}') #..Print 3 casa decimal apos ".", com 20 espaço afastamento

print('===================================')

'''
Em Python, a função abs() é usada para retornar o valor absoluto de um número. 
O valor absoluto de um número é seu tamanho, independentemente de sua direção.

A função abs() aceita um único argumento, que é o número cujo valor absoluto 
deve ser retornado. O tipo do argumento pode ser qualquer tipo numérico, 
incluindo números inteiros, números de ponto flutuante e números complexos.
'''

print(-1)
print(abs(-1))

print(1 + 2j)
print(abs(1 + 2j))

print('===================================')