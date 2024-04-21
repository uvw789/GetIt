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

def predefined_graph():
    return {
        'A': [('B', 7), ('C', 3)],
        'B': [('A', 7), ('C', 1), ('D', 2)],
        'C': [('A', 3), ('B', 1), ('D', 2)],
        'D': [('B', 2), ('C', 2)]
    }

def predefined_heuristic():
    return {'A': 3, 'B': 2, 'C': 1, 'D': 0}

def print_path(path):
    print("Path from start to goal:")
    for edge in path:
        print(f"{edge[0]} -> {edge[1]} (Cost: {edge[2]})")

graph = predefined_graph()
heuristic_values = predefined_heuristic()
start = 'A'
goal = 'D'
exists, path = greedy_best_first_search(graph, start, goal, heuristic_values)
if exists:
    print(f"Path exists from {start} to {goal}")
    print_path(path)
else:
    print(f"No path exists from {start} to {goal}")

# OUTPUT
# Path exists from A to D
# Path from start to goal:
# A -> C (Cost: 3)
# C -> D (Cost: 2)