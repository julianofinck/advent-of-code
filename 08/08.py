with open("08/input.txt", "r") as f:
    grid = {i + 1 + (j + 1) * 1j : v for j, l in enumerate(f.read().strip().split("\n")) for i, v in enumerate(l)}

part2 = True
antinodes = set()
for antenna in [a for a in set(grid.values()) if a != "."]:
    a_poss = [pos for pos, v in grid.items() if v == antenna]
    if len(a_poss) > 1:
        for i, pos in enumerate(a_poss):
            if part2:
                antinodes.add(pos)
            for contra_pos in a_poss[:i] + a_poss[i+1:]:
                dif = contra_pos - pos

                # Part 1
                for antinode in (
                    contra_pos + dif, 
                    pos - dif):
                    if antinode in grid:
                        antinodes.add(antinode)
                
                # Part 2 - Let it ressonate
                if part2:
                    j = 2
                    while (antinode := contra_pos + j * dif) in grid:
                        if antinode != antenna:
                            antinodes.add(antinode)
                        j += 1
                    
                    j = 2
                    while (antinode := pos - j * dif ) in grid:
                        if antinode != antenna:
                            antinodes.add(antinode)
                        j += 1

print("Nº Antinodes:", len(antinodes))
