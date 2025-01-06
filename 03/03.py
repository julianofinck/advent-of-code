"""
 Day 3: Mull It Over 

 North Pole Toboggan Rental Shop
"""
import re
from functools import reduce

# Read
file = "03/input.txt"
with open(file, "r") as f:
    data = f.read()

# Remove newline
data = re.sub(r'\n', '', data)

# Part 1 - get summation of products
def total_sum_of_mul_xy(string: str) -> int:
    regex = "mul\((\d{1,3}),(\d{1,3})\)"
    total = reduce(
        lambda x, y: x + y, 
        [
            int(x) * int(y) 
            for x, y in re.findall(regex, string)
        ]
    )
    
    return total

total = total_sum_of_mul_xy(data)

print(f"Sum of multiplication:   {total}")

# Part 2
dos = list()

# Get all "do*dont"
regex = "do\(\).*?don't\(\)"
dos.extend(re.findall(regex, data))

# Get from start until do or don't
regex = "^.*?do\(\)"
start_till_do = re.findall(regex, data)
regex = "^.*?don't\(\)"
start_till_dont = re.findall(regex, data) 
if len(start_till_do) < len(start_till_dont):
    dos.extend(start_till_do)
else:
    dos.extend(start_till_dont)

# Get eventual final do
dont_till_end = re.findall(".*?\)\(t'nod", data[::-1])[0][::-1]
do_till_end = re.findall(".*?\)\(od", data[::-1])[0][::-1]
if len(do_till_end) < len(dont_till_end):
    dos.append(do_till_end)

# Print answer part 2
total = total_sum_of_mul_xy("".join(dos))
print(f"Sum of do-multiplication: {total}")

# Used to double-check because of my lack of experience in REGEX
"""
for i, do in enumerate(dos):
    print(f"{i:<4} {do.count('do()')}  " + str(do.count("don\'t()")))
"""
    
# Max-Anwenden wundervolle regex: re.findall("don't\\(\\)|do\\(\\)|mul\\( *[0-9]+, *[0-9]+\\)", data)
