import time
import random
import sys
import os

# Menambahkan root folder ke sys.path agar bisa melakukan import module dari src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules.priority_queue_pengiriman import PriorityQueuePengiriman
from src.modules.bst_katalog_produk import KatalogProduk, Produk
from src.modules.graph_rantai_pasok import GraphRantaiPasok
from src.modules.dijkstra_biaya_minimum import dijkstra_biaya_minimum

# Menggunakan seed sesuai parameter sistem di soal (poin 10.2)
random.seed(61)

# Minimal 3 ukuran dataset, kita gunakan 4 agar tren grafiknya lebih terlihat
DATASET_SIZES = [100, 1000, 5000]

def benchmark_priority_queue(size):
    pq = PriorityQueuePengiriman()
    start_time = time.perf_counter()
    for i in range(size):
        # Insert dengan masa kadaluarsa acak (1-15 hari)
        pq.enqueue("PetaniA", "GudangB", f"P{i}", 50, random.randint(1, 15))
    end_time = time.perf_counter()
    return end_time - start_time

def benchmark_bst_insert(size):
    katalog = KatalogProduk()
    start_time = time.perf_counter()
    for i in range(size):
        # Kode produk dibuat acak agar memicu variasi pencabangan BST
        kode = random.randint(1, 100000)
        p = Produk(kode, f"Produk{i}", "KategoriX", 10000, 100, 10)
        katalog.insert_produk(p)
    end_time = time.perf_counter()
    return end_time - start_time

def benchmark_dijkstra(size):
    graph = GraphRantaiPasok()

    # Tambah node
    for i in range(size):
        graph.add_vertex(f"Node{i}")

    # Tambah edge linear
    for i in range(1, size):
        graph.add_edge_weighted(
            f"Node{i-1}",
            f"Node{i}",
            random.randint(1, 20),
            random.randint(1000, 5000)
        )

    # Tambah edge random biar graph lebih realistis
    for i in range(size // 2):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)

        if a != b:
            graph.add_edge_weighted(
                f"Node{a}",
                f"Node{b}",
                random.randint(1, 20),
                random.randint(1000, 5000)
            )

    start_time = time.perf_counter()

    dijkstra_biaya_minimum(graph, "Node0")

    end_time = time.perf_counter()

    return end_time - start_time
    
def run_benchmarks():
    print("="*65)
    print(" EKSPERIMEN PERBANDINGAN PERFORMA (RUNTIME BENCHMARK)".center(65))
    print("="*65)
    print(f"{'Dataset Size':<15} | {'PQ Enqueue O(n)':<15} | {'BST Insert O(log n)':<18} | {'Dijkstra O(V^2+E)':<15}")
    print("-" * 65)
    
    for size in DATASET_SIZES:
        time_pq = benchmark_priority_queue(size)
        time_bst = benchmark_bst_insert(size)
        time_dij = benchmark_dijkstra(size)
        
        # Format output menjadi detik dengan 6 angka desimal
        print(f"{size:<15} | {time_pq:<15.6f} | {time_bst:<18.6f} | {time_dij:<15.6f}")
        
    print("="*65)

if __name__ == "__main__":
    run_benchmarks()