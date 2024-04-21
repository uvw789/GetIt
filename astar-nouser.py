import heapq

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def A_Star(start, goal, h, graph):
    openSet = [(h(start), start)]
    cameFrom = {}
    gScore = {node: float('inf') for node in graph}
    gScore[start] = 0
    fScore = {node: float('inf') for node in graph}
    fScore[start] = h(start)
    
    while openSet:
        _, current = heapq.heappop(openSet)
        if current == goal:
            return reconstruct_path(cameFrom, current)
        
        for neighbor in graph[current]:
            tentative_gScore = gScore[current] + graph[current][neighbor]
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor)
                heapq.heappush(openSet, (fScore[neighbor], neighbor))
    
    return "failure"

def main():
    graph = {
        'A': {'B': 7, 'C': 3},
        'B': {'A': 7, 'C': 1, 'D': 2},
        'C': {'A': 3, 'B': 1, 'D': 2},
        'D': {'B': 2, 'C': 2}
    }

    start = 'A'
    goal = 'D'

    heuristic_values = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

    def heuristic(node):
        return heuristic_values[node]

    path = A_Star(start, goal, heuristic, graph)
    print("Path:", path)

if __name__ == "__main__":
    main()


# OUTPUT
# Path: ['A', 'C', 'D']