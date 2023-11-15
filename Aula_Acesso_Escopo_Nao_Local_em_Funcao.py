'''
Em Python, o nonlocal é uma declaração que permite que uma variável seja acessada e 
modificada em um escopo local, mesmo que ela tenha sido declarada em um escopo mais externo.

Por padrão, as variáveis declaradas dentro de uma função são consideradas locais. Isso significa 
que elas só podem ser acessadas e modificadas dentro da função em que foram declaradas. Se você tentar 
acessar uma variável local fora da função em que ela foi declarada, você receberá um erro.

O nonlocal permite que você acesse uma variável local de um escopo mais externo, "mas não global". 
Por exemplo, suponha que você tenha o seguinte código:

'''

def fora():
    a = 1
    def dentro():
        nonlocal a # informa que variável não é local
        a = 2
    dentro()
    print(a)

fora()