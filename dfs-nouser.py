from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

if __name__ == "__main__":
    g = Graph()

    # Predefined edges
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.addEdge(u, v)

    # Predefined starting vertex
    start_vertex = 2

    print(f"Depth First Traversal (starting from vertex {start_vertex}):")
    g.DFS(start_vertex)


# OUTPUT
# Depth First Traversal (starting from vertex 2):
# 2 0 1 3 