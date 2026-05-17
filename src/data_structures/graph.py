# Isi dari src/data_structures/graph.py
class Graph:
    def __init__(self):
        # Pastikan namanya 'adj_list' dan menggunakan dictionary {}
        self.adj_list = {} 

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1) # Hapus baris ini jika Directed Graph

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
