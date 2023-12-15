# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue

'''
    Em Python, LIFO (Last In First Out) e FIFO (First In First Out) são dois tipos 
    de estruturas de dados que são usadas para armazenar elementos em ordem em uma lista.

    LIFO significa "Último a Entrar, Primeiro a Sair". 
    Em uma estrutura de dados LIFO, os elementos são adicionados no final 
    da estrutura e removidos do início. Isso significa que o último elemento 
    a ser adicionado à estrutura será o primeiro a ser removido.
    # Para tirar itens do final: O(1) Tempo constante
    # Para tirar itens do início: O(n) Tempo Linear
    # https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
    # https://youtu.be/svWVHEihyNI

    FIFO significa "Primeiro a Entrar, Primeiro a Sair". 
    Em uma estrutura de dados FIFO, os elementos são adicionados no início 
    da estrutura e removidos do início. Isso significa que o primeiro elemento 
    a ser adicionado à estrutura será o primeiro a ser removido.
    # https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
    # https://youtu.be/RHb-8hXs3HE
    # Para tirar itens do final: O(1) Tempo constante
    # Para tirar itens do início: O(1) Tempo constante

'''

from collections import deque

# FIFO (First In First Out)

fila_correta: deque[int] = deque()
fila_correta.append(1)  # Adiciona no final
fila_correta.append(2)  # Adiciona no final
fila_correta.append(3)  # Adiciona no final
fila_correta.appendleft(0)  # Adiciona no começo
fila_correta.appendleft(-1)  # Adiciona no começo
fila_correta.appendleft(-2)  # Adiciona no começo
fila_correta.appendleft(-3)  # Adiciona no começo
print(fila_correta)  # deque([-3, -2, 1, 0, 1, 2, 3])
fila_correta.pop()  # 3
fila_correta.popleft()  # -2
print(fila_correta)  # deque([-2, 1, 0, 1, 2,])