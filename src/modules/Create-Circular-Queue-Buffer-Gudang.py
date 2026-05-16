from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Produk:
    kode: str
    nama: str
    kategori: str
    harga_satuan: float
    stok: int
    masa_kadaluarsa_hari: int

# ==============================================================================
# MODUL 2: CIRCULAR QUEUE (BUFFER GUDANG) - KAPASITAS 50
# ==============================================================================
class CircularQueue:
    """
    Circular Queue berbasis array dengan kapasitas tetap (fixed capacity = 50).
    Digunakan sebagai buffer FIFO untuk stok di setiap gudang/node.
    """
    def __init__(self, kapasitas: int = 50):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, produk: Produk) -> bool:
        """Big-O: O(1). Menambahkan produk di posisi rear. Mengembalikan False jika penuh."""
        if self.is_full():
            print(f" -> [Peringatan] Gagal Enqueue: Buffer Penuh saat memasukkan {produk.nama}!")
            return False
        self.buffer[self.rear] = produk
        self.rear = (self.rear + 1) % self.kapasitas
        self.size += 1
        return True

    def dequeue(self) -> Optional[Produk]:
        """Big-O: O(1). Mengambil produk terlama di posisi front (FIFO)."""
        if self.is_empty():
            return None
        produk = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self.size -= 1
        return produk

    def is_full(self) -> bool:
        """Big-O: O(1). Cek apakah buffer penuh."""
        return self.size == self.kapasitas

    def is_empty(self) -> bool:
        """Big-O: O(1). Cek apakah buffer kosong."""
        return self.size == 0

    def display_queue(self) -> List[str]:
        """Helper untuk menampilkan daftar isi buffer secara berurutan."""
        items = []
        idx = self.front
        for _ in range(self.size):
            if self.buffer[idx]:
                items.append(f"{self.buffer[idx].nama} ({self.buffer[idx].kode}) - Jumlah: {self.buffer[idx].stok}")
            idx = (idx + 1) % self.kapasitas
        return items

# ==============================================================================
# ==============================================================================
def main():
    print("=" * 60)
    print(" Pengujian Murni Modul 2: Circular Queue Buffer (Kapasitas 50) ")
    print("=" * 60)

    # Inisialisasi Buffer Gudang dengan kapasitas 50
    buffer_gudang_00 = CircularQueue(kapasitas=50)

    # Membuat objek produk secara manual langsung tanpa BST
    produk_a = Produk("PRD001", "Beras", "BAHAN_POKOK", 12000, 15, 30)
    produk_b = Produk("PRD002", "Cabai", "SAYUR", 35000, 30, 5)
    produk_c = Produk("PRD003", "Tomat", "SAYUR", 15000, 25, 7)

    print("\n[PROSES] Mengisi Buffer Gudang (Enqueue - O(1)):")
    buffer_gudang_00.enqueue(produk_a)
    print(" -> Beras berhasil masuk ke antrian.")
    buffer_gudang_00.enqueue(produk_b)
    print(" -> Cabai berhasil masuk ke antrian.")
    buffer_gudang_00.enqueue(produk_c)
    print(" -> Tomat berhasil masuk ke antrian.")

    print("\n[STATUS] Memeriksa Isi Buffer Gudang Saat Ini:")
    print(f"Jumlah slot terpakai: {buffer_gudang_00.size}/{buffer_gudang_00.kapasitas}")
    for item in buffer_gudang_00.display_queue():
        print(f" -> {item}")

    print("\n[PROSES] Mengeluarkan Barang Terlama (Dequeue FIFO - O(1)):")
    terambil = buffer_gudang_00.dequeue()
    if terambil:
        print(f" -> Berhasil mengeluarkan: {terambil.nama} (Kode: {terambil.kode})")

    print("\n[STATUS KONDISI AKHIR] Memeriksa Sisa Buffer Gudang:")
    print(f"Jumlah slot terpakai: {buffer_gudang_00.size}/{buffer_gudang_00.kapasitas}")
    for item in buffer_gudang_00.display_queue():
        print(f" -> {item}")

if __name__ == "__main__":
    main()
