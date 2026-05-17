from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Produk:
    kode: str; nama: str; kategori: str; harga_satuan: float; stok: int; masa_kadaluarsa_hari: int

class CircularQueue:
    def __init__(self, kapasitas: int = 50):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = self.rear = self.size = 0

    def enqueue(self, produk: Produk) -> bool:
        if self.size == self.kapasitas:
            print(f" -> Buffer Penuh: {produk.nama}!")
            return False
        self.buffer[self.rear] = produk
        self.rear = (self.rear + 1) % self.kapasitas
        self.size += 1
        return True

    def dequeue(self) -> Optional[Produk]:
        if self.size == 0: return None
        produk = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self.size -= 1
        return produk

    def display_queue(self) -> List[str]:
        items, idx = [], self.front
        for _ in range(self.size):
            p = self.buffer[idx]
            if p: items.append(f"{p.nama} ({p.kode}) - Stok: {p.stok}")
            idx = (idx + 1) % self.kapasitas
        return items

def main():
    q = CircularQueue(kapasitas=50)
    
    # 1. Enqueue
    q.enqueue(Produk("PRD001", "Beras", "POKOK", 12000, 15, 30))
    q.enqueue(Produk("PRD002", "Cabai", "SAYUR", 35000, 30, 5))
    q.enqueue(Produk("PRD003", "Tomat", "SAYUR", 15000, 25, 7))
    print(f"Isi Awal ({q.size}/{q.kapasitas}):\n", "\n ".join(q.display_queue()))

    # 2. Dequeue
    terambil = q.dequeue()
    print(f"\nDirendahkan/Dequeue: {terambil.nama if terambil else 'Kosong'}")
    
    # 3. Status Akhir
    print(f"\nIsi Akhir ({q.size}/{q.kapasitas}):\n", "\n ".join(q.display_queue()))

if __name__ == "__main__":
    main()
