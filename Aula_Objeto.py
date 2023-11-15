
# Objeto do tipo inteiro
inteiro = 1
print(f'{inteiro=} tipo {type(inteiro)}')
print(isinstance(inteiro, int))
print()

# Objeto do tipo ponto flutuante
flutuante = 1.1
print(f'{flutuante=} | tipo {type(flutuante)}')
print(isinstance(flutuante, float))
print()

# Objeto do tipo texto
string = 'texto'
print(f'{string=} | tipo {type(string)}')
print(isinstance(string, str))
print()

# Objeto do tipo booleano
booleano = True
print(f'{booleano=} | tipo {type(booleano)}')
print(isinstance(booleano, bool))
print()

# Objeto do tipo lista
lista = [1, 2, 3, 4, 5]
print(f'{lista=} | tipo {type(lista)}')
print(isinstance(lista, list))
print()

# Objeto do tipo tupla
tupla = ("a", "b", "c")
print(f'{tupla=} | tipo {type(tupla)}')
print(isinstance(tupla, tuple))
print()

# Objeto do tipo conjunto
conjunto = {1, 2, 3, 4, 5}
print(f'{conjunto=} | tipo {type(conjunto)}')
print(isinstance(conjunto, set))
print()

# dicionario
dicionario = {'nome':'Décio', 'idade':40, 'sexo':'masculino'}
print(f'{dicionario=} | tipo {type(dicionario)}')
print(isinstance(dicionario, dict))
