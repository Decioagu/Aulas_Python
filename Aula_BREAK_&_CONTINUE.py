'''
Em programação, as instruções BREAK e CONTINUE são usadas para controlar o fluxo de execução de um loop.
- BREAK: interrompe a execução do loop atual, independentemente da condição de parada.
- CONTINUE: pula a próxima iteração do loop atual, indo para a iteração subsequente.

'''

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
