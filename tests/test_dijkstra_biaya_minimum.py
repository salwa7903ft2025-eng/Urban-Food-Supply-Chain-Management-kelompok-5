import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.graph_rantai_pasok import GraphRantaiPasok
from modules.dijkstra_biaya_minimum import dijkstra_biaya, rekonstruksi_jalur 

graph = GraphRantaiPasok()

graph.tambah_node('A', 'PETANI')
graph.tambah_node('B', 'DISTRIBUTOR')
graph.tambah_node('C', 'PASAR')

graph.tambah_jalur('A', 'B', 10, 1000)
graph.tambah_jalur('B', 'C', 5, 2000)
graph.tambah_jalur('A', 'C', 30, 500)

dist, parent = dijkstra_biaya(graph, 'A')

print('Distance:')
print(dist)

print('\nPath A -> C:')
print(rekonstruksi_jalur(parent, 'C'))