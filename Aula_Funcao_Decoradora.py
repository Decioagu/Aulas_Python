def meu_decorador(funcao): # 2º
    def envelope():
        print('Executa ANTES da função!')
        funcao() # 3.1º
        print('Executa DEPOIS da função!')
    return envelope

def minha_funcao(): # 3.2º
    print('Executar função...')

minha_funcao = meu_decorador(minha_funcao) # decorador
minha_funcao() # 1º

#---------------------------------------------------------------------

def meu_decorador(funcao): # 2º
    def envelope():
        print('Executa ANTES da função!')
        funcao() # 3.1º
        print('Executa DEPOIS da função!')
    return envelope

@ meu_decorador # decorador
def minha_funcao(): # 3.2º
    print('Executar função...')

minha_funcao() # 1º

#---------------------------------------------------------------------

def meu_decorador(funcao): # 2º
    def envelope(*args, **kwargs):
        print('Executa ANTES da função!')
        funcao(*args, **kwargs) # 3.1º
        print('Executa DEPOIS da função!')
    return envelope

@ meu_decorador # decorador
def minha_funcao(x): # 3.2º
    print(f'Executando {x} função...')

minha_funcao('minha') # 1º

'''
Funções decoradoras:
    Em Python, uma função decoradora é uma função que recebe outra função como entrada e retorna uma função modificada. 
    As funções decoradoras são uma ferramenta poderosa que pode ser usada para adicionar funcionalidade a 
    funções existentes sem alterar seu código fonte. Elas são frequentemente usadas para fins como:

    * Adicionar log de depuração ou rastreamento de erros
    * Adicionar autenticação ou autorização
    * Adicionar métricas ou monitoramento
    * Exemplo de função decoradora

# Decorar = Adicionar / Remover/ Restringir / Alterar
# Decoradores são "Syntax Sugar" (Açúcar sintático)

'''
#---------------------------------------------------------------------
# Resumo e funcionamento...
def log_function(func): # 2 => func = minha_funcao(nome_1)
    print('1º = etapa')
    def wrapper(nome_2): # 3 => (nome_2 = nome_1)
        print("2º = Chamada da função:", func.__name__) # 3.1
        print('3º = Parâmetro: ', nome_2) # 3.2
        return func(nome_2) # 3.3 => func = minha_funcao | nome_2 = nome_1
    return wrapper # 2.1

@log_function # 1 => def minha_funcao(nome_1):
def minha_funcao(nome_1): # 4
    print(f"4º = Olá, {nome_1}!") # 4.1 => FIM!!!

minha_funcao('Décio') # 0 => INICIO...

#---------------------------------------------------------------------
'''
    args e kwargs
    *args - desempacotar nº argumentos
    **kwargs - keyword arguments (argumentos nomeados) => para dicionário
'''
# função decoradora
def criar_funcao(func): # --- 2.2
    def interna(*args, **kwargs): # --- 3.2
        print('Vou te decorar')
        for arg in args:
            e_string(arg) # --- 4.1
        resultado = func(*args, **kwargs) # --- 5.1 => (inverte_string('123'))
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado # --- 6.1
    return interna # --- 3.1

@criar_funcao # --- 2.1 (Syntax Sugar) => inverte_string('123')
def inverte_string(string): # --- 5.2
    print(f'*****{inverte_string.__name__}*****')
    return string[::-1] # --- 5.3

# testa parâmetro recebido
def e_string(param): # --- 4.2
    print('+++Teste da função "e_string()"+++')
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('ABCD') # --- 1
print('Final => ',invertida) # --- 6.2

#------------------------------------------------------------------------------

# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

#------------------------------------------------------------------------------
# introspecção
'''
O módulo functools do Python fornece ferramentas úteis para trabalhar com funções 
e objetos chamáveis. Ele oferece diversas funcionalidades para simplificar e otimizar 
seu código, como:

Criar novas funções a partir de funções existentes:
    # partial: permite criar uma nova função a partir de uma função original, 
    pré-definindo alguns argumentos e valores-chave. Isso facilita a reutilização 
    de funções e a criação de funções personalizadas com base em comportamentos existentes.
    # update_wrapper: atualiza o metadados de uma função, como nome, docstring e atributos, 
    para refletir a nova função criada a partir da original.

Trabalhar com sequências:
    # reduce: aplica uma função a dois argumentos cumulativamente aos elementos de 
    uma sequência, reduzindo-a a um único valor. Isso é útil para operações como soma, 
    multiplicação e concatenação.
    # lru_cache: cria um cache de memória para armazenar os resultados de uma função, 
    otimizando seu desempenho para chamadas frequentes com os mesmos argumentos.
Melhorar a organização do código:

    # wraps: decora uma função para que ela mantenha o metadados da função original, 
    como nome, docstring e atributos. Isso facilita a leitura e compreensão do código.
    # total_ordering: decora uma classe para fornecer métodos de comparação ricos, 
    simplificando a implementação de comparações entre objetos da classe.

Outras funcionalidades:
    # partialmethod: converte um método de instância em uma função que pode ser usada 
    sem uma instância específica.
    # singledispatch: implementa despacho único para funções, permitindo escolher 
    qual função implementar com base no tipo do primeiro argumento.
'''


from functools import wraps
'''
wraps: decora uma função para que ela mantenha o metadados da função original, 
como nome, docstring e atributos. Isso facilita a leitura e compreensão do código.
'''
def meu_decorador(funcao): # 2º
    @wraps(funcao)
    def envelope(*args, **kwargs):
        print('Executa ANTES da função!')
        funcao(*args, **kwargs) # 3.1º
        print('Executa DEPOIS da função!')
    return envelope

@ meu_decorador # decorador
def minha_funcao(x): # 3.2º
    print(f'Executando {x} função...')

minha_funcao('minha') # 1º

print(minha_funcao.__name__)

#------------------------------------------------------------------------------

from functools import partial
'''
partial: permite criar uma nova função a partir de uma função original, 
pré-definindo alguns argumentos e valores-chave. Isso facilita a reutilização 
'''
def quadrado_mais_5(x):
  return x * x + 5

quadrado_de_10 = partial(quadrado_mais_5, 10)
print(quadrado_de_10())  # Resultado: 125

#------------------------------------------------------------------------------

from functools import lru_cache
'''
lru_cache: cria um cache de memória para armazenar os resultados de uma função, 
otimizando seu desempenho para chamadas frequentes com os mesmos argumentos.
'''
@lru_cache()
def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)

print(fatorial(5))  # Resultado: 120

#------------------------------------------------------------------------------