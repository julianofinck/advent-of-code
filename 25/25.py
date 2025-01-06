"""
 Day 25: Code Chronicle 
"""
from collections import defaultdict


def get_col_height(kl):
    col_heights = defaultdict(lambda: 0)
    for _, r in enumerate(kl):
        for i, v in enumerate(r):
            if v == "#":
                col_heights[i] += 1
    return [col_heights[i] for i in range(len(kl[0]))]


with open("25/input.txt", "r") as f: data=f.read().strip().split("\n\n")

keys = [get_col_height(k.split("\n")) for k in data if k[0] != "#"]
locks = [get_col_height(l.split("\n")) for l in data if l[0] == "#"]

print("Keys:",len(keys),"Locks:",len(locks))
lock_key_pairs = list()
for i, k in enumerate(keys):
    for j, l in enumerate(locks):
        for kh, lh in zip(k, l):
            if kh + lh > 7:
                break
        else:
            #if i not in lock_key_pairs:
            #    if j not in lock_key_pairs.values():
            #        lock_key_pairs[i] = j
            lock_key_pairs.append(tuple((i,j)))

print("Pairs:", len(lock_key_pairs))
