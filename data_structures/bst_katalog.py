try:
    from .node import Node 
except ImportError:
    from node import Node  

class BSTKatalog:
    """
    Class BSTKatalog untuk mengelola data produk dalam Urban Food Supply Chain.
    Menggunakan struktur Binary Search Tree untuk efisiensi pencarian O(log n).
    """
    def __init__(self):
        # Inisialisasi root sebagai None (Pohon Kosong)
        self.root = None

    def tambah_produk(self, kode, nama):
        """
        Public method untuk menambah produk baru ke dalam katalog.
        """
        if self.root is None:
            self.root = Node({'kode': kode, 'nama': nama})
        else:
            self._tambah_recursive(self.root, kode, nama)

    def _tambah_recursive(self, current, kode, nama):
        """
        Helper method (Private) untuk menyisipkan node secara rekursif.
        """
        if kode < current.data['kode']:
            if current.left is None:
                current.left = Node({'kode': kode, 'nama': nama})
            else:
                self._tambah_recursive(current.left, kode, nama)
        elif kode > current.data['kode']:
            if current.right is None:
                current.right = Node({'kode': kode, 'nama': nama})
            else:
                self._tambah_recursive(current.right, kode, nama)

    def cari_produk(self, kode):
        """
        Public method untuk mencari informasi produk berdasarkan kode.
        """
        return self._cari_recursive(self.root, kode)

    def _cari_recursive(self, current, kode):
        """
        Helper method (Private) untuk pencarian secara rekursif.
        """
        if current is None or current.data['kode'] == kode:
            return current
        
        if kode < current.data['kode']:
            return self._cari_recursive(current.left, kode)
        return self._cari_recursive(current.right, kode)

    def cetak_katalog_inorder(self, current):
        """
        Menampilkan semua produk secara berurutan berdasarkan kode (In-order Traversal).
        Sering ditanyakan oleh dosen saat praktikum.
        """
        if current:
            self.cetak_katalog_inorder(current.left)
            print(f" > [ID: {current.data['kode']}] Nama: {current.data['nama']}")
            self.cetak_katalog_inorder(current.right)

# --- PROGRAM UTAMA (GAYA DOSEN) ---
if __name__ == "__main__":
    katalog = BSTKatalog()
    
    print("\n" + "="*50)
    print("SISTEM MANAJEMEN KATALOG URBAN FOOD - KELOMPOK 5")
    print("="*50)

    # 1. Menambahkan beberapa data produk
    produk_list = [
        (105, "Cabai Merah"),
        (102, "Beras Premium"),
        (110, "Tomat Organik"),
        (101, "Bawang Putih"),
        (108, "Minyak Goreng")
    ]

    for kode, nama in produk_list:
        katalog.tambah_produk(kode, nama)
    
    print(f"Berhasil menambahkan {len(produk_list)} produk ke sistem.")

    # 2. Menampilkan katalog secara berurutan
    print("\nDAFTAR KATALOG PRODUK (Urut Kode):")
    katalog.cetak_katalog_inorder(katalog.root)

    # 3. Simulasi Pencarian
    print("\nFITUR PENCARIAN PRODUK:")
    target = 110
    print(f"Mencari produk dengan Kode: {target}...")
    
    hasil = katalog.cari_produk(target)
    if hasil:
        print(f"HASIL: Produk ditemukan! Nama: {hasil.data['nama']}")
    else:
        print("HASIL: Produk tidak ditemukan dalam sistem.")
    
    print("="*50 + "\n")