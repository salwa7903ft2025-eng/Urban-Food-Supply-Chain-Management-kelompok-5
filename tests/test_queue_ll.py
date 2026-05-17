import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_structures.queue_ll import QueueLL

def run_test():
    print("--- TESTING QUEUE (LINKED LIST BASED) ---")
    q = QueueLL()
    
    # Uji kondisi awal (akses front langsung karena QueueLL kamu tidak punya is_empty())
    print(f"Uji Kosong Awal (Harus True): {q.front is None}") 
    
    # Memasukkan data ke antrean (FIFO)
    q.enqueue("Lokasi-Petani-01")
    q.enqueue("Lokasi-Gudang-01")
    q.enqueue("Lokasi-Pasar-01")
    print(f"Uji Kosong Setelah Enqueue (Harus False): {q.front is None}")
    
    # Mengeluarkan data dari antrean (Urutan: Petani -> Gudang -> Pasar)
    print(f"Dequeue 1 (Harus Petani-01): {q.dequeue()}")
    print(f"Dequeue 2 (Harus Gudang-01): {q.dequeue()}")
    print(f"Dequeue 3 (Harus Pasar-01): {q.dequeue()}")
    print(f"Dequeue 4 (Harus None): {q.dequeue()}")
    print(f"Uji Kosong Akhir (Harus True): {q.front is None}")

if __name__ == "__main__":
    run_test()
