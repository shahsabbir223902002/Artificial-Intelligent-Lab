import random

# DFS function
def dfs(grid, x, y, goal_x, goal_y, visited, path):
    n = len(grid)
    # Check invalid position
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    # Check obstacle or already visited
    if grid[x][y] == 1 or (x, y) in visited:
        return False

    visited.add((x, y))
    path.append((x, y))

    # If goal found
    if (x, y) == (goal_x, goal_y):
        return True

    # Explore in 4 directions
    if (dfs(grid, x+1, y, goal_x, goal_y, visited, path) or
        dfs(grid, x-1, y, goal_x, goal_y, visited, path) or
        dfs(grid, x, y+1, goal_x, goal_y, visited, path) or
        dfs(grid, x, y-1, goal_x, goal_y, visited, path)):
        return True

    # Backtrack
    path.pop()
    return False


# Main program
n = int(input("Enter grid size (N): "))

# Create grid randomly (0 = free, 1 = obstacle)
grid = [[random.choice([0, 0, 1]) for _ in range(n)] for _ in range(n)]

print("\nGenerated Grid (1 = obstacle, 0 = free):")
for row in grid:
    print(row)

# Get start and goal positions
sx, sy = map(int, input("\nEnter start position (row col): ").split())
gx, gy = map(int, input("Enter goal position (row col): ").split())

# Make sure start and goal are free
grid[sx][sy] = 0
grid[gx][gy] = 0

visited = set()
path = []

# Run DFS
if dfs(grid, sx, sy, gx, gy, visited, path):
    print("\nPath found:")
    for p in path:
        print(p)
else:
    print("\nNo path found.")
