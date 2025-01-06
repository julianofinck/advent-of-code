"""
 Day 16: Reindeer Maze 
"""
from collections import deque
import time


def get_score(moves):
    return sum({"l": 1000, "r": 1000, "f": 1}[o] for o in moves)


def find_all_paths_bfs(start, dest):
    # Queue for BFS: stores (current position, heading, moves list)
    queue = deque([(start, 1, [])])
    seen = dict()
    paths = dict()
    min_score = 10**8

    while queue:
        pos, heading, moves = queue.popleft()

        if pos == dest:
            # If destination is reached, store the moves as a path
            moves_ = "".join(moves)
            score_ = get_score(moves_)
            if score < min_score:
                min_score = score_
            paths[moves_] = score_ 
            continue

        # Find possible paths
        for i in range(4):
            next_pos = pos + 1j ** i
            # Calculate the move
            move = {1: "f", -1: "rrf", 1j: "rf", -1j: "lf"}[(next_pos - pos) / heading]

            score = get_score("".join(moves + [move]))
            if grid.get(next_pos, "#") == "#" or score > min_score or seen.get((next_pos, next_pos - pos), 10**8) < score:
                continue

            seen[(next_pos, next_pos - pos)] = score
            
            # Add the new position, heading, updated moves, and seen to the queue
            queue.append((next_pos, next_pos - pos, moves + [move]))

    return paths


with open("16/input.txt", "r") as f: data=f.read() 
grid = {i+j*1j: v for j, r in enumerate(data.split("\n")) for i, v in enumerate(r)}

# BFS - Find all paths thereto
pos, = (p for p in grid if grid[p] == "S")
DESTINATION, = (p for p in grid if grid[p] == "E")
heading = 1
moves = [""]
seen = set([pos])
ti = time.perf_counter()
paths = find_all_paths_bfs(pos, DESTINATION)
tf = time.perf_counter()
print(f"Runtime (s): {tf-ti}")  # 2941s wout "ignore node if score is already above a winning path", 2000s w it

# Sort dict
min_score = min([v for v in paths.values()])
print("Best path:", min_score)  # 134588

# Part 2
paths = {k: v for k, v in paths.items() if v == min_score}
seen = set()
for path in paths:
    pos, = (p for p in grid if grid[p] == "S")
    seen.add(pos)
    heading = 1
    for mv in path:
        match mv:
            case "f":
                pos += heading
            case "r":
                heading *= 1j
            case "l":
                heading *= -1j
        seen.add(pos)

print("Part 2 - tiles in best paths:", len(seen))  # 631