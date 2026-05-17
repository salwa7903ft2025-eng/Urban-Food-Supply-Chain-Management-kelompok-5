from typing import Optional, List, Tuple, Dict, Any
import os

class EdgeNode:
    def __init__(self, dest: str, jarak_km: int, biaya_per_km: float):
        self.dest: str = dest
        self.jarak_km: int = jarak_km
        self.biaya_per_km: float = biaya_per_km
        self.next: Optional['EdgeNode'] = None

class LLNode:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional['LLNode'] = None

class CustomQueue:
    def __init__(self):
        self.head: Optional[LLNode] = None
        self.tail: Optional[LLNode] = None
        
    def enqueue(self, data: Any) -> None:
        new_node = LLNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def dequeue(self) -> Optional[Any]:
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data
    
    def is_empty(self) -> bool:
        return self.head is None

class CustomStack:
    def __init__(self):
        self.top: Optional[LLNode] = None
        
    def push(self, data: Any) -> None:
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self) -> Optional[Any]:
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
    
    def is_empty(self) -> bool:
        return self.top is None

class GraphRantaiPasok:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}

    def tambah_node(self, node_id: str) -> None:
        if node_id not in self.adj:
            self.adj[node_id] = None

    def tambah_jalur(self, u: str, v: str, jarak_km: int, biaya_km: float) -> None:
        if u not in self.adj: self.tambah_node(u)
        if v not in self.adj: self.tambah_node(v)

        node_uv = EdgeNode(v, jarak_km, biaya_km)
        node_uv.next = self.adj[u]
        self.adj[u] = node_uv

        node_vu = EdgeNode(u, jarak_km, biaya_km)
        node_vu.next = self.adj[v]
        self.adj[v] = node_vu

    def tetangga(self, u: str) -> List[Tuple[str, int, float]]:
        result = []
        if u not in self.adj:
            return result
        current = self.adj[u]
        while current is not None:
            result.append((current.dest, current.jarak_km, current.biaya_per_km))
            current = current.next
        return result

    def audit_konektivitas_bfs(self, source: str) -> List[str]:
        visited = set()
        order = []
        queue = CustomQueue()
        if source in self.adj:
            queue.enqueue(source)
            visited.add(source)
        while not queue.is_empty():
            u = queue.dequeue()
            order.append(u)
            curr = self.adj[u]
            while curr is not None:
                if curr.dest not in visited:
                    visited.add(curr.dest)
                    queue.enqueue(curr.dest)
                curr = curr.next
        return order

    def audit_konektivitas_dfs(self, source: str) -> List[str]:
        visited = set()
        order = []
        stack = CustomStack()
        if source in self.adj:
            stack.push(source)
        while not stack.is_empty():
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                order.append(u)
                curr = self.adj[u]
                while curr is not None:
                    if curr.dest not in visited:
                        stack.push(curr.dest)
                    curr = curr.next
        return order

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def inisialisasi_peta(graph: GraphRantaiPasok):
    nodes = ["PTN01", "PTN02", "PTN03", "GDG01", "GDG02", "GDG03", "GDG04", "PSR01", "PSR02", "PSR03"]
    for node in nodes:
        graph.tambah_node(node)

    graph.tambah_jalur("PTN01", "GDG01", 90, 12.0)
    graph.tambah_jalur("PTN01", "GDG02", 110, 14.5)
    graph.tambah_jalur("PTN02", "GDG03", 65, 11.0)
    graph.tambah_jalur("PTN02", "GDG01", 180, 9.5)
    graph.tambah_jalur("PTN03", "GDG03", 45, 13.0)
    graph.tambah_jalur("PTN03", "GDG04", 260, 8.5)
    graph.tambah_jalur("GDG01", "GDG02", 70, 10.5)
    graph.tambah_jalur("GDG02", "PSR01", 45, 15.0)
    graph.tambah_jalur("GDG01", "PSR01", 120, 11.5)
    graph.tambah_jalur("GDG03", "PSR02", 15, 16.0)
    graph.tambah_jalur("GDG03", "GDG02", 310, 8.0)
    graph.tambah_jalur("GDG03", "GDG04", 280, 7.5)
    graph.tambah_jalur("GDG04", "PSR03", 20, 15.5)
    graph.tambah_jalur("GDG02", "PSR02", 320, 8.2)
    graph.tambah_jalur("GDG04", "PSR02", 290, 7.8)

def main():
    graph = GraphRantaiPasok()
    inisialisasi_peta(graph)

    while True:
        bersihkan_layar()
        print("========================================================================")
        print("           SISTEM AUDIT STRUKTUR GRAF MODUL 1 - AGRO LOGISTIK           ")
        print("========================================================================")
        print(" [1] Lihat Daftar Kedekatan Tetangga Simpul (Adjacency List)")
        print(" [2] Jalankan Audit Konektivitas Metode BFS (Breadth-First Search)")
        print(" [3] Jalankan Audit Konektivitas Metode DFS (Depth-First Search)")
        print(" [0] Keluar Aplikasi")
        print("========================================================================")
        
        pilihan = input("Pilih Menu [0-3]: ").strip()

        if pilihan == "1":
            print("\n--- DAFTAR ADJACENCY LIST JARINGAN ---")
            node_id = input("Masukkan Kode Simpul (Contoh: PTN01, GDG01): ").strip().upper()
            if node_id in graph.adj:
                list_tetangga = graph.tetangga(node_id)
                if list_tetangga:
                    for t, j, b in list_tetangga:
                        print(f" -> Terhubung ke {t} | Jarak: {j} km | Tarif: Rp {b}/km")
                else:
                    print(" Simpul terisolasi (tidak memiliki jalur distribusi).")
            else:
                print(" Kode simpul tidak terdaftar di dalam sistem.")
            input("\nTekan Enter...")

        elif pilihan == "2":
            print("\n--- PENELUSURAN AUDIT KONEKTIVITAS BFS ---")
            start = input("Masukkan Titik Awal Audit BFS: ").strip().upper()
            if start in graph.adj:
                urutan = graph.audit_konektivitas_bfs(start)
                print(f"Urutan Node Terjangkau: {' -> '.join(urutan)}")
            else:
                print(" Titik awal tidak valid.")
            input("\nTekan Enter...")

        elif pilihan == "3":
            print("\n--- PENELUSURAN AUDIT KONEKTIVITAS DFS ---")
            start = input("Masukkan Titik Awal Audit DFS: ").strip().upper()
            if start in graph.adj:
                urutan = graph.audit_konektivitas_dfs(start)
                print(f"Urutan Node Terjangkau: {' -> '.join(urutan)}")
            else:
                print(" Titik awal tidak valid.")
            input("\nTekan Enter...")

        elif pilihan == "0":
            break

if __name__ == "__main__":
    main()
