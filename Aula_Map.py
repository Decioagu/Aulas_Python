'''
    A função map() em Python usa uma função e um iterável como seus argumentos 
    e retorna um iterador que aplica a função a cada elemento do iterável.

    Exemplo: nome = list(map(função, iterável))

    iterável= string, lista, dicionario
'''

lista_num_int = [1, 2, 3, 4, 5]

def quadrado1(x):
  return x * 3
num_ao_quadrado1 = list(map(quadrado1, lista_num_int))
print(num_ao_quadrado1)

#-----------------------------------------------------------------------

num_ao_quadrado2 = list(map(lambda x: x * 3, lista_num_int))
print(num_ao_quadrado2)
print()
