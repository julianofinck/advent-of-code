"""
 Day 19: Linen Layout 

For part 1, I construct the design by adding each possible towel 
and checking if the target_design startswith it. Then, add to queue.
It finishes one the constructed design and target_design match or the queue is empty

For part 2, I expanded the queue to work with tuples. It was not efficient at all.
Someone in internet used memoization, which was way quicker.
The logic behind it is that once you know a part of a design has N ways
to be made, a recursive function with memoization will skip calculating
the possibilities again.
"""
from functools import cache
with open("19/input.txt", "r") as f:
    data = f.read().strip()

towels, desired_designs = data.split("\n\n")
towels = tuple(towels.split(", "))
desired_designs = desired_designs.split("\n")

@cache
def possible(design, towels):
    if not design:
        # Design is empty
        return 1
    # If design starts with towel, 
    #    search further on the rest of
    #    the design using towels.
    # If it eventually finds a way, it returns 1
    return sum(
        possible(design[len(towel):], towels)
        for towel in towels if design.startswith(towel)
    )

possible_designs = 0
possibilities = 0
for design in desired_designs:
    numb_possibilities = possible(design, towels)
    if numb_possibilities:
        possible_designs += 1
        possibilities += numb_possibilities


print("Possible designs:", possible_designs)
print("Possibilities:", possibilities)