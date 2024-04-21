def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node_is_terminal(node):
        return static_evaluation(node)
    
    if maximizingPlayer:
        maxEva = float('-inf')
        for child in generate_children(node):
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva
    else:
        minEva = float('inf')
        for child in generate_children(node):
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva

def node_is_terminal(node):
    return node.depth == 0  # Assuming depth 0 indicates terminal node

def static_evaluation(node):
    return node.value

def generate_children(node):
    return node.children

class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = []

# Function to build the tree
def build_tree():
    # Hardcoded tree structure
    root = Node(3, 2)
    root.children = [Node(5, 1), Node(2, 1)]
    root.children[0].children = [Node(9, 0), Node(7, 0)]
    root.children[1].children = [Node(1, 0), Node(8, 0)]
    return root

if __name__ == "__main__":
    depth = 2  # Hardcoded depth
    root = build_tree()
    maximizingPlayer = True  # Assuming it's the maximizing player's turn
    result = minimax(root, depth, maximizingPlayer)
    print("Result of Minimax:", result)


# OUTPUT
# Result of Minimax: 7
