"""
 Day 6: Guard Gallivant 
"""
with open("06/input.txt", "r") as f:
    grid = {j + i * 1j: e for i, l in enumerate(f.read().strip().split("\n")) for j, e in enumerate(l)}

step = {1j: -1j, -1: 1, -1j: 1j,  1: -1}
pos_i = [k for k, v in grid.items() if v == '^'][0]
pos = pos_i

# Part 1
d = 1j
visited = set([pos])

while True:
    last_pos = pos
    pos += step[d]

    if pos not in grid:
        break
    elif grid[pos] != "#":
        visited.add(pos)
    else:
        pos = last_pos
        d *= 1j
print("Nº pos the guard visits:", len(visited))

# Part 2
def is_loop(pos, d):
    seen = set()
    while True:
        if (pos, d) in seen:
            return True
        # Record pos + direction
        seen.add((pos, d))
        
        # Try to step
        next_pos_ = pos + step[d]

        # Check if goes overboard
        if next_pos_ not in grid:
            return False
        elif grid[next_pos_] == "#":
            d *= 1j
        else:
            pos = next_pos_

pos = pos_i
d = 1j
loops = 0
visited = set()
obstacles = set()
while True:
    visited.add((pos, d))

    # Try to step
    next_pos = pos + step[d]
    if next_pos not in grid:
        break
    elif grid[next_pos] == "#":
        d *= 1j
    else:
        if next_pos not in obstacles:
            grid[next_pos] = "#"
            if next_pos in ((104 + 99j), 3): #, (112 + 99j), (46, 86j)):
                pass #print(1)
            if is_loop(pos_i, 1j):
                obstacles.add(next_pos)
                loops += 1
            grid[next_pos] = "."
        pos = next_pos

with open("obs.txt", "r") as f:
    obs = f.readlines()
    obs = [tuple(int(n) for n in l.strip().replace(" ", "")[1:-1].split(",")) for l in obs]

obs1 = [(int(o.real), int(o.imag)) for o in list(obstacles)]
sobrando = [o for o in obs1 if o not in obs]
print("Loops Found:", len(obstacles))  # 1602
