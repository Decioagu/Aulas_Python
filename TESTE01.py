
import csv

with open('data1.csv', 'w', newline='' , encoding='utf8') as arquivo_csv:
    writer = csv.writer(arquivo_csv) # modo de gravação
    writer.writerow(['nome', 'idade', 'cidade']) # escrever uma linha
    writer.writerow(['Alice', 30, 'Rio de Janeiro']) # escrever uma linha
    writer.writerow(['Bob', 25, 'São Paulo']) # escrever uma linha