'''
O "try" é frequentemente usado para lidar com erros de entrada, estrutura:

try:
  # [Bloco de código que pode gerar um erro]
except [erro1, erro2, ...]:
  # [Bloco de código que é executado se um erro for gerado]
else:
  # [Bloco de código que é executado se nenhum erro for gerado]
finally:
  # [Bloco de código que é sempre executado, independentemente de um erro ser gerado]
'''

try:
    print(x)
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro
#-----------------------------------------------------------------------------------------------

try:
    a = 2 / '2'
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro
#-----------------------------------------------------------------------------------------------

try:
    a = int('x')
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro
#-----------------------------------------------------------------------------------------------

try:
    i = [1,2,3]
    print(f'{i[3]}')
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro
#-----------------------------------------------------------------------------------------------

try:
    a = 2 / 0
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro

#-----------------------------------------------------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    d = a / b
except Exception as erro:
    print(erro.__class__) # ver class do erro
else:
    print(f'{a} / {b} = {d}')
finally:
    print('Sempre sou executado')
#-----------------------------------------------------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    d = a / b

except ZeroDivisionError:
    print('Dividir por zero não existe')
except (ValueError, TypeError, NameError):
    print('Digite apenas valores numéricos inteiro')
else:
    print(f'{a} / {b} = {d}')
finally:
    print('Bloco de código finalizado!!!')
#-----------------------------------------------------------------------------------------------

# Exceção (aula 233 até 235)
'''
Em Python, a palavra-chave raise é usada para lançar uma exceção. 
Uma exceção é um evento que interrompe o fluxo normal de um programa. 
Ele pode ser causado por um erro de programação, como dividir um número por zero, 
ou por um evento externo, como um usuário fechar uma janela de diálogo.

Onde <motivo> é uma string que fornece o motivo da exceção. 
Por exemplo, a seguinte linha lançará uma exceção 
ValueError com o motivo "O valor é menor que zero":
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