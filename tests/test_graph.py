import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_structures.graph import Graph

def run_test():
    print("--- TESTING GRAPH (ADJACENCY LIST BASED) ---")
    g = Graph()
    
    # Uji kondisi awal (Graph kosong)
    print(f"Uji Graph Kosong (Harus {{}}): {g.adj_list}")
    
    # Menambahkan vertex (titik/lokasi)
    g.add_vertex("Lokasi-Petani-01")
    g.add_vertex("Lokasi-Gudang-01")
    g.add_vertex("Lokasi-Pasar-01")
    print(f"Setelah Tambah Vertex: {list(g.adj_list.keys())}")
    
    # Menambahkan edge (hubungan/jalur antar lokasi)
    g.add_edge("Lokasi-Petani-01", "Lokasi-Gudang-01")
    g.add_edge("Lokasi-Gudang-01", "Lokasi-Pasar-01")
    
    # Uji keterhubungan (karena Undirected, kedua arah harus terisi)
    print(f"Jalur dari Petani-01 (Harus ['Lokasi-Gudang-01']): {g.adj_list['Lokasi-Petani-01']}")
    print(f"Jalur dari Gudang-01 (Harus ['Lokasi-Petani-01', 'Lokasi-Pasar-01']): {g.adj_list['Lokasi-Gudang-01']}")
    print(f"Jalur dari Pasar-01 (Harus ['Lokasi-Gudang-01']): {g.adj_list['Lokasi-Pasar-01']}")
    
    # Cetak visualisasi Graph menggunakan method bawaan class
    print("\n--- Visualisasi Cetak Graph ---")
    g.print_graph()

if __name__ == "__main__":
    run_test()
