def dijkstra_biaya_minimum(graph, start):
    """
    Mencari jalur termurah (bobot = jarak * biaya_km).
    Big-O: O(V^2 + E) tanpa min-heap library.
    """
    distances = {vertex: float('infinity') for vertex in graph.adj_list}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph.adj_list}
    unvisited = list(graph.adj_list.keys())

    while unvisited:
        # Cari node dengan jarak terkecil di unvisited
        current_node = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_node)

        if distances[current_node] == float('infinity'):
            break

        for edge in graph.adj_list.get(current_node, []):
            if isinstance(edge, dict):
                neighbor = edge["node"]
                bobot = edge["jarak"] * edge["biaya"]
                new_route_cost = distances[current_node] + bobot
                
                if new_route_cost < distances[neighbor]:
                    distances[neighbor] = new_route_cost
                    previous_nodes[neighbor] = current_node

    return distances, previous_nodes

def merge_sort_jalur(jalur_list):
    """
    Mengurutkan daftar jalur berdasarkan biaya.
    Big-O: O(n log n)
    """
    if len(jalur_list) > 1:
        mid = len(jalur_list) // 2
        left_half = jalur_list[:mid]
        right_half = jalur_list[mid:]

        merge_sort_jalur(left_half)
        merge_sort_jalur(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['biaya'] < right_half[j]['biaya']:
                jalur_list[k] = left_half[i]
                i += 1
            else:
                jalur_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            jalur_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            jalur_list[k] = right_half[j]
            j += 1
            k += 1
    return jalur_list