from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start, []))  # Tuple: (priority, node, path)
    
    while not priority_queue.empty():
        _, current_node, path = priority_queue.get()
        visited.add(current_node)
        
        if current_node == goal:
            return True, path  # Return path if goal is reached
        
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [(current_node, neighbor, cost)]
                priority_queue.put((heuristic[neighbor], neighbor, new_path))
    
    return False, []  # No path exists

def input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        start, end, cost = input("Enter edges in the format 'node1 node2 heuristic_value: ").split()
        cost = int(cost)
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append((end, cost))
        graph[end].append((start, cost))  # Assuming undirected graph
    return graph

def input_heuristic(graph):
    heuristic = {}
    for node in graph.keys():
        heuristic[node] = int(input(f"Enter heuristic value for node {node}: "))
    return heuristic

def print_path(path):
    print("Path from start to goal:")
    for edge in path:
        print(f"{edge[0]} -> {edge[1]} (Cost: {edge[2]})")

graph = input_graph()
heuristic_values = input_heuristic(graph)
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
exists, path = greedy_best_first_search(graph, start, goal, heuristic_values)
if exists:
    print(f"Path exists from {start} to {goal}")
    print_path(path)
else:
    print(f"No path exists from {start} to {goal}")


# OUTPUT
# Enter the number of edges: 5
# Enter edges in the format 'node1 node2 heuristic_value: A B 7
# Enter edges in the format 'node1 node2 heuristic_value: A C 3
# Enter edges in the format 'node1 node2 heuristic_value: B D 2
# Enter edges in the format 'node1 node2 heuristic_value: C B 1
# Enter edges in the format 'node1 node2 heuristic_value: C D 2
# Enter heuristic value for node A: 3
# Enter heuristic value for node B: 2
# Enter heuristic value for node C: 1
# Enter heuristic value for node D: 0
# Enter the start node: A
# Enter the goal node: D
# Path exists from A to D
# Path from start to goal:
# A -> C (Cost: 3)
# C -> D (Cost: 2)