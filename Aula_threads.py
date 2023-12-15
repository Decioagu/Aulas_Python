# Threads - Executando processamentos em paralelo

'''
    Em Python, threads são linhas de execução concorrentes em um mesmo processo. 
    Elas são concorrentes no sentido de que executam simultaneamente, mas cada um 
    com a sua própria linha de execução - quase como se fossem programas diferentes.
'''

from threading import Thread
from time import sleep


class MeuThread(Thread): # executar em paralelo
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        # executar threading.Thread (obrigatório)
        super().__init__() # ou Thread.__init__(self)
        
    def run(self): # método que será executado
        sleep(self.tempo) # espera
        print(self.texto)


t1 = MeuThread('Thread 1', 9) # (nome, tempo)
t1.start() # executa a classe em paraleto

t2 = MeuThread('Thread 2', 6) # (nome, tempo)
t2.start() # executa a classe em paraleto

t3 = MeuThread('Thread 3', 3) # (nome, tempo)
t3.start() # executa a classe em paraleto

for i in range(15):
    print(i)
    sleep(1) # espera

#-----------------------------------------------------------------------------

from threading import Thread
from time import sleep

# função
def vai_demorar(texto: str, tempo: int): 
    sleep(tempo)
    print(texto)

# OBS: args=(tupla)
t1 = Thread(target=vai_demorar, args=('Thread 1', 5)) # executar em paralelo
t1.start() # iniciar execução

t2 = Thread(target=vai_demorar, args=('Thread 2', 1)) # executar em paralelo
t2.start() # iniciar execução

t3 = Thread(target=vai_demorar, args=('Thread 3', 2)) # executar em paralelo
t3.start() # iniciar execução

for i in range(20):
    print(i)
    sleep(.5)

#-----------------------------------------------------------------------------

from threading import Thread
from time import sleep

# função
def vai_demorar(texto: str, tempo: int): 
    # print('Não vai aguardar') # ative o t1.join() e veja
    sleep(tempo)
    print(texto)

# OBS: args=(tupla)
t1 = Thread(target=vai_demorar, args=('Executando a Thread 1', 5)) # executar em paralelo
t1.start() # iniciar execução
# t1.join() # cancela a funcionalidade do Thrad (executa programa de forma linear)

while t1.is_alive():
    print('Esperando a Thread 1')
    sleep(2)

print('Finalizado...')

#-----------------------------------------------------------------------------

from threading import Lock, Thread
from time import sleep

class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...
        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque # quantide em estoque
        self.lock = Lock() # cadeado

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos
        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        
        self.lock.acquire() # Tranca o método

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release() # Libera o método
            return

        sleep(1) # atraso proposital (retirar sincronia da class)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).')
        if self.estoque != 0:
            print(f'Ainda temos {self.estoque} em estoque.')
        else:
             print(f'Ingressos esgotados.')
        
        self.lock.release() # Libera o método


if __name__ == '__main__':
    ingressos = Ingressos(11) # quantidade em estoque

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,)) # executar em paralelo 
        t.start() # iniciar execução

    t = Thread(target=ingressos.comprar, args=(1,)) # executar em paralelo 
    t.start()

    # print(ingressos.estoque) # ver quantidade de ingresso inicial