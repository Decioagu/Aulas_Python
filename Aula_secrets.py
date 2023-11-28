# secrets gera números aleatórios seguros
import secrets

# gera números inteiros
print(secrets.randbelow(10)) # resposta 0 até 9

# escolhe um elemento aleatório dentro da lista
print(secrets.choice(["A", "B", "C"])) # 
#-----------------------------------------------------------------------------------------------
# gerar senha aleatória

'''
    # s.ascii_letters => todas as letras maiúscula e minuscula
    # s.digits => números de 0 até 9
    # s.punctuation => todas as pontuações
    # K => quantidade de caracteres 
'''

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=4)))

# direto no terminal:
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
#-----------------------------------------------------------------------------------------------

import secrets

random = secrets.SystemRandom()
# Funções:
# seed
#   -> NÃO MAIS FAZ NADA
random.seed(0)

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