# Aulas de Python

**Aula_CRIAR_AMBIENTE_VIRTUAL.py**
- Um __ambiente virtual__ é uma maneira de isolar as dependências de um projeto de outros projetos. Isso é útil para evitar conflitos de dependências, que podem ocorrer quando dois projetos usam versões diferentes da mesma biblioteca.
---

**Aula_Objeto.py**
- Os __objetos__ são um conceito fundamental em Python. Eles são usados para representar coisas do mundo real, como pessoas, animais, objetos físicos ou conceitos abstratos. São __atributos__ que armazenam dados e comportamentos.
- ___Atributos de dados___: Armazenam dados, como o nome, a idade ou a cor de um objeto.
- ___Atributos de comportamento___: Representam os comportamentos de um objeto, como métodos ou funções.

___Objeto iterável___
- Um iterável é um objeto que pode ser iterado, ou seja, que pode ser percorrido:

__Listas__

__Tuplas__

__Strings__

__Conjuntos__

__Dicionários__ 

__Objetos arquivo__ (txt, csv, json)

__Geradores__ (uma expressão que retorna um objeto gerador)
---

**Aula_STR.py**
- Em Python, __str()__ é o tipo de dado que representa strings. __Strings__ são sequências de caracteres que representam texto.
As strings em Python são __imutáveis__, o que significa que elas não podem ser modificadas após serem criadas. Se você tentar modificar uma string, uma nova string será criada.
As strings em Python são __unicode__, o que significa que elas podem representar caracteres de qualquer idioma.
---

**Aula_Cores.py**
- Para adicionar __cores__ em texto em Python, você pode usar as sequências de escape ANSI. Essas sequências são usadas para controlar as cores do texto exibido no terminal.
---

**Aula_LISTA.py**
- Em Python, uma __list()__ é uma estrutura de dados que permite armazenar uma coleção de itens em uma única variável. Os itens da lista podem ser de qualquer tipo, incluindo números, strings, objetos ou até mesmo outras listas.
---

**Aula_TUPLA.py**
- Uma __tuple()__ em Python é uma coleção ordenada e imutável de elementos, semelhante a uma lista.
---

**Aula_Conjunto.py**
- Em Python, um conjunto ou __set()__ é uma coleção de __itens únicos__. 
Os conjuntos são semelhantes às listas, mas têm algumas diferenças importantes:

- ___Os conjuntos não são ordenados___: Os elementos de um conjunto não têm uma ordem definida.
- ___Os conjuntos não permitem itens duplicados___: Cada elemento de um conjunto deve ser único.
---

**Aula_DICIONARIO.py**
- Em Python, um __dict()__ é uma estrutura de dados que permite armazenar uma coleção de dados relacionados, cada um com uma __chave__ e um __valor__. 
- As ___chaves___: são únicas e servem para identificar os valores. 
- Os ___valores___: podem ser de qualquer tipo, incluindo números, strings, objetos ou até mesmo outros dicionários.
---

**Aula_FLOAT_ARREDONDAMENTO.py**
- Arredondamento de ponto flutuante
- Uso de número absoluto __abs()__ recebe um único argumento, que pode ser do tipo numérico  inteiros, ponto flutuante e números complexos.
---
---

**Aula_Import.py**
- A __import é uma instrução__ em Python que importar módulos para um programa. 
Um módulo é um arquivo Python que contém código que pode ser reutilizado em outros programas Python, exemplo:
__import "module_name"__
---

**Aula_EMPACOTAMENTO_DESEMPACOTAMENTO.py**
- Em Python, o __empacotamento__ e o __desempacotamento__ são técnicas usadas para manipular __lista__, __tupla__ e __dicionário__.
- ___Empacotamento___: é o processo de colocar vários valores em uma única variável. Isso pode ser feito usando o operador .
- ___Desempacotamento___: é o processo de distribuir os valores de uma variável em várias variáveis. Isso pode ser feito usando o operador .
---

**Aula_if_elif_else.py**
- As estruturas condicionais permitem que o código seja executado de forma diferente, dependendo do valor de uma expressão.
- Em Python, as estruturas condicionais mais comuns são o __if__, __elif__ e __else__.
---

**Aula_BREAK_&_CONTINUE.py**
- Em programação, as instruções __break__ e __continue__ são usadas para controlar o fluxo de execução de um loop.
- ___Break___: interrompe a execução do loop atual, independentemente da condição de parada.
- ___Continue___: pula a próxima iteração do loop atual, indo para a iteração subsequente.
---

**Aula_Try_Except_Else_Finally.py**
- Em Python, as __exceções__ são eventos que interrompem o fluxo normal do programa. Elas podem ser causadas por uma variedade de fatores: 
- Erros de sintaxe;
- Erros de lógica;
- Erros de execução 
- Comando __raise__ usado para gerar uma exceção de um tipo personalizado.
__Para tratar exceções se usa o bloco de código _"try"_ e _"except"_.__
---

**Aula_Reduce.py**
- A função __reduce()__ do Python é usada para __reduzir uma sequência a um único valor__ em um iterável. Faz a soma dos valores em uma lista ou lista de objetos.
---

**Aula_Map.py**
- A __função map()__ em Python usa uma função e um iterável como seus argumentos e retorna um iterador que aplica a função a cada elemento do iterável.
Exemplo: __"variável" = list(map(função, iterável))__
---

**Aula_Contador_Infinito.py**
- A função é usada para __criar um iterador__ que produz uma __sequência infinita__ de inteiros, a partir de um valor especificado.
---

**Aula_GENERATOR_EXPRESSION.py**
- Generator expression em Python é uma expressão que retorna um objeto gerador. É semelhante a uma __compreensão de lista__, mas em vez de criar uma lista, cria um __objeto gerador__ que pode ser iterado para produzir os valores no gerador.
---

**Aula_pprint.py**
- O __módulo pprint__ do Python fornece uma maneira de __imprimir__ representações de estruturas de dados de __forma organizada__ e legível.
---

**Aula_Random.py**
- O __módulo random__ em Python __gerar números aleatórios__. Esses números podem ser usados para criar efeitos aleatórios em seus programas.
---

**Aula_Secrets.py**
- O __módulo secrets__ em Python fornece funções para __gerar dados criptograficamente seguros__. Esses dados podem ser usados para:
- ___Gerar chaves secretas___: são usadas para criptografar e descriptografar dados.
- ___Gerar senhas aleatórias___: são mais seguras do que as senhas escolhidas pelo usuário.
- ___Gerar tokens de autenticação___: são usados para garantir que um usuário está autorizado a acessar um recurso.
---

**Aula_lifo_e_fifo.py**
- Em Python, __LIFO__ (Last In First Out) e __FIFO__ (First In First Out) são dois tipos de estruturas de dados que são usadas para armazenar elementos em ordem em uma __lista__ de forma otimizada.
- __LIFO__ é frequentemente usado para representar __pilhas de itens__, como uma pilha de pratos ou uma pilha de arquivos.
- __FIFO__ é frequentemente usado para representar __filas de itens__, como uma fila de pessoas esperando para comprar ingressos ou uma fila de processos esperando para serem executados.
---
---

**Aula_Calendar.py**
- A função __calendar()__ é uma função interna em Python que retorna um calendário. 
    O calendário pode ser __mensal__, __semanal__ ou __anual__. 
---

**Aula_Datatime.py**
- O módulo datetime em Python fornece classes para __manipular datas e horas__. Ele suporta uma ampla gama de operações.
---

**Aula_locale_idioma.py**
- O __módulo locale__ em Python fornece funções para trabalhar com configurações regionais e de idioma, permitindo que você adapte seus programas às __configurações de idioma__, formatos de data e moeda.
---
---

**Aula_Arquivo_TXT.py**
- A extensão __TXT__ é uma extensão de arquivo que indica que um arquivo é um arquivo de texto simples.
---

**Aula_Arquivo_CSV.py**
- __CSV__ (Comma Separated Values - Valores separados por vírgulas)
---

**Aula_Arquivo_JSON.py**
- O que é __JSON__ - JavaScript Object Notation
---

**Aula_Arquivo_EXCEL.py**
- O __módulo openpyxl__ é uma biblioteca open-source escrita em Python utilizada para ler, escrever e manipular arquivos do __Microsoft Excel__. Ela oferece uma forma fácil e eficiente de automatizar tarefas relacionadas a planilhas.
---

**Aula_Arquivo_PDF_1.py**
- O __módulo PyPDF2__ é uma biblioteca Python que permite manipular __arquivos PDF__ para __leitura e escrita__.
---

**Aula_Arquivo_PDF_2.py**
- O __módulo PyMuPDF__ é uma biblioteca Python que permite manipular __arquivos PDF__ para __leitura e escrita__.
---

**Aula_Arquivo_ZIP.py**
-  O __módulo zipfile__ fornece várias funções para manipular __arquivos ZIP__, que pode ser usada para __compactar e descompactar__.
---
---

**Aula_FUNCAO.py**
-  Função é um __bloco de código__ que pode ser __reutilizado__. As funções são uma ferramenta poderosa que pode ajudar a tornar o código mais legível, organizado e eficiente.
---

**Aula_FUNCAO_LAMBDA.py**
- Função lambda (__função anônima__) são funções de uma única linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
---

**Aula_Acesso_Escopo_Nao_Local_em_Funcao.py**
- Em Python, o __nonlocal__ é uma declaração que permite que uma __variável__ seja __acessada e modificada__ em um __escopo local__, mesmo que ela tenha sido __declarada__ em um __escopo externo__.
---

**Aula_Fucao_Closure.py**
- Um __closure__ em Python é uma função que pode acessar variáveis mesmo depois que a função que a criou terminou de executar.  __Em resumo uma função externa retorna para uma função mais interna__ e isso é possível porque o __closure captura as variáveis__ em seu escopo externo e as __mantém em memória__ mesmo depois que a função externa termina.
---

**Aula_Funcao_Decoradora.py**
- Em Python, uma __função decoradora é uma função que recebe outra função como entrada e retorna uma função modificada__. As funções decoradoras são uma ferramenta poderosa que pode ser usada para adicionar funcionalidade a funções existentes sem alterar seu código fonte. 
---
---

**Aula_POO-Programacao_Orientada_Objetos.py**
- A __Programação Orientada a Objetos__ (__POO__) é um paradigma de programação que organiza o código em torno de objetos. Um objeto é uma entidade que pode ser usada para armazenar dados e realizar operações. Os objetos são criados a partir de __class__, que são modelos que definem os atributos e métodos de um objeto.
---

**Aula_Context_Manager.py**
- O método da __classe__ gerenciadora de contexto (__Context Manager__) pode capturar e tratar __exceções__, garantindo que os recursos sejam liberados adequadamente mesmo se ocorrer um __"erro"__. Isso evita vazamentos de recursos e possíveis travamentos, melhora a legibilidade do código e facilita a compreensão do fluxo geral do seu programa.
Um exemplo de (Context Manager) é considerar um cenário em que você deseja abrir um arquivo, __ler seu conteúdo e fechá-lo__. O uso de uma classe gerenciadora de contexto garante que o arquivo seja fechado mesmo se ocorrer um __erro__ durante o processo de leitura.
---

**Aula_Metaclasses.py**
- Uma __metaclasse__ em Python é uma classe especial que controla a criação de outras __classes__. Elas permitem personalizar o comportamento da criação de classes e objetos. No entanto, __são complexas e nem sempre são necessárias__. 
__Use-as apenas se você entender bem como elas funcionam e se precisar de seus recursos avançados__.
---

**Aula_Enum.py**
- O __módulo enum__ em Python fornece uma maneira fácil de __criar enumerações__ personalizadas __utilizando classes__. Uma enumeração é um tipo de dado que consiste em um conjunto de valores nomeados. Os valores de enumeração são geralmente constantes e são usados para representar diferentes estados ou opções de um sistema.
---

**Aula_Metodos_Magicos.py**
- __Métodos mágicos__ em Python são métodos que possui "underscores" no "nome" (Ex: \_\_"nome"__). Eles são chamados automaticamente pelo Python em resposta a eventos específicos, como a criação de um objeto, a atribuição de um valor a um atributo, ou a comparação de dois objetos. Normalmente utilizados com __class__.
---
---

**Aula_Path.py**
- __Path é um módulo__ incluído na biblioteca padrão do Python que fornece ferramentas para __manipular caminhos de arquivos e diretórios__. Ele oferece uma interface abrangente e consistente para trabalhar com caminhos, __independentemente do sistema operacional__ em que o Python está sendo executado.
---

**Aula_String.py**
- __Módulo string__ é uma __função que substitui espaços reservados__ em uma cadeia de caracteres, geralmente é feito usando um dicionário ou outra estrutura de dados que mapeia nomes de espaço reservado para seus valores correspondentes.
Exemplo: "Olá, meu nome é __${nome}__ e tenho __${idade}__ anos."
---

**Aula_Subprocess.py**
- O __subprocess é um módulo__ Python que __permite executar programas externos e comandos de shell e interagir com eles__. Ele fornece funções para criar novos processos, enviar e receber dados de/para os processos, e esperar por sua execução.
---

**Aula_Variaveis_de_Ambiente.py**
- Um __arquivo .env__ é um arquivo de texto que contém __variáveis de ambiente__. Ele é usado para __armazenar informações__ que podem ser __usadas por diferentes programas ou scripts__ em execução no sistema operacional, como caminhos de arquivos, configurações de rede ou informações de autenticação.
Arquivos .env são frequentemente usados em projetos Python para armazenar configurações específicas do projeto. Isso permite que as configurações sejam facilmente alteradas sem modificar o código-fonte do projeto.
---

**Aula_threads.py**
- O uso de __threads__ é uma forma de criar objetos que podem ser executados em paralelo. Isso pode ser útil para melhorar o desempenho de um programa, pois __permite que ele execute múltiplas tarefas ao mesmo tempo__.
---

### Aula_OS
**Aula_OS.py**
- O __módulo os__ em Python fornece uma interface para interagir com o sistema operacional. Ele fornece funções e variáveis para manipular arquivos, diretórios, processos, e outros recursos do sistema operacional.
---

