"""
 Day 17: Chronospatial Computer 
"""
with open("17/input.txt", "r") as f: data = f.read()
register, program = data.split("\n\n")
a, b, c = [int(l.split(" ")[-1]) for l in register.strip().split("\n")]
program = list(map(int, program.split(": ")[-1].split(",")))


def computer(a: int, b: int = 0, c: int= 0):
    ip = 0
    output = list()
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        combo_operand = {
            0: 0, 
            1: 1, 
            2: 2, 
            3: 3, 
            4: a, 
            5: b,
            6: c
            }[operand]
        match opcode:
            case 0:  # adv
                a = a >> combo_operand
            case 1:  # bxl
                b = b ^ operand
            case 2:  # bst
                b = combo_operand % 8
            case 3:  # jnz
                if a != 0:
                    ip = operand
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                output.append(combo_operand % 8)
            case 6:  # bdv
                b = a >> combo_operand
            case 7:  # cdv
                c = a >> combo_operand
        ip += 2
    return output


part1 = ",".join(list(map(str, computer(a))))
print(f"Part 1: {part1}")


# Part 2
"""
B = A % 8
B = B ^ 1
C = A >> B
A = A >> 3
B = B ^ A
B = B ^ C
output B % 8
loop
"""
# The highest 3 bits of A are 0
# The 3 next highest of A are 3
# ... this because it always cuts 8

candidates = [0]
for l in range(len(program)):
    next_candidates = []
    for val in candidates:
        for i in range(8):
            target = (val << 3) + i
            if computer(target) == program[-l-1:]:
                next_candidates.append(target)
    candidates = next_candidates

part2 = min(candidates)
print(f"Part 2: {part2}")
