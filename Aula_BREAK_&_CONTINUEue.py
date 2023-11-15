# break - exemplo
print("A instrução de pausa:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do loop =>", i)
print("Fora do loop.")

# continue - exemplo
print("\nA instrução para continuar:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do loop =>", i)
print("Fora do loop.")
