# CONTEXT MANAGER (aula 240)
'''
    Context Manager com classes - Criando e Usando gerenciadores de contexto
    Você pode implementar seus próprios protocolos
    Para criar um context manager, os métodos __enter__ e __exit__
    devem ser implementados.
    O método __exit__ receberá a classe de exceção, a exceção e o
    traceback. Se ele retornar True, exceção no with será
    suprimidas.

    Ex:
    with open('aula149.txt', 'w') as arquivo:
'''

class MyOpen: # class primaria
    def __init__(self, caminho_arquivo, modo): # construtor
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8') # abrir arquivo
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close() # fechar arquivo
        print('-' * 60)
        print(class_exception) # exibe class da exceção
        print(exception_) # exibe tipo da exceção
        print(traceback_) # exibe objeto da exceção
        print('-' * 60)
        return True # ignora a exceção


with MyOpen('aula149.txt', 'w') as arquivo: # Execução (class primaria)
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n', 123) # gerar erro (exceção)
    print('Executando...', arquivo)

#-----------------------------------------------------------------------------------------------
# Context Manager com função - Criando e Usando gerenciadores de contexto - (DECORADOR)

'''
    yield() é uma palavra-chave em Python que é usada para criar funções geradoras. 
    Funções geradoras são funções especiais que podem retornar um valor de cada vez, 
    ao invés de retornarem todos os valores de uma vez. Isso pode ser útil em situações 
    onde você precisa iterar sobre uma grande quantidade de dados, mas não quer armazenar 
    todos os dados na memória de uma vez.

def raiz_quadrada(num):
    for i in range(num):
        yield i ** 2

for raiz in raiz_quadrada(10):
    print(raiz)
'''

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8') # abrir arquivo
        yield arquivo # aguarde a execução (pausa)
    except Exception as e:
        print('Ocorreu erro', e.__class__.__name__)
    finally:
        print('Fechando arquivo')
        arquivo.close() # fecha arquivo


with my_open('aula150.txt', 'w') as arquivo: # Execução (abrir função)
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('Executando...', arquivo)