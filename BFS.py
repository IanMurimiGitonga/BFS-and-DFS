from collections import deque

# Define the graph as an adjacency list
# This represents the nodes and their connections
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    """
    Perform Breadth-First Search to find the path from start to goal.

    Args:
    graph (dict): Adjacency list representation of the graph.
    start (str): The starting node.
    goal (str): The goal node.

    Returns:
    list: The path from start to goal if found, else None.
    """
    # Initialize the queue with the start node
    queue = deque([start])

    # Keep track of visited nodes to avoid cycles
    visited = set([start])

    # Dictionary to keep track of the parent of each node for path reconstruction
    parent = {start: None}

    # BFS traversal
    while queue:
        # Dequeue the current node
        current = queue.popleft()

        # If we reach the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current

    # If goal is not found, return None
    return None

# Main function to run the BFS
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'

    print("Breadth-First Search (BFS) Implementation")
    print("=========================================")
    print(f"Graph: {graph}")
    print(f"Starting Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print()

    path = bfs(graph, start_node, goal_node)

    if path:
        print("Path found:")
        print(" -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)