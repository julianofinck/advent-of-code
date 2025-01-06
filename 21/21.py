"""
 Day 21: Keypad Conundrum 

Buttons have precedence "<", then up/down, then ">"
Repeatedly using directional-directional robots, lead to very long lists.
These lists have repeated patterns and are better stored in a dict:
 - "<A" starting from A will always be "<A>A"
"""
with open("21/input.txt", "r") as f:
    buttons = f.read().strip().split("\n")

directional="""
    #^A
    <v>
"""

numeric="""
    789
    456
    123
    #0A
"""

dir_grid = {i+j*1j:v for j,r in enumerate(directional.strip().split("\n")) for i,v in enumerate(r.strip()) if v != "#"}
num_grid = {i+j*1j:v for j,r in enumerate(numeric.strip().split("\n")) for i,v in enumerate(r.strip()) if v != "#"}

def get_presses_(n, dx, dy, numerical=False):
    if numerical:
        grid = num_grid
    else:
        grid = dir_grid
    stepx = {True: 1, False: -1}[dx >= 0]
    stepy = {True: 1j, False: -1j}[dy >= 0]
    presses = list()
    inverse = False
    # Priority: <, ^, v, >
    # If priority leads out of the keypad, inverse it at the end.
    if dx < 0:
        for _ in range(abs(dx)):
            n += stepx
            if n not in grid:
                inverse = True
            presses.append(stepx)
    for _ in range(abs(dy)):
        n += stepy
        if n not in grid:
            inverse = True
        presses.append(stepy)
    if dx > 0:
        for _ in range(abs(dx)):
            n += stepx
            if n not in grid:
                inverse = True
            presses.append(stepx)

    # Translate to directions
    presses = [{1: ">", -1: "<", -1j: "^", 1j: "v"}[p] for p in presses]
    
    if not inverse:
        return tuple(presses)
    else:
        return tuple(presses[::-1])

def get_presses(s, desired_sequence, numerical=False):
    grid = num_grid if numerical else dir_grid
    presses = dict()
    for p, c in desired_sequence.items():  # Here is the problem, this desired_sequence grows large pretty quickly, This program repeats itself, make a dict
        for b in p:
            dest, = (pos for pos, v in grid.items() if v == b)
            dx, dy = int((dest - s).real), int((dest - s).imag)
            k = "".join(get_presses_(s, dx, dy, numerical) + ("A",))
            if k in presses:
                presses[k] += c
            else:
                presses[k] = c
            s = dest

    return presses

n, d = 2+3j, 2
for dir_keypads_robot in (2, 25):
    complexities = list()
    for button in buttons:

        # From Numerical -> Directional
        presses = get_presses(n, {k: list(button).count(k) for k in button}, numerical=True)

        # Direction -> Directional
        for _ in range(dir_keypads_robot):
            presses = get_presses(d, presses)
        
        numb_presses = sum(len(k)*c for k,c in presses.items())
        print(f"Button '{button}' has {numb_presses} presses")
        complexities.append(numb_presses * int(button[:-1]))    

    print(sum(complexities))
# 171596
# 209268004868246