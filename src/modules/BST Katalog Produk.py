import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.node import Node

class BSTKatalog:
    def __init__(self):
        self.root = None

    def insert(self, produk):
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
        res = self._search_recursive(self.root, kode)
        return res.data if res else None

    def _search_recursive(self, current, kode):
        if current is None or current.data.kode == kode:
            return current
        if kode < current.data.kode:
            return self._search_recursive(current.left, kode)
        return self._search_recursive(current.right, kode)

    def update_stok(self, kode, delta):
        produk = self.search(kode)
        if produk:
            produk.stok += delta
            return True
        return False

    def filter_kadaluarsa(self, current, maks_hari):
        if current:
            self.filter_kadaluarsa(current.left, maks_hari)
            if current.data.masa_kadaluarsa_hari <= maks_hari:
                print(f" > [ALERT] {current.data.nama} (Kode: {current.data.kode}) - Sisa {current.data.masa_kadaluarsa_hari} hari!")
            self.filter_kadaluarsa(current.right, maks_hari)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            p = current.data
            print(f" > [Kode: {p.kode:3}] {p.nama:15} | Stok: {p.stok:3} | Exp: {p.masa_kadaluarsa_hari:3} hari")
            self.inorder(current.right)

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
    print("KELOMPOK 5 - TEKNOLOGI ELEKTRO UNY")
    print("="*60)

    katalog.insert(Produk("105", "Cabai Merah", "SAYUR", 25000.0, 50, 5))
    katalog.insert(Produk("101", "Beras Premium", "BAHAN_POKOK", 14000.0, 200, 180))
    katalog.insert(Produk("110", "Tomat Organik", "SAYUR", 18000.0, 30, 3))
    katalog.insert(Produk("103", "Daging Ayam", "DAGING", 35000.0, 15, 2))

    print("\n[INFO] Daftar Katalog Produk (Urut Kode):")
    katalog.inorder(katalog.root)

    print(f"\n[SISTEM] Update stok Beras (Kode 101) +50...")
    katalog.update_stok("101", 50)

    print("\n[FILTER] Produk hampir kadaluarsa (<= 4 hari):")
    katalog.filter_kadaluarsa(katalog.root, 4)

    print("\n" + "="*60)