from ..data_structures.bst import BST, TreeNode

class Produk:
    def __init__(self, kode, nama, kategori, harga, stok, masa_kadaluarsa):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.masa_kadaluarsa = masa_kadaluarsa

    def __lt__(self, other):
        return self.kode < other.kode
        
    def __str__(self):
        return f"[{self.kode}] {self.nama} (Stok: {self.stok}, Exp: {self.masa_kadaluarsa} hari)"

class KatalogProduk(BST):
    def insert_produk(self, produk):
        """Big-O: O(log n) rata-rata"""
        self.insert(produk)

    def search_produk(self, node, kode):
        """Big-O: O(log n) rata-rata"""
        if node is None or node.data.kode == kode:
            return node
        if kode < node.data.kode:
            return self.search_produk(node.left, kode)
        return self.search_produk(node.right, kode)

    def filter_kadaluarsa(self, node, maks_hari, hasil=None):
        """
        Inorder traversal dengan filter.
        Big-O: O(n)
        """
        if hasil is None:
            hasil = []
        if node:
            self.filter_kadaluarsa(node.left, maks_hari, hasil)
            if node.data.masa_kadaluarsa <= maks_hari:
                hasil.append(node.data)
            self.filter_kadaluarsa(node.right, maks_hari, hasil)
        return hasil