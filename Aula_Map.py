'''
    A função map() em Python usa uma função e um iterável como seus argumentos 
    e retorna um iterador que aplica a função a cada elemento do iterável.

    Exemplo: "variável" = list(map(função, iterável))

    iterável= string, lista, dicionario
'''

lista_num_int = [1, 2, 3, 4, 5]

def quadrado1(x):
  return x * 3
num_ao_quadrado1 = list(map(quadrado1, lista_num_int))
print(num_ao_quadrado1)

print('===================================================================')

lista_num_ao_quadrado2 = list(map(lambda x: x * 3, lista_num_int))
print(lista_num_ao_quadrado2)
print()

#-----------------------------------------------------------------------

dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}

novas_chaves = map(str.upper, dicionario.keys())

print(*novas_chaves)

print('===================================================================')

dicionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

novos_valores = map(lambda x: x ** 2, dicionario.values())

print(*novos_valores)

#-----------------------------------------------------------------------

base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)

#-----------------------------------------------------------------------
