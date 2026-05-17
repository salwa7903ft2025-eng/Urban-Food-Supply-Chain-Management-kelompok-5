import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.graph_rantai_pasok import GraphRantaiPasok

graph = GraphRantaiPasok()

graph.tambah_node('PTN01', 'PETANI')
graph.tambah_node('DST01', 'DISTRIBUTOR')

graph.tambah_jalur('PTN01', 'DST01', 25, 3000)

print('Tetangga PTN01:')
print(graph.tetangga('PTN01'))

print('\nDFS:')
graph.dfs('PTN01')

print('\n\nBFS:')
graph.bfs('PTN01')