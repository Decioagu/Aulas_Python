'''
    Um closure em Python é uma função que pode acessar variáveis mesmo depois que 
    a função que a criou terminou de executar. Em resumo uma função externa retorna 
    para uma função mais interna e isso é possível porque o closure captura as variáveis 
    em seu escopo externo e as mantém em memória mesmo depois que a função externa termina.

    Os closures podem ser usados para implementar uma variedade de padrões de design, incluindo:

    * Funções de ordem superior: Funções de ordem superior são funções 
    que podem receber outras funções como argumentos ou retornar outras 
    funções como resultado. Os closures são essenciais para implementar 
    funções de ordem superior em Python.
    * Decoradores: Decoradores são funções especiais que podem ser 
    usadas para modificar o comportamento de outras funções. Os closures 
    são usados para implementar decoradores em Python.
    * Callbacks: Callbacks são funções que são chamadas quando um evento 
    específico ocorre. Os closures são usados para implementar callbacks em Python.
    
'''
def comprimente(name):
  def interno():
    print(f"Olá, {name}!")
  return interno # retorna função sem executar

agradecer = comprimente("Alice")

agradecer() # Chama a função closure

#---------------------------------------------------------------------

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar # retorna função sem executar

falar_bom_dia = criar_saudacao('Bom dia') 
falar_boa_noite = criar_saudacao('Boa noite') 

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome)) # Chama a função closure
    print(falar_boa_noite(nome)) # Chama a função closure


#---------------------------------------------------------------------

'''Exercício - Adiando execução de funções'''
def fora(x):
    y = x
    def dentro():
        return y
    return dentro # retorna função sem executar


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1()) # Chama a função closure
print(dentro2()) # Chama a função closure

#---------------------------------------------------------------------
'''Exercício - Adiando execução de funções'''
def fora():
    def dentro(y):
        return y * 2
    return dentro # retorna função sem executar


dentro1 = fora()
dentro2 = fora()

print(dentro1(5)) # Chama a função closure
print(dentro2(10)) # Chama a função closure
#---------------------------------------------------------------------

'''Exercício - Adiando execução de funções'''
def concatenar(letra=''):
    letra_final = letra

    def interna(letra_a_concatenar):
        nonlocal letra_final # informa que variável não é local
        letra_final += letra_a_concatenar # não seria possível concatenar variável não local 
        return letra_final # retorna função sem executar
    return interna


alfabeto = concatenar()
print(alfabeto('a')) # Chama a função closure
print(alfabeto('b')) # Chama a função closure
print(alfabeto('c')) # Chama a função closure
print(alfabeto('d')) # Chama a função closure

#---------------------------------------------------------------------