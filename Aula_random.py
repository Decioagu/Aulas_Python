# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html

''' 
    O módulo random em Python fornece funções e classes para gerar números aleatórios. 
    Esses números podem ser usados para criar efeitos aleatórios em seus programas.

    import random
    import time
    # Funções:
    # seed
    #   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
    random.seed(0) # valor esta definindo gerador
    random.seed(time.time) # valor esta definindo gerador

    # Aula_secrest.py (Aula 297)
    import secrets 
    random = secrets.SystemRandom() # anula efeito do random.seed(0)
'''

import random

# Gera um número real aleatório entre 0 e 1
numero_aleatorio = random.random()
print(numero_aleatorio)

# Gera um elemento aleatório da lista [1, 2, 3, 4, 5]
elemento_aleatorio = random.choice([1, 2, 3, 4, 5])
print(elemento_aleatorio)

#-----------------------------------------------------------------------------------------------

import random

# random.randrange(início, fim, passo)
#   -> Gera um "número inteiro" aleatório dentro de um intervalo específico
r_range = random.randrange(0, 21, 5) # resposta = 0 / 5 / 10 / 20 devido ao passo = 5
print(r_range)

print('<==========================================================>')


# random.randint(início, fim)
#   -> Gera um "número inteiro" aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20) # resposta 10 até 20
print(r_int)

print('<==========================================================>')

# random.uniform(início, fim)
#   -> Gera um "número flutuante" aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20) # resposta 10 até 20
print(r_uniform)

#-----------------------------------------------------------------------------------------------
# embaralhar lista
import random
# random.shuffle(SequenciaMutável) -> Embaralha a "lista original"
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)
print(nomes)

print('<==========================================================>')

lista_ordenada = [1, 2, 3, 4, 5]
random.shuffle(lista_ordenada)
print(lista_ordenada)

#-----------------------------------------------------------------------------------------------
# sorteá nomes
import random

nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
print(nomes)
print('<==========================================================>')

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3) # "k=" quantidade de elementos 
print(novos_nomes) # não pode repete valores
print('<==========================================================>')

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3) # "k=" quantidade de elementos 
print(novos_nomes) # pode repete valores
print('<==========================================================>')

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))