class PengirimanNode:
    def __init__(self, dari, ke, kode_produk, jumlah, masa_kadaluarsa):
        self.dari = dari
        self.ke = ke
        self.kode_produk = kode_produk
        self.jumlah = jumlah
        self.masa_kadaluarsa = masa_kadaluarsa
        
        # Penentuan prioritas: 1 (Mendesak), 2 (Normal), 3 (Reguler)
        if masa_kadaluarsa <= 3:
            self.priority = 1
        elif 4 <= masa_kadaluarsa <= 7:
            self.priority = 2
        else:
            self.priority = 3
            
        self.next = None

class PriorityQueuePengiriman:
    def __init__(self):
        self.head = None

    def enqueue(self, dari, ke, kode, jumlah, masa_kadaluarsa):
        """
        Menambahkan antrean pengiriman berdasar prioritas.
        Big-O: O(n)
        """
        new_node = PengirimanNode(dari, ke, kode, jumlah, masa_kadaluarsa)
        
        if self.head is None or self.head.priority > new_node.priority:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.priority <= new_node.priority:
            current = current.next
            
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        """
        Memproses pengiriman dengan prioritas tertinggi.
        Big-O: O(1)
        """
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp