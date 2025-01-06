"""
 Day 5: Print Queue 
"""
with open("05/input.txt") as f:
    rules, sequences = f.read().strip().split("\n\n")

rules = [r for r in rules.split("\n")]
sequences = [[int(p.strip()) for p in s.split(",")] for s in sequences.split("\n")]

# Hashmap left right permission per page ----------
pages = set(p for r in rules for p in r.split("|"))
hmap = {
    int(p): {
        "r": [int(r[3:]) for r in rules if f"{p}|" in r],
        "l": [int(r[:2]) for r in rules if f"|{p}" in r]
    }
    for p in pages
}
# -------------------------------------------------
total = 0
invalids = list()  # Part 2
for s in sequences:
    valid = True
    for i, page in enumerate(s):
        if (l := s[:i]):
            for p in l:
                if p in hmap[page]["r"]:
                    valid = False
                    break
        
        if (r := s[i+1:]) and valid:
            for p in r:
                if p in hmap[page]["l"]:
                    valid = False
                    break
        if not valid:
            break

    # Get central
    if valid:
        total += s[int((len(s) - 1)/2)]
    else:
        invalids.append(s)

print("Total Sum:", total)

# Part 2
print("Invalids:", len(invalids))
total_invalids = 0
for s in invalids:
    hmap_c = {k: v for k, v in hmap.items() if k in s}
    
    # Remove pages
    hmap_c = {k: len([p for p in v["l"] if p in s]) for k, v in hmap_c.items()}
            
    # Create correct order
    correct_order = [(v, k) for k, v in hmap_c.items()]
    correct_order.sort(key=lambda x: x[0])
    s = list(map(lambda x: x[1], correct_order))

    total_invalids += s[int((len(s) - 1)/2)]

print("Total Sum Invalids:", total_invalids)
