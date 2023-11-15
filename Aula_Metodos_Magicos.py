# aula 236 até 238
'''
    Dunder methods, ou métodos mágicos, são métodos especiais Python que começam e terminam 
    com dois underscores (por exemplo, __str__ ou __add__). Eles são usados para implementar 
    a funcionalidade de operadores e funções built-in.

    Os dunder methods são uma parte poderosa da linguagem Python, pois permitem que você implemente 
    a funcionalidade de operadores e funções built-in para suas próprias classes. Isso permite que 
    você crie classes personalizadas que se comportam da mesma maneira que os objetos built-in do Python.
'''

# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

'''
    lt() é um método especial em Python que implementa o operador de comparação "<". 
    Ele é chamado quando você compara dois objetos usando o operador "<".

    O método lt() deve retornar um valor booleano indicando se o primeiro objeto é 
    menor que o segundo objeto.

    A implementação do método lt() depende do tipo de objeto que está sendo comparado. 
    Por exemplo, o método lt() para números compara os valores dos números. O método lt() 
    para strings compara os valores ASCII dos caracteres nas strings.

    Você pode definir um método lt() para qualquer classe Python. Isso pode ser útil 
    se você quiser que seus objetos sejam comparáveis usando o operador "<".
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, outra_pessoa):
        return self.idade < outra_pessoa.idade

pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1 < pessoa2)

#-----------------------------------------------------------------------------------------------
'''
    call() é um método especial em Python que permite que objetos sejam chamados como funções. 
    Isso significa que você pode passar argumentos para o objeto e ele executará alguma lógica 
    com base nos argumentos passados.

    O método call() é normalmente usado para implementar classes que fornecem funcionalidades 
    semelhantes a funções. Por exemplo, você pode usar o método call() para implementar uma 
    classe que calcula a soma de dois números ou uma classe que converte uma temperatura 
    de Celsius para Fahrenheit.

    Aqui está um exemplo de uma classe Python com um método call() definido:
'''

class Somador:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a + self.b

somador = Somador(1, 2)

print(somador())
#----------------------------------------------------------------------------------------------

'''
    repr() é um método especial em Python que retorna uma representação de string de um objeto. 
    Ele é chamado pela função embutida repr().

    A representação de string retornada pelo método repr() deve ser uma expressão Python válida 
    que possa ser usada para recriar o objeto. Isso significa que a string deve conter todas as 
    informações necessárias para construir um novo objeto do mesmo tipo, incluindo o nome da 
    classe e os valores de todos os atributos.

    O método repr() é normalmente usado para fins de depuração, pois fornece uma representação 
    completa e precisa do objeto. Ele também é usado por alguns contêineres Python, como listas 
    e dicionários, para exibir seus conteúdos.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

pessoa = Pessoa('João', 25)

print(repr(pessoa))
# Pessoa(nome='João', idade=25)

#-----------------------------------------------------------------------------------------------
'''
    str() é um método especial em Python que retorna uma representação de string de um objeto. 
    Ele é chamado pela função embutida str().

    A representação de string retornada pelo método str() deve ser legível para humanos e fornecer 
    uma descrição concisa e informativa do objeto.

    O método str() é normalmente usado para imprimir objetos no console ou para exibir objetos em 
    interfaces gráficas do usuário (GUIs).

    Aqui está um exemplo de uma classe Python com um método str() definido:
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} ({self.idade} anos)'

pessoa = Pessoa('João', 25)

print(pessoa)

#----------------------------------------------------------------------------------------------

# EXEMPLO
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p2!r}')

#----------------------------------------------------------------------------------------------
"""
    O método __eq__() em Python é um método especial, também conhecido como método dunder, 
    que é chamado automaticamente quando o operador == é usado para comparar duas instâncias de uma classe. 
    O método deve retornar um valor booleano, True se as instâncias forem iguais e False se não forem.
"""

class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.nome == other.nome and self.idade == other.idade

p1 = Person('D', 1)
p2 = Person('D', 1)
print(p1 == p2)
#----------------------------------------------------------------------------------------------

