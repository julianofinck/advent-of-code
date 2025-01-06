"""
 Day 12: Garden Groups 
"""
with open("12/input.txt", "r") as f:
    garden = {i + 1 + (j + 1) * 1j : v for j, l in enumerate(f.read().strip().split("\n")) for i, v in enumerate(l)}


def mark_region(garden, p, f, region):
    if not isinstance(f, tuple):
        garden[p] = tuple([f, region])

        for i in range(4):
            n_p = p + 1j ** i
            if n_p in garden:
                if garden[n_p] == f:
                    mark_region(garden, n_p, f, region)


def get_fences(region):
    fences = list()
    for k in region:
        for i in range(4):
            n_k = k + 1j ** i
            if n_k not in region:
                if (k - n_k).real == 0:
                    fences.append((n_k, "-", k))
                else:
                    fences.append((n_k, "|", k))

    return fences


def get_sides(f_list, step, fences):
    if step == -1:
        orientation = "-"
    else:
        orientation = "|"
    f, _, f_origin = f_list[-1]
    for i in range(2):
        n_f = f + (step) * (-1) ** i
        n_f_origin = f_origin + (step) * (-1) ** i
        n_f = (n_f, orientation, n_f_origin)
        if n_f in fences and n_f not in f_list:
            f_list.extend(get_sides(f_list + [n_f], step, fences))
    
    return f_list

# Get regions
region = 0
for plot, flower in garden.items():
    if isinstance(flower, str):
        region += 1
        mark_region(garden, plot, flower, region)

full_price = 0
discounted_price = 0
for region_label in set(garden.values()):
    region = {k: v for k, v in garden.items() if v == region_label}
    area = len(region)
    fences = get_fences(region)
    perimeter = len(fences)
    full_price += area * perimeter

    # Part 2
    num_side = 0
    sides = list()
        
    while fences:
        fence = fences[0]
        side = []
        f, orientation, origin = fence

        match orientation:
            case "|":
                side.extend(get_sides([fence], -1j, fences))
            case "-":
                side.extend(get_sides([fence], -1, fences))

        if not side:
            side = [fence]

        side = set(side)

        sides.append(side)
        for s in side:
            fences.remove(s)
        
    discounted_price += area * len(sides)

print(full_price, discounted_price)
