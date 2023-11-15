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
def depurar(func): # --- 2.2
  def interno(*args, **kwargs): # --- 3.2
    print(f"Chamada para {func.__name__=} com argumentos: {args=}, {kwargs=}") # --- 4
    return func(*args, **kwargs) 
  return interno # --- 3.1

@depurar # --- 2.1
def sandacao(name):
  print(f'{sandacao.__name__=}')
  return f"Olá, {name}!"

print(sandacao("Alice")) # --- 1

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