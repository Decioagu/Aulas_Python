'''
    A função é usada para criar um iterador que produz uma sequência infinita de inteiros, 
    a partir de um valor especificado.

    # count(start=0, step=1)
    * start: O valor inicial da sequência. O valor padrão é 0.
    * step: O incremento entre cada valor na sequência. O valor padrão é 1.

    A função é uma ferramenta útil para gerar sequências de números, especialmente quando 
    você precisa gerar uma sequência infinita. Ele também é eficiente em termos de memória, 
    pois só gera o próximo valor na sequência quando é necessário.
'''

# count é um iterador sem fim (itertools)

from itertools import count

for i in count(10, 2):
    print(i)
    if i > 20:
        break

#-----------------------------------------------------------------------------------------------

from itertools import count

c1 = count(8, 8) # (start, step)
r1 = range(8, 100, 8) # (start, stop ,step)


print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('range')
for i in r1:
    print(i)

