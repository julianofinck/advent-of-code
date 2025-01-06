"""
 Day 20: Race Condition 
"""
from collections import deque
from itertools import combinations
with open("20/input.txt", "r") as f:
    grid = {i+j*1j: v for j, r in enumerate(f.read().strip().split("\n")) 
                      for i, v in enumerate(r) if v != "#"}

start, = (k for k, v in grid.items() if v == "S")

dist = {start: 0}
path = [start]
for pos in path:
    for next_pos in (pos+1, pos-1, pos+1j, pos-1j):
        if next_pos in grid and next_pos not in path:
            dist[next_pos] = dist[pos] + 1
            path.append(next_pos)

part1 = part2 = 0

# This approach only worked because the exercise wants to know
#  the number of cheats that spare more than 100 and there is
#  no straight line in the maze that sums up 100 forward moves
for (p1, i1), (p2, i2) in combinations(dist.items(), 2):
    dist = abs((p2-p1).real) + abs((p2-p1).imag)
    if dist == 2 and i2-i1-dist >= 100:
        part1 += 1
    if dist < 21 and i2-i1-dist >= 100:
        part2 += 1
# 1441 1021490
print(part1, part2)
