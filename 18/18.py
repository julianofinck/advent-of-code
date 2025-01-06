"""
 Day 18: RAM Run 
"""
from collections import deque

with open("18/input.txt", "r") as f:
    data = f.read().strip()

bytes2fall = [(lambda x, y: int(x) + int(y)*1j)(*b.split(",")) for b in data.split("\n")]

# Initialize 2D grid 0-70 x 0-70
grid = {x + y * 1j: "." for x in range(71) for y in range(71)}

# Corrupt until 1024 bytes have fallen
for b in bytes2fall[:1024]:
    grid[b] = "#"

# BFS
def bfs():
    start = 0
    dest = 70 + 70j
    queue = deque([(start, [start])])
    seen = set()
    paths = list()
    directions = [1, -1, 1j, -1j]
    while queue:
        pos, path = queue.popleft()

        if pos == dest:
            paths = path
            continue

        for d in directions:
            next_pos = pos + d
            if next_pos not in grid:
                continue
            if (next_pos, d) not in seen:
                seen.add((next_pos, d))
                if grid[next_pos] == ".":
                    queue.append((next_pos, path + [next_pos]))
    
    return paths

path = bfs()
print(f"Minimum steps: {len(path)}")

# Part 2
for i, b in enumerate(bytes2fall[1024:]):
    grid[b] = "#"
    if b in path:
        path = bfs()
        print(i, len(path))
    if not path:
        print("Blocked path:", b)
        break
