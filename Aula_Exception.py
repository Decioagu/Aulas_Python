
# Exceção (aula 233 até 235)
'''
    Em Python, o comando raise é usado para gerar uma exceção. Uma exceção é um evento que interrompe 
    o fluxo normal de execução de um programa. O comando raise pode ser usado para gerar uma exceção 
    de propósito, como para indicar um erro ou um problema inesperado.
'''

def divide(x, y):
    if y == 0:
        raise ValueError("Divisão por zero")
    return x / y

try:
    print(divide(10, 0))
except ValueError as e:
    print(e)

#-----------------------------------------------------------------------------------------------

'''
    O comando raise também pode ser usado para gerar uma exceção de um tipo personalizado. 
    Para fazer isso, você deve definir uma classe que herda da classe Exception. Por exemplo, 
    o seguinte código define uma classe de exceção personalizada chamada MeuErro:
'''
class MeuErro(Exception):
    def __init__(self, message):
        super().__init__(message)

def divide(x, y):
    if y == 0:
        raise MeuErro("Divisão por zero") # instancia "class MeuErro"
    return x / y

try:
    print(divide(10, 0))
except MeuErro as e:
    print(e)

#-----------------------------------------------------------------------------------------------

# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error