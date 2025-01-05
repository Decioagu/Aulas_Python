'''
Lista de Métodos String em Python
O Python oferece diversos métodos para manipular strings de forma eficiente. 
Abaixo, listo alguns dos métodos mais comuns e suas funcionalidades:

1. Modificação de Case:
# upper(): Converte todos os caracteres para maiúsculas.
# lower(): Converte todos os caracteres para minúsculas.
# capitalize(): Converte o primeiro caractere para maiúscula e os demais para minúsculas.
# swapcase(): Inverte o case de cada caractere (maiúsculas para minúsculas e vice-versa).

2. Busca e Substituição:
# find(substring): Encontra a primeira ocorrência da substring dentro da string, retornando o índice da posição inicial.
# rfind(substring): Encontra a última ocorrência da substring dentro da string, retornando o índice da posição inicial.
# index(substring): Similar ao find(), mas gera uma exceção se a substring não for encontrada.
# rindex(substring): Similar ao rfind(), mas gera uma exceção se a substring não for encontrada.
# count(substring): Conta o número de ocorrências da substring dentro da string.
# replace(old, new): Substitui todas as ocorrências de old por new na string.

3. Remoção e Adição:
# strip(): Remove espaços em branco no início e no final da string.
# lstrip(): Remove espaços em branco no início da string.
# rstrip(): Remove espaços em branco no final da string.
# center(width, fillchar): Centraliza a string dentro de um campo de largura especificada, usando o caractere de preenchimento fillchar.
# zfill(width): Adiciona zeros à esquerda da string até atingir a largura especificada.
# ljust(width, fillchar): Justifica a string à esquerda dentro de um campo de largura especificada, usando o caractere de preenchimento fillchar.
# rjust(width, fillchar): Justifica a string à direita dentro de um campo de largura especificada, usando o caractere de preenchimento fillchar.

4. Formatação:
# # format(*args, **kwargs): Formata a string usanisspacedo formatação de estilo antigo (similar ao C).
# # f-strings: Formata a string usando formatação de string f-string (mais recente e poderosa).

5. Métodos de Validação:
# endswith(): Verifica se a string termina com um substring específico.
# startswith(): Verifica se a string começa com um substring específico.
# isupper(): Verifica se todos os caracteres são maiúsculas.
# islower(): Verifica se todos os caracteres são minúsculas.
# isalnum(): Verifica se todos os caracteres são alfanuméricos (letras e números).
# isdecimal(): Verifica se todos os caracteres são decimais (0 a 9).
# isspace(): Verifica se todos os caracteres são espaços em branco.
# istitle(): Verifica se a string está formatada como título (primeira letra de cada palavra em maiúscula).
# isnumeric(): Verifica se a string contém apenas dígitos decimais (0 a 9).
# isalpha(): Verifica se a string contém apenas letras (A a Z e a a z).
# isalnum(): Verifica se a string contém apenas letras e dígitos decimais.
# isspace(): Verifica se a string contém apenas espaços em branco.
# isdigit(): Verifica se todos os caracteres da string são dígitos (incluindo subscritos e sobrescritos).
# match(): Usa expressões regulares para verificar se a string corresponde a um padrão específico.
# search(): Usa expressões regulares para encontrar a primeira ocorrência de um padrão na string.

6. Junção e Divisão:
# join(iterable): Junta uma sequência de strings em uma única string, usando o separador especificado no objeto iterável.
# split(sep, maxsplit): Divide a string em uma lista de substrings, usando o separador especificado por sep e limitando o número de divisões por maxsplit.

7. Conversão:
# encode(encoding): Converte a string para uma sequência de bytes usando a codificação especificada por encoding.
# decode(encoding): Converte uma sequência de bytes em uma string usando a codificação especificada por encoding.

8. Outros Métodos Úteis:
# len(): Retorna o tamanho da string (número de caracteres).
# startswith(prefix): Verifica se a string começa com a substring prefixa.
# endswith(suffix): Verifica se a string termina com a substring sufixa.
# istitle(): Verifica se a string está formatada como título (primeira letra de cada palavra maiúscula).
# splitlines(): Divide a string em uma lista de linhas, com base nas quebras de linha.
'''

# FORMATAÇÃO DE TEXTO
nome = 'Décio'
idade = 43
print("Meu nome é {} e tenho {} anos".format(nome, idade))
print("Meu nome é {n} e tenho {i} anos".format(i=idade, n=nome))
print(f"Meu nome é {nome} e tenho {idade} anos")

# FIM DA TABELA DE CORES
print()
print('= FATIAMENTO DE FRASE =')
frase = 'Curso em Vídeo Python'
print(f'Frase a ser analisada = "{frase}"')
print('0=> frase[:] =',frase[:])
print('1=> frase[9] =',frase[9])
print('2=> frase[:6] =',frase[:6])
print('3=> frase[15:] =',frase[15:])
print('4=> frase[9:14] =',frase[9:14])
print('5=> frase[0:6:2] =',frase[0:6:2])
print('6=> frase[15::3] =',frase[15::3])
print('7=> frase[:-4] =',frase[:-4])
print('8=> frase[-6:] =',frase[-6:])
print()

'''
    A isinstance()função em Python é uma função interna que pode ser usada para verificar se 
    um objeto é uma instância de uma determinada classe.
    Exemplo: (isinstance(object, class))
'''
x = [1, 2, 3]
print(isinstance(x, set))
print(isinstance(x, list))
print(isinstance(x, (set, list)))
x = 'a'
print(isinstance(x, (int, float)))
x = 1
print(isinstance(x, (int, float)))
x = 1.5
print(isinstance(x, (int, float)))

print('REALIZA CONTAGEM DO OBJETO ESPECIFICADO (QUANTIDADE QUE APARECE)')
frase = 'Curso em Vídeo Python'
print('Frase a ser analisada =',frase)
print('9 =',frase.count('o'))
print()

#REALIZA CONTAGEM DO OBJETO ESPECIFICADO, PONTO DE INICIO, FINAL (QUANTIDADE QUE APARECE)
frase = 'Curso em Vídeo Python'
print('8=',frase.count('o', 0, 15))
print()

#IDENTIFICA POSIÇÃO INICIAL DO OBJETO ESPECIFICADO, PONTO DE INICIO E FINAL
frase = 'Curso em Vídeo Python'
print('9a=',frase.find('o', 10, 15))
print()

#IDENTIFICA POSIÇÃO INICIAL DO OBJETO ESPECIFICADO, FINAL PARA O INICIO
frase = 'Curso em Vídeo Python'
print('9b=',frase.rfind('o'))
print()

#REALIZA CONTAGEM DO OBJETO ESPECIFICADO
frase = 'Curso em Vídeo Python'
print('10=',frase.count('deo'))
print()

#IDENTIFICA POSIÇÃO INICIAL DO OBJETO ESPECIFICADO
frase = 'Curso em Vídeo Python'
print('11=',frase.find('deo'))
print()

#IDENTIFICA POSIÇÃO INICIAL DO OBJETO ESPECIFICADO - RETORNA "-1" QUANDO NÃO ENCONTRADO
frase = 'Curso em Vídeo Python'
print('12=',frase.find('x'))
print()

#IDENTIFICA SE STRING =>'CURSO' ESTA CONTIDO EM FRASE - RETORNA TRUE OU FALSE
frase = 'Curso em Vídeo Python'
v = 'Curso' in frase
print('13= "Curso" in frase=',v)
print()

#IDENTIFICA SE STRING =>'CURSO' ESTA CONTIDO EM FRASE - RETORNA TRUE OU FALSE
frase = 'Curso em Vídeo Python'
n = 'Décio' in frase
print('14= "Décio" in frase=',n)
print()

#ALTERA A STRING 'Python' POR OUTRA 'Android' DENTRO DE UM TEXTO
frase = 'Curso em Vídeo Python'
frase.replace('Python','Android')
print('15= frase=',frase.replace('Python','"Android"'))
print('16= frase=',frase)
frase = 'Curso em Vídeo Python'
print('15= frase=',frase.replace('o','x',2))
print('16= frase=',frase)
print()
print()

#ALTERA A STRING 'Python' POR OUTRA 'Android' DENTRO DE UM TEXTO OU CONJUNTO DE CARACTER
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python','Android')
print('17= frase=',frase)
print()

#ALTERA TODA STRING PARA MAIÚSCULA
frase = frase.upper()
print('18= frase=',frase)
print()

#ALTERA TODA STRING PARA MIÚSCULA
frase = frase.lower()
print('19= frase=',frase)
print()

#ALTERA PRIMEIRA LETRA DA STRING PARA MIÚSCULA
frase = frase.capitalize()
print('20= frase=',frase)
print()

#ALTERA PRIMEIRA LETRA DA STRING PARA MIÚSCULA QUANDO HOUVER ESPAÇO
frase = frase.title()
print('21= frase=',frase)
print()

#CONTA A QUANTIDADE DE STRING EM UMA CONJUNTO DE CARACTERES
frase = 'Curso em Vídeo Python'
print('22= contagem=',frase ,len(frase))
print()

#ELIMINA ESPAÇO EM BRANCO DE UM TEXTO A DIREITA
frase = '   Aprenda Python   '
print('23= contagem com espaço={}={}'.format(frase ,len(frase)))
frase = '   Aprenda Python   '
frase = frase.rstrip()
print('24= contagem sem espaço a direita={}={}'.format(frase ,len(frase)))
print()

#ELIMINA ESPAÇO EM BRANCO DE UM TEXTO A ESQUERDA
frase = '   Aprenda Python   '
print('25= contagem com espaço={}={}'.format(frase ,len(frase)))
frase = '   Aprenda Python   '
frase = frase.lstrip()
print('26= contagem sem espaço a esquerda={}={}'.format(frase ,len(frase)))
print()

#ELIMINA ESPAÇO EM BRANCO DE UM TEXTO
frase = '   Aprenda Python   '
print('27= contagem com espaço={}={}'.format(frase ,len(frase)))
frase = '   Aprenda Python   '
frase = frase.strip()
print('28= contagem sem espaço={}={}'.format(frase ,len(frase)))
print()

print('DIVIDE UMA STRING ONDE HOUVER ESPAÇO EM UMA LISTA OU CARACTER SELECIONADO')
frase = 'Curso em Vídeo Python'
print(frase)
frase = frase.split() # ou frase.split('V')
print(frase)
print(frase[0])
print(frase[1])
print(frase[2])
print(frase[3])
print(frase[3][:2])
print()

print('JUNTA CARACTERES DE UMA LISTA')
print(frase)
frase = ' '.join(frase)
print(frase)
frase = frase.split()
frase = '_'.join(frase)
print(frase)


print('{:♥<40}'.format(' lOJAS DESCONTÃO '))
print('{:=<27}{}'.format('1',' lOJAS DESCONTÃO '))
print('{:♥^40}'.format(' lOJAS DESCONTÃO '))
print(' lOJAS DESCONTÃO '.center(39, '♥'))

x = 5
v = 5
p = 9
print(x is v)
print(x is p)

a = 1 - 2
print(abs(a))

'''
Os parâmetros sep= e end= em Python são usados com a função print() 
para personalizar a formatação da saída no console.

sep= (Separador)
Define o separador entre os elementos na string, onde por padrão seria espaço vazio.

end= (Finalizador)
Define o caractere que será adicionado ao final da saída da função print(), 
onde por padra é "\n" quebra de linha.

'''
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My name is", end=" ")
print("Monty Python.")
print("My name is", end="###")
print("Monty Python.")
print("My", "name", "is", sep="_", end="*")
print("Monty Python.")

# Suponhamos que temos a seguinte string:

frase = 'uma FRASE'

# Podemos acessar individualmente cada caractere em uma frase.
# A ideia é a mesma de acessar uma lista:
print(frase[0])
print(frase[1])
print(frase[2])

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

# Porém, strings são imutáveis: não podemos alterar caracteres individuais
# A linha abaixo, se for descomentada, dará erro no programa:
# frase[4] = 'C'

# Podemos converter strings para listas:
listafrase = list(frase)
print(listafrase)

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)

# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Existem algumas funções interessantes que retornam a string "tratada":
s1 = frase.capitalize() # 1a letra maiúscula, restante minúscula
s2 = frase.title() # todo início de palavra em maiúscula, resto minúscula
s3 = frase.upper() # string inteira em maiúscula
s4 = frase.lower() # string inteira em minúscula
s5 = frase.replace('F', 'C') # substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
# Note que NENHUMA delas ALTERA a string original, elas sempre retornam
# a string nova.
print('String original:', frase)

# Outra possibilidade com strings é quebrar a string em uma lista de substrings
# Sempre que o caractere especificado é encontrado, a string é quebrada
quebra1 = frase.split(' ') # quebra a frase no caractere espaço em branco
quebra2 = s3.split('A') # quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)
# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'

# Verifique se a string começa com "Hello", True ou False
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
