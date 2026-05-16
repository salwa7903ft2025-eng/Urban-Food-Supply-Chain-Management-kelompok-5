import sys
import os

# Menambahkan path folder saat ini agar modul 'node' dapat terdeteksi dengan baik
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from node import Node
except ImportError:
    from .node import Node

class BSTKatalog:
    """
    Kelas untuk mengelola katalog produk pada sistem Urban Food Supply Chain.
    Menggunakan struktur data Binary Search Tree (BST) untuk optimasi pencarian.
    """
    
    def __init__(self):
        # Inisialisasi akar pohon (root) sebagai None
        self.root = None

    def tambah_produk(self, kode, nama):
        """
        Fungsi untuk menambahkan produk baru ke dalam katalog.
        Menerima parameter kode produk (integer) dan nama produk (string).
        """
        if self.root is None:
            self.root = Node({'id': kode, 'nama': nama})
        else:
            self._tambah_rekursif(self.root, kode, nama)

    def _tambah_rekursif(self, current, kode, nama):
        # Logika BST: Kode lebih kecil ke kiri, kode lebih besar ke kanan
        if kode < current.data['id']:
            if current.left is None:
                current.left = Node({'id': kode, 'nama': nama})
            else:
                self._tambah_rekursif(current.left, kode, nama)
        elif kode > current.data['id']:
            if current.right is None:
                current.right = Node({'id': kode, 'nama': nama})
            else:
                self._tambah_rekursif(current.right, kode, nama)

    def cari_produk(self, kode):
        """
        Fungsi pencarian produk berdasarkan kode dengan kompleksitas waktu O(log n).
        """
        return self._cari_rekursif(self.root, kode)

    def _cari_rekursif(self, current, kode):
        # Basis rekursi: jika data ditemukan atau sampai pada ujung leaf
        if current is None or current.data['id'] == kode:
            return current
            
        if kode < current.data['id']:
            return self._cari_rekursif(current.left, kode)
        return self._cari_rekursif(current.right, kode)

    def cetak_seluruh_katalog(self, current):
        """
        Menampilkan seluruh isi katalog menggunakan metode In-order Traversal
        sehingga data ditampilkan berurutan berdasarkan Kode Produk.
        """
        if current:
            self.cetak_seluruh_katalog(current.left)
            print(f" > [Kode: {current.data['id']}] Nama Produk: {current.data['nama']}")
            self.cetak_seluruh_katalog(current.right)

# --- Demonstrasi Program ---
if __name__ == "__main__":
    katalog_kelompok5 = BSTKatalog()
    
    print("\n" + "="*55)
    print("SISTEM INFORMASI KATALOG URBAN FOOD SUPPLY CHAIN")
    print("KELOMPOK 5 - TEKNOLOGI INFORMASI")
    print("="*55)

    # Input data produk sesuai studi kasus Topik 10
    katalog_kelompok5.tambah_produk(105, "Cabai Merah")
    katalog_kelompok5.tambah_produk(101, "Beras Premium")
    katalog_kelompok5.tambah_produk(110, "Tomat Organik")
    katalog_kelompok5.tambah_produk(103, "Bawang Merah")

    print("\n[INFO] Menampilkan daftar katalog produk (Urut berdasarkan Kode):")
    katalog_kelompok5.cetak_seluruh_katalog(katalog_kelompok5.root)
    
    # Uji coba fitur pencarian produk
    kode_target = 110
    print(f"\n[SISTEM] Melakukan pencarian untuk Kode Produk: {kode_target}")
    hasil_pencarian = katalog_kelompok5.cari_produk(kode_target)
    
    if hasil_pencarian:
        print(f"[HASIL] Produk ditemukan: {hasil_pencarian.data['nama']}")
    else:
        print("[HASIL] Produk tidak ditemukan dalam sistem.")
    
    print("="*55 + "\n")