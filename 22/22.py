"""
 Day 22: Monkey Market 
"""
from collections import defaultdict
with open("22/input.txt", "r") as f: secrets = [int(l.strip()) for l in f.read().strip().split("\n")]

def next_secret_numbers(n, times):
    ones_digits = tuple()    
    for _ in range(times):
        v1 = ((n * 64) ^ n) % 16777216

        v2 = (int(v1 / 32) ^ v1) % 16777216

        n = ((v2 * 2048) ^ v2) % 16777216 

        ones_digits += (n % 10,)
    
    changes = [ones_digits[i] - ones_digits[i -1] for i in range(1, len(ones_digits))]

    changes_seq4 = defaultdict(lambda: 0)
    for i in range(4, len(ones_digits)):
        k = tuple(changes[i-4:i])
        # Only first occurrence matters
        if k not in changes_seq4:
            changes_seq4[k] = ones_digits[i]

    return n, changes_seq4

tot = 0
changes_i = dict()
for i, s in enumerate(secrets):
    s2000th, changes = next_secret_numbers(s, 2000)
    changes_i[i] = changes
    tot += s2000th
print("Sum", tot)

# Get all
seq4s = {seq4 for v in changes_i.values() for seq4 in v}
max_profit = 0
golden_sequence = None
for i, seq4 in enumerate(seq4s):
    profit = 0
    for sequences in changes_i.values():
        profit += sequences[seq4]
    if profit > max_profit:
        max_profit = profit
        golden_sequence = seq4
print(f"Sequence '{golden_sequence}' yields the max profit: '{max_profit}'")
