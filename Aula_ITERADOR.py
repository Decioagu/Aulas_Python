'''
Em Python, um iterador é um objeto que permite percorrer uma coleção de elementos 
sequencialmente, sem expor seus detalhes internos. Imagine um balde cheio de maçãs. 
Um iterador seria como ter uma mão dentro do balde, pegando uma maçã por vez, até 
que todas as maçãs acabem.

Características principais dos iteradores:

    # Iteráveis: Um iterador é sempre um iterável, o que significa que ele pode ser usado 
    em loops for. No entanto, nem todo iterável é um iterador.
    # Método __next__(): Um iterador possui um método especial chamado __next__() 
    (ou next() no Python 2). Esse método retorna o próximo elemento da coleção a 
    cada vez que é chamado.
    # Exceção StopIteration: Quando não há mais elementos na coleção, o método __next__() 
    levanta a exceção StopIteration para indicar o fim da iteração.

Diferença entre iterador e iterável:
    # Iterável: Um objeto que pode ser passado para um loop for. Exemplos: listas, strings, 
    conjuntos, dicionários etc.
    # Iterador: Um objeto que retorna elementos sequencialmente através do método __next__(). 
    Um iterador é sempre um iterável, mas nem todo iterável é um iterador.

Criando iteradores:
    # Função iter(): A função nativa iter() converte um iterável em um iterador.
    # Método __iter__(): Objetos iteráveis definem um método __iter__() que retorna o 
    próprio objeto iterador.
    # Objetos geradores: Funções que usam a palavra-chave yield para gerar valores 
    sequencialmente são consideradas geradores e também são iteradores.

Vantagens dos iteradores:
    # Eficiência de memória: Permitem processar grandes coleções sem carregar tudo 
    na memória de uma vez.
    # Flexibilidade: Possibilitam diferentes formas de iteração, como loops for e 
    usando a função next().
    # Abstração: Escondem os detalhes internos da coleção, permitindo que diferentes 
    tipos de coleções sejam iteradas de forma semelhante.

Exemplos de iteradores:
    # Listas: for item in lista:
    # Strings: for letra in frase:
    # Conjuntos: for elemento in conjunto:
    # Dicionários: for chave, valor in dicionario.items():
    # Objetos geradores: for valor in gerador():

Conclusão:
Os iteradores são um conceito fundamental em Python que permite percorrer coleções de 
forma eficiente e flexível. Ao entender como os iteradores funcionam, você pode escrever 
código mais elegante, legível e performante.
'''

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)