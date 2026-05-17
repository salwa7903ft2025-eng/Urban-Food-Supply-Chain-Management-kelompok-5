from ..data_structures.graph import Graph

class GraphRantaiPasok(Graph):
    def __init__(self):
        super().__init__()
        
    def add_edge_weighted(self, v1, v2, jarak, biaya):
        """
        Menambahkan jalur distribusi dengan bobot jarak (km) dan biaya per km.
        Big-O: O(1)
        """
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Hapus koneksi default jika ada, lalu ganti dengan dictionary berbobot
        self.adj_list[v1].append({"node": v2, "jarak": jarak, "biaya": biaya})
        self.adj_list[v2].append({"node": v1, "jarak": jarak, "biaya": biaya})

    def dfs_audit(self, start, visited=None):
        """
        Audit konektivitas jaringan menggunakan DFS.
        Big-O: O(V + E)
        """
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        
        for neighbor_data in self.adj_list.get(start, []):
            neighbor = neighbor_data if isinstance(neighbor_data, str) else neighbor_data["node"]
            if neighbor not in visited:
                self.dfs_audit(neighbor, visited)
        return visited