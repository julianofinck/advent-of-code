"""
 Day 14: Restroom Redoubt 
"""
with open("14/input.txt", "r") as f:
    data = f.read().strip()

from functools import reduce
import re
space = (101, 103)
#space = (11, 7)
sx, sy = space
mid_x, mid_y = sx // 2, sy // 2
regex = "p=(.*?\d{1,3}),(.*?\d{1,3}) v=(.*?\d{1,3}),(.*?\d{1,3})"
robot = {
    i: {
        "pos": int(r[0]) + (int(r[1])) * 1j, 
        "vel": int(r[2]) + (int(r[3])) * 1j
        } 
    for i, r in enumerate(re.findall(regex, data))
    }

def wait(seconds, robot) -> (dict[int: dict], list[int]):
    quadrants = [0, 0, 0, 0]
    for i, r in robot.items():
        new_pos = r["pos"] + r["vel"] * seconds
        new_pos = new_pos.real % space[0] + (new_pos.imag % space[1]) * 1j
        robot[i]["pos"] = new_pos
        x, y = new_pos.real, new_pos.imag
        if x < mid_x:
            if y < mid_y:
                quadrants[0] += 1
            elif y > mid_y:
                quadrants[2] += 1
        elif x > mid_x:
            if y < mid_y:
                quadrants[1] += 1
            elif y > mid_y:
                quadrants[3] += 1
    return robot, quadrants

_, quadrants = wait(7847, robot)
print(reduce(lambda x, y: x*y, quadrants))

import matplotlib.pyplot as plt

def show_matplotlib(xys, xf, yf, xi=0, yi=0, save_as_png=True):
    # Create a new figure
    fig, ax = plt.subplots()

    # Set the axes limits
    ax.set_xlim(xi, xf)
    ax.set_ylim(yi, yf)

    # Plot the points as black dots
    x_vals, y_vals = zip(*xys)  # Unzip x and y values
    ax.scatter(x_vals, y_vals, color='black', s=1)  # s=1 makes dots smaller
    
    # If requested, save the plot as a PNG file
    if save_as_png:
        plt.savefig(f"14/img/{safety_factor}_{eta}.png", format="png")


eta = 0
for s in range(10000):
    robot, quadrants = wait(1, robot)
    xys = [(int(r["pos"].real), int(r["pos"].imag)) for r in robot.values()]
    safety_factor = reduce(lambda x, y: x*y, quadrants)

    if safety_factor < 100_000_000:
        print(safety_factor)
        show_matplotlib(xys, sx, sy)
    eta += 1

