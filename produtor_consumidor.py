"""
Template para o Problema do Produtor-Consumidor
================================================

INSTRUÇÕES:
Complete este template seguindo o checklist da atividade.
Preencha as seções marcadas com TODO.

Nome do Aluno: Sol de Souza Nelo
Data: 19/12/25
"""

import threading
import time
import random
from threading import Semaphore, Lock

# ============================
# CONFIGURAÇÕES
# ============================

# Constantes já definidas para você
TAMANHO_BUFFER = 10          # Capacidade máxima do buffer
NUM_PRODUTORES = 2           # Número de threads produtoras
NUM_CONSUMIDORES = 2         # Número de threads consumidoras
NUM_ITENS_POR_THREAD = 10    # Quantos itens cada produtor/consumidor processa

# ============================
# ESTRUTURAS DE DADOS COMPARTILHADAS
# ============================

# Buffer já criado para você (lista vazia)
buffer = []
itens_disponiveis = Semaphore(0)
espacos_vazios = Semaphore(TAMANHO_BUFFER)
lock = Lock()

# ============================
# FUNÇÃO PRODUTOR
# ============================

def produtor(id_produtor):
    """
    Função executada por cada thread produtora.
    
    Args:
        id_produtor: Identificador único do produtor
    """
    # TODO: Implemente a função produtor
    # Dica: Use um loop para produzir NUM_ITENS_POR_THREAD itens
    
    for i in range(NUM_ITENS_POR_THREAD):
        # Gere um item aleatório
        item = random.randint(1, 100)

        # Aguarde por um espaço vazio no buffer
        espacos_vazios.acquire()

        # Adquira o lock para acessar o buffer
        lock.acquire()
        try:
            # Adicione o item ao buffer
            buffer.append(item)

            # Exiba uma mensagem informando o que foi produzido
            print(f"Produtor {id_produtor} produziu item {item} (buffer={len(buffer)})")
        finally:
            # Libere o lock
            lock.release()

        # Sinalize que há um novo item disponível
        itens_disponiveis.release()

        # Simule o tempo de produção
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Produtor {id_produtor} finalizou")

# ============================
# FUNÇÃO CONSUMIDOR
# ============================

def consumidor(id_consumidor):
    """
    Função executada por cada thread consumidora.
    
    Args:
        id_consumidor: Identificador único do consumidor
    """
    # TODO: Implemente a função consumidor
    # Dica: Use um loop para consumir NUM_ITENS_POR_THREAD itens
    
    for i in range(NUM_ITENS_POR_THREAD):
        # Aguarde por um item disponível no buffer
        itens_disponiveis.acquire()

        # Adquira o lock para acessar o buffer
        lock.acquire()
        try:
            # Remova o primeiro item do buffer
            item = buffer.pop(0)

            # Exiba uma mensagem informando o que foi consumido
            print(f"Consumidor {id_consumidor} consumiu item {item} (buffer={len(buffer)})")
        finally:
            # Libere o lock
            lock.release()

        # Sinalize que há um novo espaço vazio
        espacos_vazios.release()

        # Simule o tempo de consumo
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Consumidor {id_consumidor} finalizou")

# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    """
    Função principal que inicializa e gerencia todas as threads.
    """
    print("=" * 60)
    print("PROBLEMA DO PRODUTOR-CONSUMIDOR")
    print("=" * 60)
    print()
    
    # Crie uma lista para armazenar as threads
    threads = []

    # Crie e inicie as threads produtoras
    for i in range(NUM_PRODUTORES):
        t = threading.Thread(target=produtor, args=(i,))
        threads.append(t)
        t.start()

    # Crie e inicie as threads consumidoras
    for i in range(NUM_CONSUMIDORES):
        t = threading.Thread(target=consumidor, args=(i,))
        threads.append(t)
        t.start()

    # Aguarde todas as threads terminarem
    for t in threads:
        t.join()
    
    print()
    print("=" * 60)
    print("Programa finalizado!")
    print("=" * 60)

# ============================
# PONTO DE ENTRADA
# ============================

if __name__ == "__main__":
    main()