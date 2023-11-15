# Função soma embutido no Python
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print(soma)
#-----------------------------------------------------------------------------------------------

# Define tipo do parâmetro na função
def A(z: str): # objeto tipo str
    print(z.upper())
x = A('oi')
#-----------------------------------------------------------------------------------------------

# Função sem parâmetro
def teste():
    soma = 2 + 3
    mult = 2 * 3
    print(f'soma = {soma}')
    print(f'multiplicação = {mult}')
teste()
#-----------------------------------------------------------------------------------------------

# Função com 2 parâmetros declarados
def teste(a, b): # A quantidade de parâmetro deve ser igual ao valor declarado
    soma = a + b
    mult = a * b
    print(f'soma = {soma}')
    print(f'multiplicação = {mult}')
teste(2, 3) # A quantidade de valor declarado deve ser igual ao parâmetro
#-----------------------------------------------------------------------------------------------

# Função com 2 parâmetro (ver tipo)
def dados(nome, matr=1): # parâmetro "matr = 1" se não for definido
    print(nome, type(nome),matr, type(matr))
dados('Décio', 5699)
#-----------------------------------------------------------------------------------------------

# ordem de execução de variáveis
def teste(x):
    y = x
    x += 5
    z = 25
    print(f'Valor de "z" DENTRO do "def" = {z}')
    print(f'Valor de "x" DENTRO do "def" = {x}')
    print(f'Valor de "y" DENTRO do "def" = {y}')
z = 5
teste(z)
print(f'Valor de "z" FORA do "def" = {z}')
#-----------------------------------------------------------------------------------------------

# Função com quantidade de parâmetro indeterminado (DESEMPACOTAMENTO - lista, tupla)
def dados(*inf):
    print(inf, type(inf))
    print(inf[1], inf[0])
dados('Décio', 5699)
#-----------------------------------------------------------------------------------------------

# Função com quantidade de parâmetro indeterminado (DESEMPACOTAMENTO - dicionario)
def dados(**inf):
    print(inf,type(inf))
    print(inf['idade'], inf['nome'])
dados(nome='Décio', idade=5)
#-----------------------------------------------------------------------------------------------

# Função com 2 parâmetro (ver tipo)
def nome(p_nome, s_nome):
    print(p_nome,s_nome) # Ordem de exibição dos parâmetro
    print(p_nome, type(p_nome), s_nome, type(s_nome))
nome(s_nome='Santana', p_nome='Décio') # Ordem declarações das variáveis
#-----------------------------------------------------------------------------------------------

# Exemplo de cálculo com 3 parâmetro
def contador(inicio, fim, passo):
    cont = inicio
    while cont <= fim:
        print(cont, end=' ')
        cont += passo
    print('Fim!')
contador(0, 10, 2)
#-----------------------------------------------------------------------------------------------

# Declaração de parâmetro
def teste(a=0, b=0, c=0):
    soma = a + b + c
    print(f'{a}+{b}+{c} = {soma}')
teste(1, 2, 3)
teste(1, 2)
teste(3)
teste()
teste(1, b=2)
# teste(a=1, 2, 3) # Erro... após declara parâmetro a sequencia deve ser declarada
teste(c=3, a=1, b=2)
teste(b=2, a=1)
teste(a=1, c=3)
teste(c=3, b=2)
#-----------------------------------------------------------------------------------------------

# executar múltiplos argumentos em um único parâmetro (DESEMPACOTAMENTO - lista, tupla)
def contador(*num):
    print(num)
contador(0, 2, 4, 6, 8, 10)
contador(0, 2, 4, 6, 8,)
contador(0, 2, 4, 6)
contador(0, 2, 4)
contador(0, 2)
contador(0)
contador()
#-----------------------------------------------------------------------------------------------

# exemplo (DESEMPACOTAMENTO - lista, tupla)
def valor(*n, div=1):
    resultado = sum(n)/div
    return resultado

print(valor(8,10, div=2))
#-----------------------------------------------------------------------------------------------

# exemplo (DESEMPACOTAMENTO - dicionario)
def piscina(prof, **infos):
    vol = prof * infos['largura'] * infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)
#-----------------------------------------------------------------------------------------------



print()
def teste(x):
    global a
    print(f'Valor de "a" DENTRO do "def" = {a}')
    a = 15
    x += 10
    y = 10
    print(f'Valor de "a" DENTRO do "def" = {a}')
    print(f'Valor de "x" DENTRO do "def" = {x}')
    print(f'Valor de "y" DENTRO do "def" = {y}')
a = 5
teste(a)
print(f'Valor de "a" FORA do "def" = {a}')


print()
def teste(a, b):
    soma = a + b
    mult = a * b
    return soma
a = int(input('a = '))
b = int(input('b = '))
x = teste(a, b)
print(f'soma_ab = {x}')

def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.append(i)
    return strange_list
print(strange_list_fun(5))

def notas(* num, sit=False):
    """
    A função notas calcula a média do aluno independente de quantas notas
    forem adicionado a média e possui o opcional da situação do aluno
    conforme valor da média >= 7 ou menor que 5.

    :param num: valores (notas) para calcular a média do aluno
    :param sit:(opcional) quanto a situação do aluno
    :return: retorna a um dicionario os parâmetros =>
    => Total: quantidade de notas inseridas;
    => Maior: maior nota;
    => Média: média entre as notas;
    => Situação: (opcional) se aluno foi ou não aprovado.
    """
    dic = {}
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Média'] = sum(num)/len(num)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'APROVADDO'
        elif dic['Média'] < 5:
            dic['Situação'] = 'REPROVADO'
        else:
            dic['Situação'] = 'RECUPERAÇÃO'
    return dic
#__main__
resp = notas(7, 4, 5, 5, sit=True)
print(resp)
print()
help(notas)


print()
def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'=' * (len(txt) + 4))
    print(f'= {txt} =')
    print(f'=' * (len(txt) + 4))
titulo('Décio Santana de Aguiar'.upper())


print()
def opcao(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar os valores "S" ou "N" para variável "op"
    
    :msg : texto descrito pelo usuário 
    :op: Variável recebe somente os valores "S" ou "N"
    :return: Retorna variável "op" com o valor "S" ou "N"
    """
    while True:
        op = input(msg).strip().upper()
        if op in 'S':
            print()
            break
        elif op in 'N':
            break
        else:
            print()
            print(f'Opção invalida!')
            print(f'Digite [s] para CONTINUAR ou [n] para SAIR.')
    return op
menu = opcao(f'Quer continuar? [S/N]')



print()
def teste_int(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valida (número inteiro).

    :msg : texto descrito pelo usuário 
    :num_str: Variável testada
    :num_int : Variável transformada em int()
    :erro : mensagem do tipo de erro
    :return: Retorna valor numérico do tipo inteiro
    """
    while True:
        try:
            num_str = input(msg).strip()
            num_int = int(num_str)
            return num_int
        except Exception as erro:
            print()
            print(f'\nErro de operação => ({erro})')
            print(f'Caractere "{num_str}" não é valido.')

num_inteiro = teste_int(f'Digite um número inteiro: ')
print(f'\nNúmero real = {num_inteiro} => {type(num_inteiro)}')

print()
def teste_float(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valida. Variável testada pode ser
    escrita por "." ou "," exemplo: "4.29" ou "4,29"

    :msg : texto descrito pelo usuário
    :param num_str: Variável testada
    :num_real : Variável transformada em float()
    :erro : mensagem do tipo de erro
    :return: Retorna valor numérico do tipo 'float' (número real)
    """
    while True:
        try:
            num_str = input(msg).strip()
            num_str = num_str.replace(',', '.')
            num_real = float(num_str)
            return num_real
        except Exception as erro:
            print()
            print(f'\nErro de operação => ({erro})')
            print(f'Caractere "{num_str}" não é valido.')


num_float = teste_float(f'Digite um número real: ')
print(f'\nNúmero real = {num_float} => {type(num_float)}')


def moeda(valor, moeda='R$'):
    """
    Formata na impressão um Valor Numérico 'int' em Moeda 'str'
    Ex: Valor Numérico= 3.50 para Moeda= R$3,50

    :param preço: Valor Numérico a ser formatado
    :param moeda: Adiciona simbolo desejado=> Ex: R$
    :return: Retorna valor formatado em Moeda tipo 'str'
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')
valor = float(input(f'Digite o preço: R$'))
valor = moeda(valor)
print(f'Moeda = {valor}')
print(f'{type(valor)}')





