class EdgeNode:
    def __init__(self, dest, jarak_km, biaya_per_km):
        self.dest = dest
        self.jarak_km = jarak_km
        self.biaya_per_km = biaya_per_km
        self.next = None

        # PERBAIKAN: Tambahkan method untuk menghitung total biaya

class GraphRantaiPasok:
    def __init__(self):
        self.adj = {}
        self.tipe_node = {}

    def tambah_node(self, node_id, tipe):
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.tipe_node[node_id] = tipe

    def tambah_jalur(self, u, v, jarak, biaya_km):
        edge_uv = EdgeNode(v, jarak, biaya_km)
        edge_uv.next = self.adj[u]
        self.adj[u] = edge_uv

        edge_vu = EdgeNode(u, jarak, biaya_km)
        edge_vu.next = self.adj[v]
        self.adj[v] = edge_vu

    def tetangga(self, u):
        hasil = []
        curr = self.adj.get(u)

        while curr:
            hasil.append({
                'tujuan': curr.dest,
                'jarak_km': curr.jarak_km,
                'biaya_per_km': curr.biaya_per_km,
                'total_biaya': curr.jarak_km * curr.biaya_per_km
            })
            curr = curr.next

        return hasil

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        curr = self.adj[start]
        while curr:
            if curr.dest not in visited:
                self.dfs(curr.dest, visited)
            curr = curr.next

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=' ')

            curr = self.adj[node]
            while curr:
                if curr.dest not in visited:
                    visited.add(curr.dest)
                    queue.append(curr.dest)
                curr = curr.next