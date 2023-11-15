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

try:
    a = 2 / '2'
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro

try:
    a = int('x')
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro

try:
    i = [1,2,3]
    print(f'{i[3]}')
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro

try:
    a = 2 / 0
except Exception as erro:
    print(erro.__class__, erro) # ver class do erro

print()
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

'''
Em Python, a palavra-chave raise é usada para lançar uma exceção. 
Uma exceção é um evento que interrompe o fluxo normal de um programa. 
Ele pode ser causado por um erro de programação, como dividir um número por zero, 
ou por um evento externo, como um usuário fechar uma janela de diálogo.

Onde <motivo> é uma string que fornece o motivo da exceção. 
Por exemplo, a seguinte linha lançará uma exceção 
ValueError com o motivo "O valor é menor que zero":
'''
print()
raise ValueError("O valor é menor que zero")




