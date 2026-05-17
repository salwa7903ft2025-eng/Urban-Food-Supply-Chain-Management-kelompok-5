import sys
import os
import time
import random

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.graph_rantai_pasok import GraphRantaiPasok
from modules.circular_queue_buffer_gudang import CircularQueue
from modules.priority_queue_pengiriman import PriorityQueueKirim
from modules.bst_katalog_produk import BSTKatalog
from modules.dijkstra_biaya_minimum import dijkstra_biaya

from dataclasses import dataclass


@dataclass
class Produk:
    kode: str
    nama: str
    kategori: str
    harga_satuan: float
    stok: int
    masa_kadaluarsa_hari: int


@dataclass
class Pengiriman:
    pengiriman_id: int
    prioritas: int
    kode_produk: str


print('=' * 50)
print('BENCHMARK FOOD SUPPLY CHAIN SYSTEM')
print('=' * 50)


# ==================================================
# BENCHMARK GRAPH
# ==================================================

print('[1] Benchmark GraphRantaiPasok')

graph = GraphRantaiPasok()

jumlah_node = 500
jumlah_edge = 1000

start = time.perf_counter()

for i in range(jumlah_node):
    graph.tambah_node(f'N{i}', 'DISTRIBUTOR')

for _ in range(jumlah_edge):
    u = f'N{random.randint(0, jumlah_node - 1)}'
    v = f'N{random.randint(0, jumlah_node - 1)}'

    if u != v:
        graph.tambah_jalur(
            u,
            v,
            random.randint(1, 100),
            random.randint(500, 3000)
        )

end = time.perf_counter()

print(f'Total node  : {jumlah_node}')
print(f'Total edge  : {jumlah_edge}')
print(f'Runtime     : {(end - start):.6f} detik')


# ==================================================
# BENCHMARK CIRCULAR QUEUE
# ==================================================

print('[2] Benchmark CircularQueue')

queue = CircularQueue(10000)

start = time.perf_counter()

for i in range(10000):
    queue.enqueue(f'Produk-{i}')

for i in range(10000):
    queue.dequeue()

end = time.perf_counter()

print('10000 enqueue + dequeue selesai')
print(f'Runtime : {(end - start):.6f} detik')


# ==================================================
# BENCHMARK PRIORITY QUEUE
# ==================================================

print('[3] Benchmark PriorityQueueKirim')

pq = PriorityQueueKirim()

start = time.perf_counter()

for i in range(5000):
    pq.enqueue(
        Pengiriman(
            i,
            random.randint(1, 3),
            f'PRD-{i}'
        )
    )

while len(pq) > 0:
    pq.dequeue()

end = time.perf_counter()

print('5000 enqueue + dequeue selesai')
print(f'Runtime : {(end - start):.6f} detik')


# ==================================================
# BENCHMARK BST
# ==================================================

print('[4] Benchmark BSTKatalog')

bst = BSTKatalog()

start = time.perf_counter()

indices = list(range(5000))
random.shuffle(indices)

for i in indices:
    bst.insert(
        Produk(
            f'PRD-{i:05d}',
            f'Produk-{i}',
            'SAYUR',
            10000,
            100,
            random.randint(1, 30)
        )
    )

for i in range(5000):
    bst.search(f'PRD-{i:05d}')

end = time.perf_counter()

print('5000 insert + search selesai')
print(f'Runtime : {(end - start):.6f} detik')


# ==================================================
# BENCHMARK DIJKSTRA
# ==================================================

print('[5] Benchmark Dijkstra')

start = time.perf_counter()

result = dijkstra_biaya(graph, 'N0')

end = time.perf_counter()

print('Dijkstra selesai dijalankan')
print(f'Runtime : {(end - start):.6f} detik')


print('' + '=' * 50)
print('BENCHMARK SELESAI')
print('=' * 50)