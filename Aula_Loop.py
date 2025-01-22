frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# ----------------- OU ----------------

# "compreensão de lista" ou "list comprehension"
print([fruta for fruta in frutas]) 

# ================================================================================

contador = 10
while contador >= 5:
    print(contador)
    contador -= 1

# ================================================================================

# "compreensão de lista" ou "list comprehension"
print([num for num in range(5)]) 

# range(inicio, fim, passo)
num_par = list(range(0,11,2))
print(num_par)

# range(inicio, fim)
for i in range(2, 7):
    print(i)

# ================================================================================

contador = 0
while contador <= 10:
    print(contador)
    if contador == 5:
        break # BREAK: interrompe a execução do loop atual, independentemente da condição de parada.
    contador += 1

# ----------------- OU ----------------

for numero in range(10):
    if numero == 5:
        break # BREAK: interrompe a execução do loop atual, independentemente da condição de parada.
    print(numero)

# ================================================================================

for numero in range(5):
    if numero == 2:
        continue # CONTINUE: pula a próxima iteração do loop atual, indo para a iteração subsequente.
    print(numero)

# ----------------- OU ----------------

for numero in range(5):
    if numero == 2:
        ... # CONTINUE: pula a próxima iteração do loop atual, indo para a iteração subsequente.
    print(numero)