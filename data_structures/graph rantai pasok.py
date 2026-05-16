from collection imnport deque
#kiew aryo :vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# 1. Struktur data untuk Jalur (Edge)
Edge:
r__init__(self, tujuan, jarak_km, biaya_per_km):
   self.tujuan = tujuan 
   self.jarak_km = jarak_km
   self.biaya_per_km = biaya_per_km
   # Hitung bobot utama sesuai modul
   self.total_biaya = jarak_km * biaya_per_km
# 2. Struktur data untuk Peta (Graph)
class Graph:
    def__init__(self)
       # Menggunakan dictionary untuk Adjacency List
       self.adj_list = {}

    # Fungsi tambah_node
    def tambah-node(self, nama_kota)
     if nama_kota not in self.adj_list:
         self.adj_list[nama_kota] = []
         
