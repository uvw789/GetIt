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
    graph = {}

    while True:
        edge = input("Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): ").split()
        if edge[0] == 'done':
            break
        node1, node2, weight = edge
        weight = int(weight)
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    heuristic_values = {}
    for node in graph:
        heuristic_values[node] = int(input(f"Enter heuristic value for node {node}: "))

    def heuristic(node):
        return heuristic_values[node]

    path = A_Star(start, goal, heuristic, graph)
    print("Path:", path)

if __name__ == "__main__":
    main()

# OUTPUT
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): A B 7
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): A C 3
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): B A 7
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): B C 1
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): B D 2
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): C A 3
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): C B 1
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): C D 2
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): D B 2     
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): D C 2
# Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): done
# Enter the start node: A
# Enter the goal node: D
# Enter heuristic value for node A: 3
# Enter heuristic value for node B: 2
# Enter heuristic value for node C: 1
# Enter heuristic value for node D: 0
# Path: ['A', 'C', 'D']