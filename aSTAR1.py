import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, target):
    rows, cols = len(grid), len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        r, c = current
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g_cost[current] + 1

                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + manhattan(neighbor, target)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None


def main():
    with open("input.txt", "r") as f:
        data = f.read().strip().split()

    idx = 0
    R, C = int(data[idx]), int(data[idx+1])
    idx += 2

    grid = []
    for _ in range(R):
        row = list(map(int, data[idx:idx+C]))
        grid.append(row)
        idx += C

    start = (int(data[idx]), int(data[idx+1]))
    idx += 2
    target = (int(data[idx]), int(data[idx+1]))

    path = astar(grid, start, target)

    if path:
        print(f"Path found with cost {len(path)-1} using A*")
        print("Shortest Path:", path)
    else:
        print("Path not found using A*")


if __name__ == "__main__":
    main()
