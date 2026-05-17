import unittest
from src.modules.bst_katalog_produk import KatalogProduk, Produk

class TestKatalogProduk(unittest.TestCase):
    def test_insert_and_search(self):
        katalog = KatalogProduk()
        p1 = Produk(101, "Beras", "Pokok", 15000, 100, 30)
        p2 = Produk(102, "Tomat", "Sayur", 8000, 50, 4)
        
        katalog.insert_produk(p1)
        katalog.insert_produk(p2)
        
        hasil_search = katalog.search_produk(katalog.root, 102)
        self.assertEqual(hasil_search.data.nama, "Tomat")
        
        mendekati_kadaluarsa = katalog.filter_kadaluarsa(katalog.root, 5)
        self.assertEqual(len(mendekati_kadaluarsa), 1)
        
        # PERBAIKAN: Mengakses indeks [0] sebelum mengambil properti .nama
        self.assertEqual(mendekati_kadaluarsa[0].nama, "Tomat")

if __name__ == '__main__':
    unittest.main()
