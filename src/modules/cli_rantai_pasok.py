from .graph_rantai_pasok import GraphRantaiPasok
from .circular_queue_buffer_gudang import CircularQueueBuffer
from .priority_queue_pengiriman import PriorityQueuePengiriman
from .bst_katalog_produk import KatalogProduk, Produk
from .dijkstra_biaya_minimum import dijkstra_biaya_minimum

class CLI:
    def __init__(self):
        self.graph = GraphRantaiPasok()
        self.katalog = KatalogProduk()
        self.pq_pengiriman = PriorityQueuePengiriman()
        self.buffers = {} # Node -> CircularQueueBuffer

    def init_node_buffer(self, node_name):
        if node_name not in self.buffers:
            self.buffers[node_name] = CircularQueueBuffer(capacity=50)

    def run(self):
        print("Sistem Manajemen Rantai Pasok Berjalan...")
        # (Implementasi parsing input loop while True bisa diletakkan di sini.
        # Untuk tujuan modul, kita menyediakan fungsi-fungsi eksekusi.)
        
    def kirim(self, dari, ke, kode, jumlah, masa_kadaluarsa):
        self.pq_pengiriman.enqueue(dari, ke, kode, jumlah, masa_kadaluarsa)
        print(f"Dimasukkan antrean pengiriman: {kode} dari {dari} ke {ke}")

    def proses_kirim(self):
        item = self.pq_pengiriman.dequeue()
        if item:
            self.init_node_buffer(item.ke)
            sukses = self.buffers[item.ke].enqueue({"kode": item.kode_produk, "jumlah": item.jumlah})
            if sukses:
                print(f"Sukses mengirim {item.kode_produk} ke buffer {item.ke}")
            else:
                print(f"Gagal: Buffer di {item.ke} penuh!")
        else:
            print("Antrean pengiriman kosong.")