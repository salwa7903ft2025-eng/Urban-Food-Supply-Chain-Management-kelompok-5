import unittest
from src.modules.circular_queue_buffer_gudang import CircularQueueBuffer

class TestCircularQueueBuffer(unittest.TestCase):
    def test_enqueue_dequeue(self):
        cq = CircularQueueBuffer(capacity=3)
        self.assertTrue(cq.is_empty())
        
        cq.enqueue("Produk1")
        cq.enqueue("Produk2")
        cq.enqueue("Produk3")
        
        self.assertTrue(cq.is_full())
        self.assertFalse(cq.enqueue("Produk4")) # Harus gagal
        
        self.assertEqual(cq.dequeue(), "Produk1")
        self.assertFalse(cq.is_full())

if __name__ == '__main__':
    unittest.main()