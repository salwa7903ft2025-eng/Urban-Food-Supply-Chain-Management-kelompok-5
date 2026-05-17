import unittest
from src.modules.cli_rantai_pasok import CLI

class TestCLIRantaiPasok(unittest.TestCase):
    def setUp(self):
        # Dijalankan sebelum setiap test dimulai
        self.cli = CLI()

    def test_inisialisasi_cli(self):
        # Memastikan semua modul utama terhubung di dalam CLI
        self.assertIsNotNone(self.cli.graph)
        self.assertIsNotNone(self.cli.katalog)
        self.assertIsNotNone(self.cli.pq_pengiriman)
        self.assertEqual(len(self.cli.buffers), 0)

    def test_kirim_dan_proses(self):
        # 1. Uji perintah KIRIM: Memasukkan produk ke antrean prioritas (Priority Queue)
        self.cli.kirim("PetaniA", "GudangB", "P01", 50, 2) # masa kadaluarsa 2 = Mendesak
        
        # Pastikan data ada di antrean pengiriman
        self.assertIsNotNone(self.cli.pq_pengiriman.head)
        self.assertEqual(self.cli.pq_pengiriman.head.kode_produk, "P01")
        
        # 2. Uji perintah PROSES_KIRIM: Memindahkan dari antrean prioritas ke Circular Queue di tujuan
        self.cli.proses_kirim()
        
        # Pastikan buffer GudangB dibuat otomatis
        self.assertIn("GudangB", self.cli.buffers)
        
        # Pastikan produk berhasil ditaruh ke dalam buffer GudangB
        item_di_buffer = self.cli.buffers["GudangB"].dequeue()
        self.assertIsNotNone(item_di_buffer)
        self.assertEqual(item_di_buffer["kode"], "P01")
        self.assertEqual(item_di_buffer["jumlah"], 50)
        
        # Pastikan antrean pengiriman sudah kosong setelah diproses
        self.assertIsNone(self.cli.pq_pengiriman.head)

if __name__ == '__main__':
    unittest.main()