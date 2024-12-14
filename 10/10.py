with open("10/input.txt", "r") as f:
    grid = {i + 1 + (j + 1) * 1j : int(v) for j, l in enumerate(f.read().strip().split("\n")) for i, v in enumerate(l)}


def up_to_9(pos):
    result = list()
    for p in pos:
        if grid[p] == 9:
            return p
        else:
            # Walk
            for i in range(4):
                next_p = p + 1j ** i
                if next_p in grid:
                    if grid[next_p] - grid[p] == 1:
                        r = up_to_9([next_p])
                        if r:
                            result.append(r)
                    
            return result

def flatten(results):
    """Flatten nested lists into a single list."""
    if not isinstance(results, list):
        return [results]  # Base case: not a list, return as a list
    flat_list = []
    for item in results:
        flat_list.extend(flatten(item))  # Recursively flatten each item
    return flat_list

trailheads_9_unique = list()
trailheads_9 = list()
for trailhead in [g for g, h in grid.items() if h == 0]:
    r = flatten(up_to_9([trailhead]))
    # Part 1
    trailheads_9_unique.append(set(r))

    # Part 2
    trailheads_9.append(r)


print("Part 1: Trailhead Score:", sum([len(s) for s in trailheads_9_unique]))
print("Part 2: Trailhead Rating:", sum([len(s) for s in trailheads_9]))
