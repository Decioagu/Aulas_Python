from queue import Queue

# Criação de uma fila com capacidade ilimitada
fila = Queue()

# Adicionando itens à fila
fila.put("Item 1")
fila.put("Item 2")
fila.put("Item 3")
fila.put("Item 4")
fila.put("Item 5")

# Verificando o tamanho da fila
print("Tamanho da fila:", fila.qsize())  # Saída: 3

# Removendo e processando itens
while not fila.empty():
    item = fila.get()  # Remove o próximo item da fila
    print("Processando:", item)


# Verifica se a fila está vazia
print("Fila vazia?", fila.empty())  # Saída: True
