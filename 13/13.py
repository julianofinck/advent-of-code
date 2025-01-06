"""
 Day 13: Claw Contraption 
"""
with open("13/input.txt", "r") as f:
    data = f.read()

import re

# Any-Numbers
numb = ".(\d{1,6})"
regex = f"A: X{numb}, Y{numb}.*?X{numb}, Y{numb}.*?X{numb}, Y{numb}"
func = lambda ax, ay, bx, by, px, py:  {
    "game": lambda a, b: (
        a * int(ax) + b * int(bx),  
        a * int(ay) + b * int(by)
        ),
    "prize": (int(px), int(py))
    }
machines = {i: (func)(*machine) for i, machine in enumerate(re.findall(regex, data, re.DOTALL))}

total_tokens = 0
total_tokens_adjust_prize = 0
positives = 0
solvable = 0
for m in machines.values():
    prize = m["prize"]
    game_tokens = 999999

    # brute force - part1
    for a in range(101):
        for b in range(101):
            if m["game"](a, b) == prize:
                cost = 3*a + b
                if cost < game_tokens:
                    game_tokens = cost
    if game_tokens != 999999:
        total_tokens += game_tokens

    # mathematic solution - part2
    px, py = tuple(map(lambda x: (x + 10**13), prize))
    ax, ay = m["game"](1, 0)
    bx, by = m["game"](0, 1)
    lim = 0
    a = (py - by * px / bx) / (ay - by * ax / bx)
    if abs(a - round(a)) < 0.0001 and a > 0:
        a = round(a)
        b = int((px - a * ax) / bx)
        if b > 0:
            positives += 1
            if ax * a + bx * b == px:
                solvable += 1
                total_tokens_adjust_prize += 3 * a + b

print(positives, solvable)
print(total_tokens, f"{int(total_tokens_adjust_prize)}")
