"""
 Day 9: Disk Fragmenter 
"""
import time

# Day 09: Disk Fragmenter
with open("09/input.txt", "r") as f:
    disk = f.read().strip()

# Build string "block" / "free-space", putting IDs where block starting from 0 and "." where free
decoded = list()
for i, e in enumerate(disk):
    e = int(e)
    if i % 2 == 0:
        decoded += e * [int(i / 2)]
    else:
        decoded += e * ["."] 
decoded2 = decoded.copy()

# FILE SYSTEM FRAGMENTATION
# Part 1
# From right to left, fill "." with numbers

fspaces = decoded.count(".")
len_decoded = len(decoded)
mustblock = len_decoded - fspaces
i = 0
r = len_decoded - 1
ti = time.perf_counter()
while True:
    if decoded[i] == ".":
        while decoded[r] == ".":
            r -= 1
        
        decoded[i] = decoded[r]
        decoded[r] = "."

    i += 1
    if i >= mustblock:
        break
tf = time.perf_counter()
print("Part 1 took", tf-ti, "s")

# Part 2
r = len(decoded2) - 1
file = decoded2[r]
ti = time.perf_counter()
while (r > 0):
    if decoded2[r] != file:
        r -= 1
    else:
        # Get file size
        file = decoded2[r]
        size = 0
        while decoded2[r] == file:
            size += 1
            r -= 1
        file -= 1

        # Find leftmost free space
        i = decoded2.index(".")
        free_size = 0
        while (free_size < size) and (i <= r):
            if decoded2[i] == ".":
                free_size += 1
            else:
                free_size = 0
            i += 1

        # Substitute
        if size == free_size:
            for j in range(size):
                decoded2[i - size + j] = decoded2[r + 1 + j]
                decoded2[r + 1 + j] = "."
tf = time.perf_counter()
print("Part 2 took", tf-ti, "s")            


# Run checksum
checksum = sum([i * int(e) for i, e in enumerate(decoded) if e != "."])   # 6414919955263 too low
print("Part1 Checksum:", checksum)

checksum = sum([i * e for i, e in enumerate(decoded2) if e != "."])   # 6414919955263 too low
print("Part2 Checksum:", checksum)

print("Done!")
