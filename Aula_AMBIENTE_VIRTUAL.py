'''
# Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:


*********************** Windows PowerShell**************************
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Opção: S
# https://www.youtube.com/watch?v=m1TYpvIYm74&t=326s
********************************************************************

# O Debugger do VS Code = Aula 36

# ambiente virtual
py -m venv venv
py -m venv "NOME"
python -m venv "NOME"
python 3 -m venv "NOME"

# ativa um ambiente virtual
.\venv\Scripts\activate
.\"NOME"\Scripts\activate

# desativar um ambiente virtual
deactivate

# atualizar pip
python.exe -m pip install --upgrade pip

# instalar pacote
py -m pip install "pacote"
pip install "pacote"

# desintalar pacote 
pip uninstall  "pacote"

# versão python
py -V
python -V
pip --version

# ver pacotes instalados no ambiente virtual
pip freeze

# gerar arquivo.txt de pacotes instalados
py -m pip freeze > requirements.txt (OBS: nome requirements.txt pode ser alterado)
pip freeze > requirements.txt

# recuperar pacotes em pip freeze em arquivo.txt
py -m pip install -r requirements.txt (OBS: nome requirements.txt pode ser diferente)
pip install -r requirements.txt

# ver versão do pacote
pip show "pacote"
pip index versions "pacote"

# instalar versão pacote antigo código
pip install "pacote"=="código"

# instalar versão mais recente
pip install "pacote" --upgrade

# instalar jupyter notebook
py -m pip install notebook

# ativar jupyter notebook
jupyter notebook

# arquivo ".gitignore" (consultar arquivo "gitignore_padrão.txt")
Abra o VS Code e navegue até o diretório do seu projeto.
Crie um novo arquivo chamado .gitignore.
Abra o arquivo .gitignore recém-criado.

Adicione os arquivos ou diretórios que você deseja excluir, exemplo:
consultar arquivo "gitignore_padrão.txt", na pasta P:\REPOSITORIO\PRIVADO\Aulas_Python

# PyInstaller Manual = Aula374
pip install -U pyinstaller
https://pyinstaller.org/en/stable/
'''



