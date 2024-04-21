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

    # Input edges
    print("Enter edges (u v), or type 'done' to finish:")
    for line in iter(input, 'done'):
        u, v = map(int, line.split())
        g.addEdge(u, v)

    # Input starting vertex
    start_vertex = int(input("Enter the starting vertex for BFS traversal: "))

    print(f"Breadth First Traversal (starting from vertex {start_vertex}):")
    g.BFS(start_vertex)


# OUTPUT
# Enter edges (u v), or type 'done' to finish:
# 0 1
# 0 2
# 1 2
# 2 0
# 2 3
# 3 3
# done
# Enter the starting vertex for BFS traversal: 2
# Breadth First Traversal (starting from vertex 2):
# 2 0 3 1 