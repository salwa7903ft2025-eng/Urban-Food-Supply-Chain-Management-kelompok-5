import sys
import os
import unittest

# Menambahkan folder 'src' ke dalam sys.path agar modul bisa diimpor dari folder 'tests'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_structures.queue_ll import QueueLL


class TestQueueLL(unittest.TestCase):
    def setUp(self):
        """Membuat instance queue baru sebelum setiap test dijalankan."""
        self.queue = QueueLL()

    def test_initial_state(self):
        """Memastikan queue baru dalam kondisi kosong."""
        self.assertIsNone(self.queue.front)
        self.assertIsNone(self.queue.rear)

    def test_enqueue_single_element(self):
        """Memastikan enqueue satu elemen berhasil."""
        self.queue.enqueue(10)
        self.assertEqual(self.queue.front.data, 10)
        self.assertEqual(self.queue.rear.data, 10)

    def test_enqueue_multiple_elements(self):
        """Memastikan urutan FIFO benar saat enqueue beberapa elemen."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.front.data, 10)
        self.assertEqual(self.queue.rear.data, 30)

    def test_dequeue_single_element(self):
        """Memastikan dequeue pada queue berisi satu elemen mengosongkan queue kembali."""
        self.queue.enqueue(10)
        data = self.queue.dequeue()
        self.assertEqual(data, 10)
        self.assertIsNone(self.queue.front)
        self.assertIsNone(self.queue.rear)

    def test_dequeue_multiple_elements(self):
        """Memastikan data keluar sesuai urutan masuk (FIFO)."""
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.queue.enqueue("C")
        
        self.assertEqual(self.queue.dequeue(), "A")
        self.assertEqual(self.queue.dequeue(), "B")
        self.assertEqual(self.queue.dequeue(), "C")

    def test_dequeue_empty_queue(self):
        """Memastikan dequeue pada queue kosong menghasilkan None."""
        self.assertIsNone(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()
