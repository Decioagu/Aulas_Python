# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) Cria a classe - "(metaclass, nome da casse, herança, dicionário ou atributos)"
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# Aula 247 até 249
'''
Uma metaclasse em Python é uma classe especial que controla a criação de outras classes. 
Em outras palavras, ela define como uma classe será criada e quais serão suas propriedades.

Conceito básico:
Imagine as classes como objetos.
As metaclasses são uma camada acima, como uma "classe das classes".
Elas controlam o comportamento da criação de novas classes.

Diferença de classes normais:
As classes normais criam objetos.
As metaclasses criam classes.

Utilização:
As metaclasses são um recurso avançado e nem sempre são necessárias.
São mais utilizadas em situações específicas, como:
Criar classes com comportamento dinâmico.
Implementar singletons.
Realizar validações em tempo de compilação.

Como funcionam:
Uma metaclasse é definida como uma subclasse de type.
Ela define métodos especiais, como __new__ e __init__, que são chamados durante 
a criação de uma classe.
Esses métodos podem modificar a classe antes de ela ser criada.

Vantagens:
Reduzem código repetitivo.
Aumentam a modularidade do código.
Permitem implementar comportamentos avançados.

Desvantagens:
São um recurso complexo e difícil de entender.
Podem tornar o código mais difícil de depurar.

Exemplos de uso:
Classes abstratas.
Singletons.
Classes dinâmicas com atributos personalizados.
'''
class ValidadorDeAtributos(type):
    def __new__(mcs, name, bases, attributes):
        print('EXECUTADO...')
        cls = super().__new__(mcs, name, bases, attributes)
        return cls


class Pessoa(metaclass=ValidadorDeAtributos): # executado automaticamente 
    nome_da_class = 'Décio'

nome  = Pessoa()
print(nome)
print(nome.nome_da_class)

#-----------------------------------------------------------------------------------------------

def meu_repr(self): # Aula_Metaclasses.py
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type): # Metaclasses
    def __new__(mcls, name, bases, dict):
        print('METACLASS NEW')
        cls = super().__new__(mcls, name, bases, dict)
        cls.exemplo = 1234 # atributo de class
        cls.__repr__ = meu_repr # Aula_Metaclasses.py
        return cls

        # if 'falar' not in cls.__dict__ or \
        #         not callable(cls.__dict__['falar']):
        #     raise NotImplementedError('Implemente falar')

        # return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        # if 'nome' not in instancia.__dict__:
        #     raise NotImplementedError('Crie o attr nome')

        return instancia


class Pessoa(metaclass=Meta):
    # falar = 123

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        # self.nome = nome

    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Luiz')
print(p1.exemplo)
print(Pessoa.exemplo)
p1.falar()

