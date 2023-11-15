from pathlib import Path

print()
caminho_do_projeto = Path()
print(caminho_do_projeto.absolute()) # ver caminho da pasta
print('-' * 50)
caminho_do_arquivo = Path(__file__) # ver caminho do arquivo executado
print(caminho_do_arquivo)
print('-' * 50)
print(Path.home()) # ver caminho da pasta usuário