from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex in visited:
                continue
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbour for neighbour in self.graph[vertex] if neighbour not in visited)

if __name__ == "__main__":
    g = Graph()

    # Predefined edges
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.addEdge(u, v)

    # Predefined starting vertex
    start_vertex = 2

    print(f"Breadth First Traversal (starting from vertex {start_vertex}):")
    g.BFS(start_vertex)


# OUTPUT
# Breadth First Traversal (starting from vertex 2):
# 2 0 3 1 