import unittest
from src.modules.priority_queue_pengiriman import PriorityQueuePengiriman

class TestPriorityQueuePengiriman(unittest.TestCase):
    def test_priority(self):
        pq = PriorityQueuePengiriman()
        # Normal (4-7 hari)
        pq.enqueue("A", "B", "P02", 10, 5) 
        # Mendesak (<= 3 hari)
        pq.enqueue("A", "B", "P01", 10, 2) 
        # Reguler (> 7 hari)
        pq.enqueue("A", "B", "P03", 10, 10) 
        
        first = pq.dequeue()
        self.assertEqual(first.kode_produk, "P01") # Mendesak keluar pertama
        second = pq.dequeue()
        self.assertEqual(second.kode_produk, "P02")

if __name__ == '__main__':
    unittest.main()