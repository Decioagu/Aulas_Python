'''
    A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza 
    o código em torno de objetos. Um objeto é uma entidade que pode ser usada para armazenar 
    dados e realizar operações. Os objetos são criados a partir de classes, que são modelos 
    que definem os atributos e métodos de um objeto.

    A POO é um paradigma poderoso que pode ser usado para criar programas mais robustos, 
    flexíveis e fáceis de manter.
    
    Definições de class:
    # Classes: Uma classe é um modelo que define os atributos e métodos de um objeto.
    # Objetos: Um objeto é uma instância de uma classe e pode ter atributos e métodos 
        específicos.
    # Atributos: Os atributos são dados que são armazenados em um objeto.
    # Métodos: Os métodos são operações (ações) que podem ser realizadas em um objeto.

    Os conceitos básicos de POO são:
    # Encapsulamento: O encapsulamento é um mecanismo que permite esconder os detalhes 
        internos de uma classe e expor apenas as interfaces necessárias para interagir com o objeto.
    # Herança: A herança é um mecanismo que permite criar novas classes com base em 
        classes existentes. A classe filha herda os atributos e métodos da classe pai, 
        o que facilita a reutilização de código e a criação de hierarquias de classes.
    # Polimorfismo: O polimorfismo é a capacidade de um objeto se comportar de 
        diferentes maneiras, dependendo do contexto em que é utilizado.
'''
class Nome:
    def __init__(self): # iniciar classe (construtor)_0
        self.nome = 'Décio'

pessoa_01 = Nome() # adicionar dados (atributo)
pessoa_02 = Nome() # adicionar dados (atributo)

print(f'Class: {pessoa_01.nome}') # acessar dados (atributo)
print(f'Class: {pessoa_02.nome}') # acessar dados (atributo)
print(f'Class: {pessoa_01 == pessoa_02}') # Class: False

pessoa_03 = 'Décio'
pessoa_04 = 'Décio'
print(f'Objeto: {pessoa_03}')
print(f'Objeto: {pessoa_04}')
print(f'Objeto: {pessoa_03 == pessoa_04}') # Objeto: True

#-----------------------------------------------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade): # iniciar classe (construtor)
        self.nome = nome # atributo
        self.idade = idade # atributo

    def falar(self): # método (ação)
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def maior_de_idade(self):
        return f'Você é MAIOR de idade' if self.idade > 18 else f'Você é MENOR de idade'


pessoa1 = Pessoa("João", 30) # adicionar dados (atributo)
pessoa2 = Pessoa("Maria", 17) # adicionar dados (atributo)

print(f'{pessoa1.nome}:') # acessar dados (atributo)
pessoa1.falar() # acessar método (ação)
Pessoa.falar(pessoa1) # acessar método (ação)
print(pessoa1.maior_de_idade()) # acessar método (ação)
print(Pessoa.maior_de_idade(pessoa1)) # acessar método (ação)

print('<======>')
print(f'{pessoa2.nome}:') # acessar dados (atributo)
pessoa2.falar() # acessar método (ação)
Pessoa.falar(pessoa2) # acessar método (ação)
print(pessoa2.maior_de_idade()) # acessar método (ação)
print(Pessoa.maior_de_idade(pessoa2)) # acessar método (ação)

#-----------------------------------------------------------------------------------------------
# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False): # iniciar classe
        self.nome = nome # atributo
        self.filmando = filmando # atributo

    def filmar(self): # método (ação)

        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return 

        print(f'{self.nome} está filmando...')
        self.filmando = True # armazena estado

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
print('Canon esta filmando =', c1.filmando)
print('Sony esta filmando =', c2.filmando)
c2.filmando = True # alterando valor do atributo dentro da class
print('Sony esta filmando =', c2.filmando)

#-----------------------------------------------------------------------------------------------
# Atributos de classe
class Pessoa:
    ano_atual = 2022 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # uso do atributo da classe


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual) # atributo da classe
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print('-' * 20)
Pessoa.ano_atual = 1000 # alterar valor do atributo
print(Pessoa.ano_atual) # atributo da classe
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print('-' * 20)

#-----------------------------------------------------------------------------------------------
# "__dict__" ou "vars" para atributos de instância
class Pessoa:
    ano_atual = 2022 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # uso do atributo da classe


p1 = Pessoa('João', 35)

print(p1.__dict__) # mostra um dicionario da instancia p1
p1.__dict__['nome'] = 'Décio' # altera valor 
print(p1.nome)
p1.__dict__['sexo'] = 'Masculino' # cria novo atributo (não existe na class)
print(vars(p1)) #  vars(p1) = p1.__dict__
print(p1.sexo) # ver novo atributo
del p1.__dict__['sexo']
print(p1.__dict__) # ou vars(p1)
novo_dicionario = vars(p1).copy() # copia rasa
print(f'{novo_dicionario=}')
novo_dicionario['nome'] = 'João' # alterar nome
print(f'{p1.__dict__=}')
print(f'{novo_dicionario=}')

#-----------------------------------------------------------------------------------------------
# Métodos de classe (DECORADOR)
'''
    Em Python, é um decorador que é usado para definir um método dentro de uma 
    classe que opera no nível de classe em vez do nível de objeto (instância). 
    Isso significa que o método pode acessar e modificar atributos de classe e 
    pode ser chamado diretamente usando o nome da classe ou em um objeto da classe.
    # @classmethod

    # Métodos de classe + factories (fábricas)
    # São métodos onde "self" será "cls", ou seja,
    # ao invés de receber a instância no primeiro
    # parâmetro, receberemos a própria classe.
'''

class Numero:
    valor = 5  # atributo de classe

    def __init__(self, num):
        self.num = num

    def metodo(self): # método (ação)
        print(self.num * self.valor)

    @classmethod # método de classe
    def metodo_de_classe(cls, novo_num): # receberemos a própria class
        cls.valor = novo_num

p1 = Numero(10)
p1.metodo()
Numero.metodo_de_classe(10)
p1.metodo() # autera atributo de classe
p2 = Numero(10)
p2.metodo()

print('<==========================================================>')

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome): # receberemos a própria class
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade): # receberemos a própria class
        return cls('Anônima', idade)
    
    @classmethod
    def criar_nome_idade(cls, nome, idade): # receberemos a própria class
        return cls(nome, idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(25)
p4 = Pessoa.criar_nome_idade('Décio', 41)
print(Pessoa.ano)
Pessoa.metodo_de_classe(p1)
print('-' * 30)
print(p2.nome, p2.idade)
print('-' * 30)
print(p3.nome, p3.idade)
print('-' * 30)
print(p4.nome, p4.idade)
#-----------------------------------------------------------------------------------------------
# aulas 209 e 210 (DECORADOR)
'''
    Em Python, é um decorador que é usado para definir um método estático dentro de uma 
    classe. Um método estático se comporta como uma função regular, mas está associado 
    a uma classe. Aqui estão as principais características dos métodos estáticos.
    # @staticmethod

    # método vs @classmethod vs @staticmethod
    # método - self, método de instância
    # @classmethod - cls, método de classe
    # @staticmethod - método estático (❌self, ❌cls)
'''
class Connection:
    def __init__(self, host='localhost'): # construtor
        self.host = host
        self.user = None
        self.password = None

    # adiciona valor em "self.user" 
    def set_user(self, user): # método (enviar valor)
        self.user = user

    # adiciona valor em "self.password"
    def set_password(self, password): # método (enviar valor)
        self.password = password

    # adiciona valor em "self.user" e "self.password" 
    @classmethod
    def create_with_auth(cls, user, password): # método de classe 
        connection = cls() # acesso ao construtor
        connection.user = user # acesso ao self.user
        connection.password = password # acesso ao self.password 
        return connection # necessário retornar a instancia ao objeto

    @staticmethod
    def log(msg): # método estático
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)

print('Uso de método:')
c1 = Connection()
c1.set_user('Luiz')
c1.set_password('02468')
print(c1.user)
print(c1.password)
print('-' * 100)

print('Uso de método de class:')
c2 = Connection.create_with_auth('Maria', '13579')
print(c2.user)
print(c2.password)
print('-' * 100)

print('Uso de método etático:')
print(Connection.log('Essa é a mensagem de log'))
#-----------------------------------------------------------------------------------------------
# (DECORADOR)
'''
    # @property - um getter no modo Pythônico
    # getter - um método para obter um atributo
    # cor -> get_cor()
    # modo pythônico - modo do Python de fazer coisas
    # @property é uma propriedade do objeto, ela
    # é um método que se comporta como um
    # atributo 🤯 🤯 🤯
    # Geralmente é usada nas seguintes situações:
    # - como getter
    # - p/ evitar quebrar código cliente
    # - p/ habilitar setter
    # - p/ executar ações ao obter um atributo
    # Código cliente - é o código que usa seu código

    Em Python, uma @property é um decorador que transforma um método em uma 
    propriedade de uma classe. Isso permite que o método seja acessado como 
    um atributo, sem a necessidade de chamá-lo como uma função.
'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self): # obter um valor (getter)
        print('PROPERTY')
        return self.cor_tinta

    @property # obter um valor (getter)
    def cor_tampa(self):
        print('PROPERTY')
        return 123456

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

print('<==========================================================>')

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self): # método (obter valor)
        print('GET COR')
        return self.cor


caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())

#-----------------------------------------------------------------------------------------------
# aula 212 e 213 (DECORADOR)
'''
    # @property + @setter - getter e setter no modo Pythônico
    # - como getter
    # - p/ evitar quebrar código cliente
    # - p/ habilitar setter
    # - p/ executar ações ao obter um atributo
    # Atributos que começar com um ou dois underlines
    # não devem ser usados fora da classe.

    Embora o Python não tenha decoradores @setter integrados, ele fornece uma 
    abordagem mais Pythonic para controlar o acesso e a validação de atributos 
    usando propriedades.
    Propriedades:
    As propriedades permitem definir um getter (para recuperar valores de atributo) 
    e um setter opcional (para modificar valores de atributo) com o decorador. Aqui 
    está a estrutura básica:@property.setter
'''
class Caneta:
    def __init__(self):
        # private protected
        self.cor = None

    @property
    def cor(self): # getter (solicita valores)
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor): # setter (envia valores)
        print('ESTOU NO SETTER')
        self._cor = valor

    @cor.deleter # del (deleta propriedade)
    def cor(self):
        del self._cor

caneta = Caneta()
print(caneta.cor) # getter (solicita valores)
caneta.cor = 'Rosa' # setter (envia valores)
print(caneta.cor) # getter (solicita valores)
del caneta.cor
#-----------------------------------------------------------------------------------------------
# ENCAPSULAMENTO (aula 214)
'''
    # Encapsulamento (modificadores de acesso: public, protected, private):
    ======> OBS: Python NÃO TEM modificadores de acesso <======
    # Mas podemos seguir as seguintes convenções
    #   +(sem underline) = public
    #       pode ser usado em qualquer lugar
    # _ (um underline) = protected
    #       não DEVE ser usado fora da classe
    #       ou suas subclasses.
    # __ (dois underlines) = private
    #       "name mangling" (desfiguração de nomes) em Python
    #       _NomeClasse__nome_attr_ou_method
    #       só DEVE ser usado na classe em que foi
    #       declarado.
'''
from functools import partial

class Foo:
    def __init__(self): # public
        self.public = 'isso é público' # atributo
        self._protected = 'isso é protegido' # atributo
        self.__private = 'isso é private' # atributo

    def metodo_publico(self): # método public
        self._metodo_protected() # acesso método protected
        self.__metodo_private() # acesso método private
        return 'metodo_publico'

    def _metodo_protected(self): # método protected
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self): # método private
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
print(f.public) # acesso atributo
print(f.metodo_publico()) # acesso método public
#-----------------------------------------------------------------------------------------------
# Relações entre classes: (ASSOCIAÇÃO) - (DECORADOR)
'''
    # Relações entre classes: associação, agregação e composição
    # Associação é um tipo de relação onde os objetos
    # estão ligados dentro do sistema.
    # Essa é a relação mais comum entre objetos e tem subconjuntos
    # como agregação e composição (que veremos depois).
    # Geralmente, temos uma associação quando um objeto tem
    # um atributo que referencia outro objeto.
    # A associação não especifica como um objeto controla
    # o ciclo de vida de outro objeto.
'''

class Escritor:
    def __init__(self, nome_fescrotor) -> None:
        self.nome_fescrotor = nome_fescrotor
        self._ferramenta = None

    @property # (getter)
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter # (setter)
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome_ferramenta):
        self.nome_ferramenta = nome_ferramenta

    def escrever(self):
        return f'{self.nome_ferramenta} está escrevendo'


escritor = Escritor('Luiz')
print(escritor.ferramenta, '\n') # classe "escritror", método "@ferramenta.setter"

caneta = FerramentaDeEscrever('Caneta Bic')
print(caneta.escrever(), '\n') # classe "FerramentaDeEscrever",  método "escrever"

maquina_de_escrever = FerramentaDeEscrever('Máquina')
print(maquina_de_escrever.escrever(), '\n') # classe "FerramentaDeEscrever",  método "escrever"

# classe "escritror", método " @property" => recebe método da classe "FerramentaDeEscrever"
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever(), '\n')

# classe "escritror", método " @property" => recebe método da classe "FerramentaDeEscrever"
escritor.ferramenta = maquina_de_escrever
print(escritor.ferramenta.escrever(), '\n') 

#-----------------------------------------------------------------------------------------------
# Relações entre classes: (AGREGAÇÃO):
'''
    # Relações entre classes: associação, agregação e composição
    # Agregação é uma forma mais especializada de associação
    # entre dois ou mais objetos. Cada objeto terá
    # seu ciclo de vida independente.
    # Geralmente é uma relação de um para muitos, onde um
    # objeto tem um ou muitos objetos.
    # Os objetos podem viver separadamente, mas pode
    # se tratar de uma relação onde um objeto precisa de
    # outro para fazer determinada tarefa.
    # (existem controvérsias sobre as definições de agregação).
'''
class Carrinho:
    def __init__(self):
        self._produtos = []

    # adicionar produtos na lista "self._produtos" vindos da "class Produto" 
    def inserir_produtos(self, *produtos): 
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

    def total(self):
        return sum([p.preco for p in self._produtos])


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho() # criar carrinho "class Carrinho"
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20) # criar produtos "class Produto"
carrinho.inserir_produtos(p1, p2) # adicionar produtos no carrinho da "class Produto"
carrinho.listar_produtos() # adicionar produtos no carrinho
print(carrinho.total()) # somar valores dos produtos

#-----------------------------------------------------------------------------------------------
# Relações entre classes: (COMPOSIÇÃO):
'''
    # Relações entre classes: associação, agregação e composição
    # Composição é uma especialização da agregação.
    # Mas nela, quando o objeto "pai" for apagado, todas
    # as referências dos objetos filhos também são
    # apagadas.
'''
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    # adiciona endereço com uso da "class Endereco"
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # aciona "class Endereco"

    # adiciona endereço sem uso de classe
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    # lista todos os endereços
    def listar_enderecos(self):
        print()
        print('-' * 50)
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self): # ativa automaticamente quando "class Cliente" é apagado 
        print()
        print('-' * 50)
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    '''
        O método del é um método especial em Python que é chamado quando um objeto é deletado. 
        Ele é chamado automaticamente pelo coletor de lixo do Python, quando o objeto não é 
        mais referenciado por nenhuma outra variável.
    '''

    def __del__(self): # ativa quando programa encerrado
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1 # apagar cliente
# OBS: o endereco_externo não foi apagado pois não foi criado pela "class Endereco"

print()
print('-' * 50)
print(endereco_externo.rua, endereco_externo.numero) 
print()
print('---------------------- AQUI TERMINA MEU CÓDIGO ----------------------')
print()

#-----------------------------------------------------------------------------------------------
# HERANÇA SIMPLES
'''
    # Herança simples (Relações entre classes)
    # Associação -> usa, 
    # Agregação -> tem
    # Composição -> É dono de, 
    # Herança -> É um
    #
    # Herança vs Composição
    #
    # Classe principal (Pessoa)
    #   -> super class, base class, parent class
    # Classes filhas (Cliente)
    #   -> sub class, child class, derived class
'''
class Pessoa: # Classe principal
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa): # Classe filha
    def falar_nome_classe(self):
        print('classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa): # Classe filha
    cpf = 'cpf aluno'


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe() # esta usando método da "class Cliente"
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe() # esta usando método da "class Pessoa"
print(a1.cpf)

print('<==========================================================>')

class Animal: # Classe principal
    def __init__(self, nome, cor): # construtor
        self.nome = nome
        self.cor = cor

    def falar(self):
        print("Esse animal faz:", end=' ')


class Gato(Animal): # Classe filha
    def __init__(self, nome_gato, cor_gato, raça_gato):
        super().__init__(nome_gato, cor_gato) # construtor da "class Animal"
        self.raca = raça_gato # atributo da class "class Gato"

    def miar(self): # método da "class Gato"
        super().falar() # uso método "class Animal"
        print("Miau...")


class Cachorro(Animal): # Classe filha
    def __init__(self, nome_cachorro, cor_cachorro, raça_cachorro):
        super().__init__(nome_cachorro, cor_cachorro) # construtor da "class Animal"
        self.raca = raça_cachorro # atributo da class "class Cachorro"

    def latir(self): # método da "class Cachorro"
        super().falar() # uso método "class Animal"
        print("Au au...")


gato = Gato("Gato", "Cinza", "Siamês")
cachorro = Cachorro("Cachorro", "Marrom", "Pastor Alemão")

print(gato.nome) # Gato
print(gato.cor) # Cinza
print(gato.raca) # Cinza
gato.miar() # Miau...
print('-' * 50)
print(cachorro.nome) # Cachorro
print(cachorro.cor) # Marrom
print(cachorro.raca) # Pastor Alemão
cachorro.latir() # Au au...
print()
# gato.falar()
# cachorro.falar()

print('<==========================================================>')

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodoA(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodoB(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodoC(self):
        print('C')

a = A('Atributo de A')
b = B('Atributo de B', 'Qualquer')
c = C('Atributo de C', 'Qualquer')

print('-' * 50)
print(a.atributo) 
print(b.atributo) # Herança da "class A"
print(c.atributo) # Herança da "class A"

print('-' * 50)
print(c.atributo_a) # Herança da "class A"
print(c.atributo_b) # Herança da "class B"
print(c.atributo_c)

print('-' * 50)
a.metodoA()

print('-' * 50)
b.metodoA() # Herança da "class A"
b.metodoB()

print('-' * 50)
c.metodoA() # Herança da "class A"
c.metodoB() # Herança da "class B"
c.metodoC()

# print('-' * 50)
# print(C.mro())
# print(B.mro())
# print(A.mro())

#-----------------------------------------------------------------------------------------------
# HERANÇA MÚLTIPLA
'''
    # Herança Múltipla - Python Orientado a Objetos
    # Quer dizer que no Python, uma classe pode estender
    # várias outras classes.
    # Herança simples:
    # Animal -> Mamifero -> Humano -> Pessoa -> Cliente
    # Herança múltipla e mixins
    # Log -> FileLog
    # Animal -> Mamifero -> Humano -> Pessoa -> Cliente
    # Cliente(Pessoa, FileLog)
    #
    # A, B, C, D
    # D(B, C) - C(A) - B(A) - A
    #
    # método -> falar
    #           A
    #         /   \
    #        B     C
    #         \   /
    #           D
    #
    # Python 3 usa C3 superclass linearization
    # para gerar o mro.
    # Você não precisa estudar isso (é complexo)
    # https://en.wikipedia.org/wiki/C3_linearization
    #
    # Para saber a ordem de chamada dos métodos
    # Use o método de classe Classe.mro()
    # Ou o atributo __mro__ (Dunder - Double Underscore)
'''

class A:
    ...
    def quem_sou(self):
        print('A')


class B(A):
    ...
    # def quem_sou(self):
    #     print('B')


class C(A):
    ...
    # def quem_sou(self):
    #     print('C')

class D(B, C): # a ordem importa "class D(B, C)" ou "class D(C, B)"
    ...
    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou()
# caminho a percorrer
print(D.mro()) # ou print(D.__mro__)

'''
    MRO, ou Method Resolution Order, é a ordem em que os métodos são pesquisados em uma hierarquia 
    de classes em Python. É especialmente útil em Python porque Python suporta herança múltipla.
    O MRO é determinado por um algoritmo chamado C3 linearização. O algoritmo C3 linearização garante que:

    # Os métodos de uma classe são pesquisados antes dos métodos de suas superclasses.
    # Se uma classe herda de várias classes, os métodos são pesquisados na ordem da esquerda 
      para a direita.
    # Nenhuma classe é visitada mais de uma vez.

    O MRO pode ser obtido usando o método mro() ou o atributo __mro__ de uma classe. 
    O método mro() retorna uma lista de classes, enquanto o atributo __mro__ retorna uma tupla de classes.
'''
#-----------------------------------------------------------------------------------------------
# ABSTRAÇÃO (aula 229 e 230) - (DECORADOR)
'''
    # Classes abstratas - Abstract Base Class (abc)
    # ABCs são usadas como contratos para a definição
    # de novas classes. Elas podem forçar outras classes
    # a criarem métodos concretos. Também podem ter
    # métodos concretos por elas mesmas.
    # @abstractmethods são métodos que não têm corpo.
    # As regras para classes abstratas com métodos
    # abstratos é que elas NÃO PODEM ser instânciadas
    # diretamente.
    # Métodos abstratos DEVEM ser implementados
    # nas subclasses (@abstractmethod).
    # Uma classe abstrata em Python tem sua metaclasse
    # sendo ABCMeta.
    # É possível criar @property @setter @classmethod
    # @staticmethod e @method como abstratos, para isso
    # use @abstractmethod como decorator mais interno.

    O decorador @abstractmethod em Python é usado para declarar métodos abstratos. 
    Um método abstrato é um método que não possui uma implementação, mas deve ser 
    implementado por todas as subclasses da classe que o declara.
'''
from abc import ABC, abstractmethod

class Log(ABC): # classe principal
    # OBS: uma class abstrata não deve ser instanciada diretamente
    @abstractmethod 
    def _log(self, msg): # método abstrato
        ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log): # subclasse
    def _log(self, msg): # implementação do método abstrato 
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('1111') # uso método "class Log"
l.log_success('9999') # uso método "class Log"

print('<==========================================================>')
# (DECORADOR)
from abc import abstractmethod

class Animal:
    # OBS: uma class abstrata não deve ser instanciada diretamente
    @abstractmethod
    def son_do_animal(self): # método abstrato
        pass

class Cachorro(Animal):
    def son_do_animal(self): # implementação do método abstrato 
        print("Au au!")

class Gato(Animal):
    def son_do_animal(self): # implementação do método abstrato 
        print("Miau!")

c = Cachorro() # criar instancia
c.son_do_animal() # iniciar método
print('-' * 25)
g = Gato()
g.son_do_animal()

#-----------------------------------------------------------------------------------------------

# POLIMORFISMO - (DECORADOR)
'''
    # Polimorfismo em Python Orientado a Objetos
    # Polimorfismo é o princípio que permite que
    # classes deridavas de uma mesma superclasse
    # tenham métodos iguais (com mesma assinatura)
    # mas comportamentos diferentes.
    # Assinatura do método = Mesmo nome e quantidade
    # de parâmetros (retorno não faz parte da assinatura)
    # Opinião + princípios que contam:
    # Assinatura do método: nome, parâmetros e retorno iguais
    # SO"L"ID
    # Princípio da substituição de liskov
    # Objetos de uma superclasse devem ser substituíveis
    # por objetos de uma subclasse sem quebrar a aplicação.
    # Sobrecarga de métodos (overload)  🐍 = ❌
    # Sobreposição de métodos (override) 🐍 = ✅

    Polimorfismo em Python é a capacidade de um objeto assumir várias formas. 
    Em palavras simples, o polimorfismo permite-nos realizar a mesma ação de muitas 
    maneiras diferentes. Por exemplo, Jessa atua como funcionária quando está no escritório. 
    No entanto, quando está em casa, ela atua como esposa.
'''
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod # método abstrato
    def enviar(self) -> bool: # " -> bool" informa tipo de retorno desejado (NÃO OBRIGATÓRIO)
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: # implementação do método abstrato 
        print('E-mail: enviando - ', self.mensagem)
        return True # retorno método

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool: # implementação do método abstrato 
        print('SMS: enviando - ', self.mensagem)
        return False # retorno método


def notificar(notificacao: Notificacao): # Polimorfismo
    # print(notificacao.enviar())
    notificacao_enviada = notificacao.enviar() 

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)

print('<==========================================================>')

# sem uso da biblioteca "from abc import ABC, abstractmethod"
class Animal:
    def som(self): # método abstrato
        raise NotImplementedError()

class Cachorro(Animal):
    def som(self): # implementação do método abstrato 
        print("Au au!")

class Gato(Animal):
    def som(self): # implementação do método abstrato 
        print("Miau!")

def som_dos_animais(animais): # Polimorfismo
    for animal in animais:
        # print(animal)
        animal.som()

# c = Cachorro()
# c.som()
# g = Gato()
# g.som()
# Criar uma lista de animais
animals = [Cachorro(), Gato()]
# Fazer todos os animais fazerem som
som_dos_animais(animals)

print('<==========================================================>')

# (DECORADOR)
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def som(self): # método abstrato
        pass

    def falar(self):
        print("Esse animal faz:", end=' ')

class Cachorro(Animal):
    def som(self): # implementação do método abstrato 
        self.falar() # usar "método falar" HERANÇA
        print("Au au!")

class Gato(Animal):
    def som(self): # implementação do método abstrato 
        super().falar() # usar "método falar" HERANÇA
        print("Miau!")

def som_dos_animais(animal): # Polimorfismo
    animal.som()

c = Cachorro()
som_dos_animais(c)
g = Gato()
som_dos_animais(g)
#-----------------------------------------------------------------------------------------------

# Função decoradora com decoradores class - (DECORADOR)
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls): # função decoradora 
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr # class
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr # class
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)
#-----------------------------------------------------------------------------------------------

# Funções decoradoras e decoradores com métodos - (DECORADOR)
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls): # função decoradora
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo): # função decoradora
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr # class
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr # class
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta # método
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome()) # método
print(marte.falar_nome()) # método
#-----------------------------------------------------------------------------------------------
# MÉTODO __call__ (aula 245)
'''
    # Método especial __call__
    # callable é algo que pode ser executado com parênteses
    # Em classes normais, __call__ faz a instância de uma
    # classe "callable".
'''

class CallMe:
    def __init__(self, phone):
        self.phone = phone # atributo

    def __call__(self, nome):
        print(nome, 'está ligando para telefone', self.phone)
        return 'Aguarde ser atendido...'


call1 = CallMe('99001-1234') # chama a class
retorno = call1('Luiz Otávio') # executa método __call__ na class
print(retorno)
#-----------------------------------------------------------------------------------------------

# Classes decoradoras - (DECORADOR)
class Multiplicar:
    def __init__(self, func):
        self.func = func # função soma
        self._multiplicador = 10

    def __call__(self, *args, **kwargs): # chama objeto
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador 
        


@Multiplicar # class decoradora
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)

print('<==========================================================>')

# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func): # chamar função
        def interna(*args, **kwargs): # chama os objetos
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador # resposta
        return interna


@Multiplicar(2) # executar "class Multiplicar"
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)

#-----------------------------------------------------------------------------------------------
# DATACLASSE (aula 265)
'''
    Dataclasses são uma nova funcionalidade introduzida no Python 3.7. Elas são uma forma simplificada 
    de criar classes que representam dados. Dataclasses são baseadas em classes regulares do Python, 
    mas fornecem algumas funcionalidades adicionais que as tornam mais fáceis de usar.

    Dataclasses geram automaticamente os seguintes métodos especiais para você:

    * __init__(): Este método é chamado quando uma nova instância da classe é criada.
    * __repr__(): Este método retorna uma string que representa a instância da classe.
    * __eq__(): Este método compara duas instâncias da classe para determinar se elas são iguais.

    class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Person(nome={self.nome}, idade={self.idade})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.nome == other.nome and self.idade == other.idade

    # doc: https://docs.python.org/3/library/dataclasses.html
'''
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa('Luiz', 30)
p2 = Pessoa('Luiz', 30)
p3 = Pessoa('Luiz', 10)
print(p1)
print(p2)
print(p2)
p1.nome = 'Décio'
print(p1 == p2)
print(p1 == p3)

print('<==========================================================>')

from dataclasses import dataclass

@dataclass(frozen=True) # frozen=True não permite alteração dos atributos
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa('Luiz', 30)
p2 = Pessoa('Luiz', 30)
p3 = Pessoa('Luiz', 10)
print(p1)
print(p2)
print(p2)
p1.nome = 'Décio'
print(p1 == p2)
print(p1 == p3)

print('<==========================================================>')

from dataclasses import dataclass

@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome) # ordenar
    print(ordenadas)

print('<==========================================================>')

from dataclasses import asdict, astuple, dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys()) # dicionario
    print(asdict(p1).values()) # dicionario
    print(asdict(p1).items()) # dicionario
    print(astuple(p1)[0]) # tupla

print('<==========================================================>')

from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent' # imutável
    idade: int = 100 # imutável
    enderecos: list[str] = field(default_factory=list) # mutável devido ao "field"

if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)

#-----------------------------------------------------------------------------------------------
# NAMEDTUPLES (aula 271)
# ver Aula_TUPLA.py (aula 271)
'''
    # Usamos namedtuples para criar classes de objetos que são apenas um
    # agrupamento de atributos, como classes normais sem métodos, ou registros de
'''

from typing import NamedTuple

class Carta(NamedTuple):
    naipe: str = 'NAIPE'
    valor: str = 'VALOR'

espadas = Carta('ESPADAS', 'DAMA')

print(espadas)

print(espadas[0])
print(espadas.naipe)

print(espadas[1])
print(espadas.valor)

dicionario = espadas._asdict() # formatação para dicionario
print (f'{dicionario=}')

print(espadas._fields) # ver valor padrão
print(espadas._field_defaults) # ver valor padrão
#-----------------------------------------------------------------------------------------------

'''
    # Implementando o protocolo do "Iterator" em Python
    # Essa é apenas uma aula para introduzir os protocolos de collections.abc no
    # Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
    # estrutura usada nessa aula.
    # https://docs.python.org/3/library/collections.abc.html

    A classe abstrata Sequence define uma interface comum para sequências em Python, 
    como listas, tuplas e strings. Isso significa que qualquer classe que implementa 
    a interface Sequence deve fornecer os métodos definidos nela,
    como __len__, __getitem__, __iter__ e __contains__.

    * __len__(): Retorna o comprimento da sequência.
    * __getitem__(): Retorna o item na posição especificada.
    * __setitem__(): Define o item na posição especificada.
    * __delitem__(): Remove o item na posição especificada.
    * __contains__(): Verifica se a sequência contém o item especificado.
    * __iter__(): Retorna um iterador para a sequência.
    * __reversed__(): Retorna um iterador para a sequência reversa.

    Além desses métodos abstratos, a classe Sequence também define alguns métodos mixin que podem ser sobrescritos, mas não são necessários para implementar a interface Sequence. Esses métodos incluem:

    * index(): Obtém o índice de um elemento na sequência.
    * count(): Conta o número de vezes que um elemento aparece na sequência.

    Alguns exemplos de classes que implementam a interface Sequence incluem:

    * list(): Listas são sequências mutáveis que podem ser criadas usando a função list().
    * tuple(): Tuplas são sequências imutáveis que podem ser criadas usando a função tuple().
    * str(): Strings são sequências imutáveis de caracteres que podem ser criadas usando a função str().
'''
from collections.abc import Sequence

class MySequence(Sequence):

  def __init__(self, *data): # construtor
    self.data = list(data)

  def __len__(self): # Retorna o comprimento da sequência.
    return len(self.data)
  
  def __iter__(self): # Retorna um iterador para a sequência.
    return iter(self.data)

  def __getitem__(self, index): # Retorna o item na posição especificada.
    return self.data[index]

  def __contains__(self, item): # Verifica se a sequência contém o item especificado.
    for element in self.data:
      if element == item:
        return True
    return False

my_sequence = MySequence("a", "b", "c") # def __init__(self, data):
print('-' * 45)

print(my_sequence) # endereço de memória
print('-' * 45)

print('Quantidade de elementos = ', len(my_sequence)) # def __len__(self):
print('-' * 45)

print(my_sequence.data) # def __init__(self, data):
print('-' * 45)

print(my_sequence[0]) # def __getitem__(self, index):
print(my_sequence[1]) # def __getitem__(self, index):
print(my_sequence[2]) # def __getitem__(self, index):
print('-' * 45)

print("z" in my_sequence) # def __contains__(self, item):
print("a" in my_sequence) # def __contains__(self, item):
print('-' * 45)

print(*my_sequence) # def __getitem__(self, index):
print('-' * 45)

print('Uso de "for":')
for i in my_sequence: # def __getitem__(self, index):
  print(i)
print('----------')
print('Uso de "for":')
for i in my_sequence: # def __getitem__(self, index):
  print(i)
print('-' * 45)

print('<==========================================================>')

from collections.abc import Sequence

class MySequence(Sequence):

    def __init__(self): # construtor
        self._items = []

    def __len__(self): # retorna o comprimento da sequência
        return len(self._items)
    
    def __iter__(self): # retorna um iterador para a sequência
        for item in self._items:
            yield item
    
    def append(self, *values): # adicionar valores na sequência
        for value in values:
            self._items.append(value) 

    def __getitem__(self, index): # retorna o item na posição especificada
        return self._items[index]

    def __setitem__(self, index, item): # atualiza um elemento da sequência pelo seu índice
        self._items[index] = item

    def __delitem__(self, index): # deleta (apaga) um elemento da sequência pelo seu índice
        del self._items[index]

    def __contains__(self, item): # verifica se a sequência contém o item especificado
        return item in self._items  

    def __reversed__(self): # retornar sequencia na ordem inversa
        for item in reversed(self._items):
            yield item

sequence = MySequence() # def __init__(self):

sequence.append('a') # def append(self, *values):
sequence.append('b') # def append(self, *values):
sequence.append('c') # def append(self, *values):
sequence.append('d') # def append(self, *values):
print('-' * 45)

print('Total elementos na sequencia =>', len(sequence)) # def __len__(self):
print('-' * 45)
 
print('1º elemento =>', sequence[0]) # def __getitem__(self, index):
print('2º elemento =>', sequence[1]) # def __getitem__(self, index):
print('3º elemento =>', sequence[2]) # def __getitem__(self, index):
print('4º elemento =>', sequence[3]) # def __getitem__(self, index):
print('-' * 45)

sequence[3] = 'z' # def __setitem__(self, index, item):
print('Sequencia alterada =>', *sequence) # def __getitem__(self, index):
print('-' * 45)

del sequence[3]  # def __delitem__(self, index):

print('Uso do "for":')
for items in sequence: # def __getitem__(self, index):
    print(items)
print('-' * 10)
print('Uso do "for":')
for items in sequence: # def __getitem__(self, index):
    print(items)
print('-' * 45)

print('Letra "a" esta na sequencia =>','a' in sequence) # def __contains__(self, item):
print('Letra "z" esta na sequencia =>','z' in sequence) # def __contains__(self, item):
print('-' * 45)

print('Inverter sequencia =>', *reversed(sequence)) # def __reversed__(self):
print('-' * 45)

print('<==========================================================>')

from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self): # construtor
        self._data = {} # dicionário
        self._index = 0
        self._next_index = 0 

    def __len__(self): # retorna o comprimento da sequência
        return self._index
    
    def __iter__(self): # retorna um iterador para a sequência
        return self
    
    def append(self, *values): # adicionar valores na sequência
        for value in values:
            self._data[self._index] = value
            self._index += 1
            # resposta => {self._index: 'valor'}

    def __getitem__(self, index): # obtém um elemento da sequência pelo seu índice
        return self._data[index]
    # resposta => lista[0] => 'Maria'

    def __setitem__(self, index, value): # atualiza um elemento da sequência pelo seu índice
        self._data[index] = value
    # resposta => lista[0] = 'João'

    def __next__(self): # possibilita desempacotar a sequência
        if self._next_index == self._index:
            self._next_index = 0 # retorna "index = 0" para novo "for"
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value
    
if __name__ == '__main__':
    lista = MyList() # def __init__(self):
    print(lista) # endereço de memória
    print('-' * 45)

    lista.append('Maria', 'Helena', 'Décio') # def __getitem__(self, index):
    print(lista[0]) 
    print(lista[1]) 
    print(lista[2])
    print('-' * 45)

    lista[0] = 'João' # def __setitem__(self, index, value):
    print('Nome da primeira posição alterado para', lista[0])
    print('-' * 45)

    lista.append('Luiz') # def append(self, *values):
    print('Elementos na lista =', len(lista)) # def __len__(self):
    print('-' * 45)

    print('Lista = ', *lista) # def __next__(self)
    print('-' * 45)

    for item in lista: # def __next__(self)
        print(item)
    print('------')
    for item in lista: # def __next__(self)
        print(item)
    print('-' * 45)
    
    print("João" in lista) # def __next__(self)
    print('Ana' in lista) # def __next__(self)
    print("Décio" in lista) # def __next__(self)
    print('-' * 45)

#-----------------------------------------------------------------------------------------------

class Pessoa:

    def __init__(self): # construtor
        self.nome = None
        self.idade = None

    def set_dados(self): # método
        print('Cadastramento:')
        self.nome = input('Digite seu nome: ')
        self.idade = input('Digite seu idade: ')

    def get_dados(self): # método
        print('Cadastro:')
        print(f'Nome: {self.nome}, Idade{self.idade}')

def main():
    loop = True # finaliza loop se False e permanece se True
    LISTA = []

    while loop:
        # menu de operações existentes => "menu de opções"
        menu =  '''
============================================================
                    Menu de opções:
                    [1] CADASTRAR
                    [2] EXIBIR
                    [3] FINALIZAR
                '''
        # exibir "menu de opções"
        print(menu)

         # entrada de parâmetro digitada pelo usuário
        opcao = input('Escolha uma opção:').lower()
        print('=' * 60)

        # "menu de opções" = CADASTRO
        if opcao == '1':
            nome = Pessoa()
            nome.set_dados()
            LISTA.append(nome)
        # "menu de opções" = EXIBIR
        elif opcao == '2':
            for i in LISTA:
                i.get_dados()
        # "menu de opções" = FINALIZAR
        elif opcao == '3':
            loop = False
        else:
            # caso usuário digite qualquer opção não existente no "Menu de opções" 
            print('Opção invalida, digite o NUMERO correspondente ao "Menu de opções:"')

main()

#-----------------------------------------------------------------------------------------------
