# empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)
print()

# --------------------------------------------------------------------------------------------


# desempacotamento dicionário
pessoa = {
    'Nome':'Décio',
    'Idade': 41,
    'Sexo': 'M'
}
a, b, c = pessoa
print(a,b,c, sep='\n')
print()
(a1, a2,), (b1, b2), (c1, c2) = pessoa.items() # .items()\ .values()\ .keys()
print(a1, a2)
print(b1, b2)
print(c1, c2)
print()

# --------------------------------------------------------------------------------------------

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} # desempacotar 2 dicionários em um novo dicionário

print(pessoas_completa) # exibir dicionário
print()

print(*pessoas_completa.items(), sep='\n') # exibir dicionário
print()

for chave, valor in pessoas_completa.items(): 
    print(chave, valor) # exibir dicionário
print()

# --------------------------------------------------------------------------------------------
'''
    args e kwargs
    *args - desempacotar nº argumentos
    **kwargs - keyword arguments (argumentos nomeados) => para dicionário
'''
# desempacotamento de argumentos e dicionário
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args) # args => objeto

    for chave, valor in kwargs.items(): # kwargs => dicionario
        print(chave, valor) 

# empacotar em dicionário
configuracoes = {
    'dicionário1': 1,
    'dicionário2': 2,
    'dicionário3': 3,
    'dicionário4': 4,
}
mostro_argumentos_nomeados('Meu', 'argumento', **configuracoes) # desempacotar

# --------------------------------------------------------------------------------------------

# desempacotamento em retorno da função
def impar_par(n):
    resposta = 'impar'
    if n % 2 == 0:
        resposta = 'par'
    return n, resposta

pergunta = impar_par(3)
print(pergunta) # tupla
print(*pergunta) # desempacotar em uma variável
n, res = impar_par(4)
print(f'{n} é {res}') # desempacotar em duas variável