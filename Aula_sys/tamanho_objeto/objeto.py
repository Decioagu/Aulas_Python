import sys

print(sys.getsizeof(10))         # Inteiro
print(sys.getsizeof(10.5))       # Float
print(sys.getsizeof("Hello"))    # String
print(sys.getsizeof(True))       # Booleano

# ----------------------------------------------

lst = [1, 2, 3]
dct = {"a": 1, "b": 2}

print(sys.getsizeof(lst))  # Tamanho da lista
print(sys.getsizeof(dct))  # Tamanho do dicionário

# ----------------------------------------------

nested_list = [1, [2, 3], 4]

# O tamanho da lista não inclui o tamanho dos elementos internos
print(sys.getsizeof(nested_list))  # Ex.: 80

# ----------------------------------------------

class MyClass:
    pass

obj = MyClass()
print(sys.getsizeof(obj, default=100))  # Retorna 100 se não conseguir calcular
