import random
from collections import deque


# Function to generate grid with random obstacles
def generate_grid(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    num_obstacles = n  # number of obstacles (you can change it)
    for _ in range(num_obstacles):
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        grid[x][y] = 1  # 1 means obstacle
    return grid


# Function to print grid
def print_grid(grid):
    for row in grid:
        print(row)


# BFS traversal
def bfs(grid, start, goal):
    n = len(grid)
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([(start, [])])  # (current_position, path)
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            print("\nPath Found!")
            for move in path:
                print(f"Moving {move[0]} -> {move[1]}")
            return True

        for dx, dy, move_name in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(move_name, (nx, ny))]))

    print("\nNo path found!")
    return False


# ---- MAIN PROGRAM ----
n = int(input("Enter grid size N: "))
grid = generate_grid(n)

print("\nGenerated Grid (0 = free, 1 = obstacle):")
print_grid(grid)

start_x, start_y = map(int, input("\nEnter start position (x y): ").split())
goal_x, goal_y = map(int, input("Enter goal position (x y): ").split())

# Ensure start and goal are not obstacles
grid[start_x][start_y] = 0
grid[goal_x][goal_y] = 0

print("\nStarting BFS traversal...\n")
bfs(grid, (start_x, start_y), (goal_x, goal_y))
