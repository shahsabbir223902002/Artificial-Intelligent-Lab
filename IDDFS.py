def iddfs_maze(grid, start, target, max_depth):
    rows, cols = len(grid), len(grid[0])

    def dls(r, c, tr, tc, depth, visited, path):
        if (r, c) == (tr, tc):
            path.append((r, c))
            return True

        if depth == 0:
            return False

        visited.add((r, c))
        path.append((r, c))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and
                (nr, nc) not in visited):
                if dls(nr, nc, tr, tc, depth - 1, visited, path):
                    return True

        path.pop()
        visited.remove((r, c))
        return False

    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if dls(start[0], start[1], target[0], target[1],
               depth, visited, path):
            return True, depth, path

    return False, max_depth, []
grid1 = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1]
]

start1 = (0, 0)
target1 = (2, 3)
max_depth1 = 6

found, depth, path = iddfs_maze(grid1, start1, target1, max_depth1)

if found:
    print(f"Path found at depth {depth} using IDDFS")
    print("Traversal Order:", path)
else:
    print(f"Path not found at max depth {depth} using IDDFS")
grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

start2 = (0, 0)
target2 = (2, 2)
max_depth2 = 6

found, depth, path = iddfs_maze(grid2, start2, target2, max_depth2)

if found:
    print(f"Path found at depth {depth} using IDDFS")
    print("Traversal Order:", path)
else:
    print(f"Path not found at max depth {depth} using IDDFS")
