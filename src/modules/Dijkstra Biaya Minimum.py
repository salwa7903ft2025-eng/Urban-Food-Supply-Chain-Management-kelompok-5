# NEXT
class EdgeNode:
    def __init__(self, dest, jarak_km, biaya_per_km):
        self.dest = dest
        self.jarak_km = jarak_km
        self.biaya_per_km = biaya_per_km
        self.next = None


class GraphRantaiPasok:
    """
    Graph rantai pasok menggunakan adjacency list.
    """

    def __init__(self):
        self.adj = {}

    def tambah_node(self, node_id):
        """
        Menambahkan node baru.
        Big-O: O(1)
        """

        if node_id not in self.adj:
            self.adj[node_id] = None

    def tambah_jalur(self, u, v, jarak, biaya_km):
        """
        Menambahkan edge dua arah.
        Bobot = jarak * biaya_km

        Big-O: O(1)
        """

        edge_uv = EdgeNode(v, jarak, biaya_km)
        edge_uv.next = self.adj[u]
        self.adj[u] = edge_uv

        edge_vu = EdgeNode(u, jarak, biaya_km)
        edge_vu.next = self.adj[v]
        self.adj[v] = edge_vu

    def tetangga(self, u):
        """
        Mengambil semua tetangga node.
        Big-O: O(deg)
        """

        result = []

        current = self.adj[u]

        while current is not None:
            result.append(current)
            current = current.next

        return result


def dijkstra_biaya(graph, asal):
    """
    Dijkstra shortest path berdasarkan:

        bobot = jarak_km * biaya_per_km

    Big-O: O(V^2 + E)
    """

    INF = float('inf')

    dist = {}
    parent = {}
    visited = set()

    # inisialisasi
    for v in graph.adj:
        dist[v] = INF
        parent[v] = None

    dist[asal] = 0

    while len(visited) < len(graph.adj):

        # cari node minimum yang belum dikunjungi
        min_node = None
        min_dist = INF

        for node in graph.adj:
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        # relaksasi edge
        current = graph.adj[min_node]

        while current is not None:

            bobot = current.jarak_km * current.biaya_per_km

            if dist[min_node] + bobot < dist[current.dest]:

                dist[current.dest] = dist[min_node] + bobot
                parent[current.dest] = min_node

            current = current.next

    return dist, parent


def rekonstruksi_jalur(parent, tujuan):
    """
    Rekonstruksi jalur dari hasil Dijkstra.
    """

    path = []

    current = tujuan

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path


# ==========================================
# MERGE SORT UNTUK AUDIT BIAYA
# ==========================================

def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort_biaya(data):
    """
    Mengurutkan jalur berdasarkan total biaya.

    Format data:
    [
        (tujuan, biaya),
        ...
    ]

    Big-O: O(n log n)
    """

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort_biaya(data[:mid])
    right = merge_sort_biaya(data[mid:])

    return merge(left, right)
