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

def dfs(graph, start, goal):
    """
    Perform Depth-First Search to find the path from start to goal.
    Args:
    graph (dict): Adjacency list representation of the graph.
    start (str): The starting node.
    goal (str): The goal node.
    Returns:
    list: The path from start to goal if found, else None.
    """
    # Stack for DFS: each element is (current_node, path_so_far)
    stack = [(start, [start])]

    # Keep track of visited nodes to avoid cycles
    visited = set()

    while stack:
        # Pop the top of the stack
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        # If we reach the goal, return the path
        if current == goal:
            return path

        # Explore neighbors in reverse order to simulate stack behavior
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                # Add neighbor to the stack with updated path
                stack.append((neighbor, path + [neighbor]))

    # If goal is not found, return None
    return None

# Main function to run the DFS
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'

    print("Depth-First Search (DFS) Implementation")
    print("=======================================")
    print(f"Graph: {graph}")
    print(f"Starting Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print()

    path = dfs(graph, start_node, goal_node)

    if path:
        print("Path found:")
        print(" -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)