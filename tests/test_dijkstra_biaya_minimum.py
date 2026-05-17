import unittest
from src.modules.graph_rantai_pasok import GraphRantaiPasok
from src.modules.dijkstra_biaya_minimum import dijkstra_biaya_minimum, merge_sort_jalur

class TestDijkstraAndSort(unittest.TestCase):
    def test_dijkstra(self):
        g = GraphRantaiPasok()
        g.add_edge_weighted("A", "B", 10, 10) # cost = 100
        g.add_edge_weighted("B", "C", 5, 10)  # cost = 50
        g.add_edge_weighted("A", "C", 20, 10) # cost = 200
        
        distances, prev = dijkstra_biaya_minimum(g, "A")
        self.assertEqual(distances["C"], 150) # Lewat B lebih murah
        
    def test_merge_sort(self):
        jalur = [{"rute": "A-B", "biaya": 500}, {"rute": "C-D", "biaya": 100}, {"rute": "E-F", "biaya": 300}]
        sorted_jalur = merge_sort_jalur(jalur)
        
        # PERBAIKAN: Gunakan indeks [0] untuk elemen pertama (terkecil)
        self.assertEqual(sorted_jalur[0]["biaya"], 100)
        
        # PERBAIKAN: Gunakan indeks [2] atau [-1] untuk elemen terakhir (terbesar)
        self.assertEqual(sorted_jalur[2]["biaya"], 500)

if __name__ == '__main__':
    unittest.main()
