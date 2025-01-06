"""
 Day 15: Warehouse Woes 
"""
def show(wh):
    i = int(max([k.real for k in wh]))
    j = int(max([k.imag for k in wh]))
    plot = [[3 for _ in range(i + 1)] for _ in range(j + 1)]
    for k, v in wh.items():
        plot[int(k.imag)][int(k.real)] = v
    for l in plot:
        print("".join(l))


def try_move_it(wh, r_pos, step):
    n_r_pos = r_pos + step
    match wh[n_r_pos]:
        case ".":
            wh[n_r_pos] = "@"
            wh[r_pos] = "."
            r_pos = n_r_pos
        case "O":
            i = 0
            while wh[n_r_pos + (i) * step] == "O":
                i += 1
            if wh[n_r_pos + (i) * step] == "#":
                pass
            elif wh[n_r_pos + (i) * step] == ".":
                wh[r_pos] = "."
                wh[n_r_pos] = "@"
                wh[n_r_pos + (i) * step] = "O"
                r_pos = n_r_pos
    return wh, r_pos


def try_move_it_part2(wh, r_pos, step):
    n_r_pos = r_pos + step
    match wh[n_r_pos]:
        case ".":
            wh[n_r_pos] = "@"
            wh[r_pos] = "."
            r_pos = n_r_pos
        case "[" | "]":
            # Horizontal
            if isinstance(step, int):
                i = 0
                while wh[n_r_pos + (i) * step] in ["[", "]"]:
                    i += 1
                if wh[n_r_pos + (i) * step] == ".":
                    for j in range(i, 0, -1):
                        wh[n_r_pos + (j) * step] = wh[n_r_pos + (j -1) * step]
                    wh[r_pos] = "."
                    wh[n_r_pos] = "@"
                    r_pos = n_r_pos
            
            # Vertical
            else:
                boxes = [n_r_pos]
                # Get the box
                if wh[n_r_pos] == "[":
                    boxes += [n_r_pos +1]
                else:
                    boxes += [n_r_pos -1]
                
                # Free space above it both?
                i = 0
                new_boxes = boxes.copy()
                while True:
                    i += 1
                    new_boxes = [b + step for b in new_boxes]
                    if any(wh[b] == "#" for b in new_boxes):
                        break
                    elif all(wh[b] == "." for b in new_boxes):
                        k_v = {k: wh[k] for k in boxes}
                        for p in boxes:
                            wh[p] = "."
                        for p in boxes:
                            wh[p + step] = k_v[p]
                        wh[r_pos] = "."
                        wh[n_r_pos] = "@"
                        r_pos = n_r_pos
                        break
                    else:
                        # Check if hit by new boxes
                        new_boxes = [b for b in new_boxes if wh[b] != "."]
                        for b in new_boxes:
                            if wh[b] == "[":
                                if b + 1 not in new_boxes:
                                    new_boxes.append(b+1)
                            elif wh[b] == "]":
                                if b - 1 not in new_boxes:
                                    new_boxes.append(b-1)
                            else:
                                new_boxes.remove(b)

                    # Add "k"
                    boxes += new_boxes

    return wh, r_pos

# Warehouse & Robot movements
wh_str, moves = open("15/input.txt", "r").read().strip().split("\n\n")
moves = moves.replace("\n", "")

duplication_rules = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
    "\n": "\n"
}
for pt, wh in enumerate([wh_str, "".join([duplication_rules[s] for s in wh_str])]):
    wh = {x + (y) * 1j : v for y, l, in enumerate(wh.split("\n")) for x, v in enumerate(l)}

    r_pos = [pos for pos, v in wh.items() if v == "@"][0]

    if pt == 0:
        move_it = try_move_it
    else:
        move_it = try_move_it_part2
    
    for mv in moves:
        wh, r_pos = move_it(wh, r_pos, {"<": -1, ">": +1, "^": -1j, "v": +1j}[mv])

    # Lantern fish Goods Positioning System
    gps = sum([int(100 * p.imag + p.real) for p, v in wh.items() if v in "O["])
    print("GPS:", gps)

