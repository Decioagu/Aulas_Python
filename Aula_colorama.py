from colorama import Fore, Back, Style, init

# Inicializar o Colorama (necessário no Windows)
init()

print(Fore.RED + "Este texto é vermelho.")
print(Back.YELLOW + "Este texto tem fundo amarelo.")
print(Style.BRIGHT + "Texto em estilo brilhante.")
print(Style.RESET_ALL + "Voltou ao padrão.")

'''
Componentes principais:
Fore: Define a cor do texto (ex: Fore.RED, Fore.GREEN).
Back: Define a cor de fundo (ex: Back.YELLOW, Back.BLUE).
Style: Define o estilo do texto (ex: Style.BRIGHT, Style.DIM, Style.NORMAL).
'''