# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Métodos úteis Set:
# add, update, clear, discard
'''
Em Python, um conjunto é uma coleção de itens únicos. Os conjuntos são 
representados pelo tipo de dados set.
Os conjuntos são semelhantes às listas, mas têm algumas diferenças importantes:

* Os conjuntos são não ordenados: Os elementos de um conjunto não têm uma ordem definida.
* Os conjuntos não permitem itens duplicados: Cada elemento de um conjunto deve ser único.
'''
s1 = set() # criar conjunto
print(s1)
s1.add('Luiz') # adicionar no conjunto
print(s1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # adicionar no conjunto
print(s1)
s1.discard('Olá mundo') # excluir do conjunto
print(s1)
s1.clear()
print(s1)
print()
# Operadores úteis:
# união "|" união (union) => Une
# intersecção "&" (intersection) => Itens presentes em ambos
# diferença "-" => Itens presentes apenas no set da esquerda
# diferença simétrica "^" => Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f'{s1=}')
print(f'{s2=}')
print()
s3 = s1 | s2 # união
print(s3)
s3 = s1 & s2 # intercessão 
print(s3)
s3 = s1 ^ s2 # diferença entre s1 e s2
print(s3)
s3 = s1 - s2 # diferença em s1
print(s3)
s3 = s2 - s1 # diferença em s2
print(s3)
s3 = s1.difference(s2)
print(s3)

'''
Aqui está uma lista dos métodos do tipo set() em Python:

add(): Adiciona um elemento ao conjunto.
clear(): Remove todos os elementos do conjunto.
copy(): Copia o conjunto para um novo conjunto.
difference(): Retorna um conjunto com os elementos que estão no conjunto atual, mas não no conjunto passado como argumento.
difference_update(): Remove os elementos do conjunto passado como argumento do conjunto atual.
discard(): Remove um elemento do conjunto se ele estiver presente.
intersection(): Retorna um conjunto com os elementos que estão presentes em ambos os conjuntos.
intersection_update(): Remove os elementos do conjunto atual que não estão presentes no conjunto passado como argumento.
isdisjoint(): Retorna True se os dois conjuntos não têm elementos em comum, False caso contrário.
issubset(): Retorna True se o conjunto atual é um subconjunto do conjunto passado como argumento, False caso contrário.
issuperset(): Retorna True se o conjunto atual é um superconjunto do conjunto passado como argumento, False caso contrário.
pop(): Remove e retorna um elemento aleatório do conjunto.
remove(): Remove um elemento do conjunto. Se o elemento não estiver presente, uma exceção será lançada.
symmetric_difference(): Retorna um conjunto com os elementos que estão presentes em um ou no outro conjunto, mas não em ambos.
symmetric_difference_update(): Atualiza o conjunto atual com os elementos que estão presentes em um ou no outro conjunto, mas não em ambos.
union(): Retorna um conjunto com os elementos que estão presentes em um ou no outro conjunto.
update(): Atualiza o conjunto atual com os elementos do conjunto passado como argumento.
'''
z = {'A', 1, 'B', 2, 'C', 3}
print(z)
z.discard('B')
print(z)
z.pop()
print(z)
z.clear()
print(z)

d = set()
d.update([0,1,2,3], (0,2,4,6))
print(d)

# Criar um "set" ou conjunto
x = set()
for i in range(3):
    a = input('valor:')
    x.add(a)
print(x)

y = set()

for i in range(3):
    a = input('valor:')
    y.update(a)
print(y)
