import sys
import os

# Menambahkan path folder agar modul 'node' terdeteksi dengan baik
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from node import Node
except ImportError:
    from .node import Node

class BSTKatalog:
    def __init__(self):
        # Inisialisasi akar pohon (root) sebagai None (Pohon Kosong)
        self.root = None

    def insert(self, produk):
        """Menambahkan objek Produk ke dalam BST berdasarkan kode_produk."""
        if self.root is None:
            self.root = Node(produk)
        else:
            self._insert_recursive(self.root, produk)

    def _insert_recursive(self, current, produk):
        if produk.kode < current.data.kode:
            if current.left is None:
                current.left = Node(produk)
            else:
                self._insert_recursive(current.left, produk)
        elif produk.kode > current.data.kode:
            if current.right is None:
                current.right = Node(produk)
            else:
                self._insert_recursive(current.right, produk)

    def search(self, kode):
        """Mencari produk dan mengembalikan data produknya (bukan objek Node)."""
        res = self._search_recursive(self.root, kode)
        return res.data if res else None

    def _search_recursive(self, current, kode):
        if current is None or current.data.kode == kode:
            return current
        if kode < current.data.kode:
            return self._search_recursive(current.left, kode)
        return self._search_recursive(current.right, kode)

    def update_stok(self, kode, delta):
        """Update stok produk berdasarkan delta (+ atau -)."""
        produk = self.search(kode)
        if produk:
            produk.stok += delta
            return True
        return False

    def filter_kadaluarsa(self, current, maks_hari):
        """Menampilkan produk yang sisa harinya <= maks_hari (In-order)."""
        if current:
            self.filter_kadaluarsa(current.left, maks_hari)
            if current.data.masa_kadaluarsa_hari <= maks_hari:
                print(f" > [ALERT] {current.data.nama} (Kode: {current.data.kode}) - Sisa {current.data.masa_kadaluarsa_hari} hari!")
            self.filter_kadaluarsa(current.right, maks_hari)

    def inorder(self, current):
        """Menampilkan semua produk urut berdasarkan kode."""
        if current:
            self.inorder(current.left)
            p = current.data
            print(f" > [Kode: {p.kode}] {p.nama:15} | Stok: {p.stok:3} | Exp: {p.masa_kadaluarsa_hari:3} hari")
            self.inorder(current.right)

# --- Demonstrasi Sesuai Starter.py Dosen ---
if __name__ == "__main__":
    from dataclasses import dataclass

    @dataclass
    class Produk:
        kode: str
        nama: str
        kategori: str
        harga_satuan: float
        stok: int
        masa_kadaluarsa_hari: int

    katalog = BSTKatalog()
    
    print("\n" + "="*60)
    print("SISTEM MANAGEMENT KATALOG - URBAN FOOD SUPPLY CHAIN")
    print("KELOMPOK 5 - TEKNOLOGI INFORMASI")
    print("="*60)

    # Contoh input data lengkap sesuai spesifikasi tugas
    katalog.insert(Produk("105", "Cabai Merah", "SAYUR", 25000.0, 50, 5))
    katalog.insert(Produk("101", "Beras Premium", "BAHAN_POKOK", 14000.0, 200, 180))
    katalog.insert(Produk("110", "Tomat Organik", "SAYUR", 18000.0, 30, 3))
    katalog.insert(Produk("103", "Daging Ayam", "DAGING", 35000.0, 15, 2))

    print("\n[INFO] Daftar Katalog Produk (In-order):")
    katalog.inorder(katalog.root)

    print("\n[SISTEM] Update stok Beras (Kode 101) +50...")
    katalog.update_stok("101", 50)

    print("\n[FILTER] Produk hampir kadaluarsa (<= 4 hari):")
    katalog.filter_kadaluarsa(katalog.root, 4)

    print("="*60 + "\n")