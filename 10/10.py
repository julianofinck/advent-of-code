"""
 Day 10: Hoof It 
"""
with open("10/input.txt", "r") as f:
    topography = {i + 1 + (j + 1) * 1j : int(v) for j, l in enumerate(f.read().strip().split("\n")) for i, v in enumerate(l)}


def find_peaks(pos):
    result = list()
    for p in pos:
        if topography[p] == 9:
            result.append(p)
        else:
            # Walk
            for i in range(4):
                next_p = p + 1j ** i
                if next_p in topography:
                    if topography[next_p] - topography[p] == 1:
                        r = find_peaks([next_p])
                        if r:
                            result.extend(r)
                    
        return result


trail_heads_unique = list()
trail_heads = list()
for trail_head in [g for g, h in topography.items() if h == 0]:
    r = find_peaks([trail_head])

    # Part 1
    trail_heads_unique.append(set(r))

    # Part 2
    trail_heads.append(r)


print("Part 1: Trail head Score:", sum([len(s) for s in trail_heads_unique]))
print("Part 2: Trail head Rating:", sum([len(s) for s in trail_heads]))
