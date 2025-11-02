from collections import defaultdict

# Depth-Limited Search (DFS with depth limit)
def dls(graph, node, goal, limit, path, visited):
    visited.add(node)
    path.append(node)

    # Goal found
    if node == goal:
        return True

    # Stop if depth limit reached
    if limit <= 0:
        path.pop()
        return False

    # Explore neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, limit - 1, path, visited):
                return True

    # Backtrack
    path.pop()
    return False


# Iterative Deepening DFS
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if dls(graph, start, goal, depth, path, visited):
            return path  # path found
    return None


# Main Program
graph = defaultdict(list)

# Input number of edges
n = int(input("Enter number of edges: "))

# Take dynamic graph input
print("Enter edges (u v):")
for _ in range(n):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # if undirected

print("\nGraph:", dict(graph))

# Take source and goal
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

max_depth = int(input("Enter maximum depth limit: "))

# Run IDDFS
path = iddfs(graph, start, goal, max_depth)

# Output result
if path:
    print("\nPath found using IDDFS:")
    print(" -> ".join(path))
else:
    print("\nNo path found within the given depth limit.")
