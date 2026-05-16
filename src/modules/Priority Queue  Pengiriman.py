from dataclasses import dataclass
import time

@dataclass
class Pengiriman:
    pengiriman_id: int
    dari_node: str
    ke_node: str
    kode_produk: str
    jumlah: int
    prioritas: int
    waktu_kirim: float


class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class PriorityQueueKirim:
    """
    Priority Queue Pengiriman

    Prioritas:
    1 = MENDESAK   (kadaluarsa <= 3 hari)
    2 = NORMAL     (4 - 7 hari)
    3 = REGULER    (> 7 hari)

    Queue selalu terurut ascending:
    prioritas kecil = lebih penting

    Big-O:
    enqueue  -> O(n)
    dequeue  -> O(1)
    """

    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, pengiriman):
        """
        Menambahkan pengiriman sesuai urutan prioritas.
        Big-O: O(n)
        """

        new_node = LLNode(pengiriman)

        # jika queue kosong
        if self.head is None:
            self.head = new_node

        # jika prioritas lebih tinggi dari head
        elif pengiriman.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head

            # cari posisi insertion
            while (
                current.next is not None
                and current.next.data.prioritas <= pengiriman.prioritas
            ):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        self._size += 1
#ntar gw lanjut :v
    def dequeue(self):
        """
        Menghapus pengiriman prioritas tertinggi.
        Big-O: O(1)
        """

        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next

        self._size -= 1

        return removed

    def peek(self):
        """
        Melihat elemen terdepan tanpa menghapus.
        """

        if self.head is None:
            return None

        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        """
        Menampilkan isi queue.
        """

        if self.head is None:
            print("Queue kosong")
            return

        current = self.head

        while current is not None:
            p = current.data

            print(
                f"[ID:{p.pengiriman_id}] "
                f"{p.kode_produk} | "
                f"{p.dari_node} -> {p.ke_node} | "
                f"Jumlah: {p.jumlah} | "
                f"Prioritas: {p.prioritas}"
            )

            current = current.next

    def __len__(self):
        return self._size

# if __name__ == "__main__":

#     pq = PriorityQueueKirim()

#     p1 = Pengiriman(
#         1, "PTN01", "PSR01",
#         "PRD-001", 100,
#         3,
#         time.time()
#     )

#     p2 = Pengiriman(
#         2, "PTN02", "PSR02",
#         "PRD-002", 50,
#         1,
#         time.time()
#     )

#     p3 = Pengiriman(
#         3, "PTN03", "PSR03",
#         "PRD-003", 70,
#         2,
#         time.time()
#     )

#     pq.enqueue(p1)
#     pq.enqueue(p2)
#     pq.enqueue(p3)

#     print("Isi Priority Queue:")
#     pq.display()

#     print("\nProses Pengiriman:")
#     while not pq.is_empty():
#         kirim = pq.dequeue()

#         print(
#             f"Memproses {kirim.kode_produk} "
#             f"dengan prioritas {kirim.prioritas}"
#         )
