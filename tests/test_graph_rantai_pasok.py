import unittest
from src.modules.graph_rantai_pasok import GraphRantaiPasok

class TestGraphRantaiPasok(unittest.TestCase):
    def test_add_edge_and_dfs(self):
        g = GraphRantaiPasok()
        g.add_edge_weighted("PetaniA", "Distributor1", jarak=10, biaya=5000)
        g.add_edge_weighted("Distributor1", "PasarX", jarak=5, biaya=7000)
        
        visited = g.dfs_audit("PetaniA")
        self.assertIn("PasarX", visited)
        self.assertEqual(len(visited), 3)

if __name__ == '__main__':
    unittest.main()