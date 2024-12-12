from itertools import product
import time

with open("07/input.txt", "r") as f:
    data = [[int(e) if ":" not in e else int(e[:-1]) for e in l.split(" ")] for l in f.read().strip().split("\n") ]
    eqs = [{e[0]: e[1:]} for e in data]


def operate(p, ns) -> int:
    result = ns[0]
    for n, o in zip(ns[1:], p):
        if o == "+":
            result += n
        elif o == "*":
            result *= n
        elif o == "||":
            result = int(str(result) + str(n))
        else:
            raise NotImplementedError(f"{o} not implemented")
    return result


def solve(operators, eqs) -> None:
    sum_ = 0
    ti = time.perf_counter()
    for eq in eqs:
        for ans, ns in eq.items():
            # Cartesian product via itertools
            for p in product(operators, repeat = len(ns) - 1):
                result = operate(p, ns)
                if result == ans:
                    sum_ += ans
                    break
    tf = time.perf_counter()
    eta = round((tf - ti) * 1000, 3)
    print(f"{eta:>12} ms -", f"Sum of solveable with {operators}:", sum_)


# Part 1
operators = ["+", "*"]
sum_ = solve(operators, eqs)
# 12553187650171

# Part 2
operators = ["+", "*", "||"]
sum_ = solve(operators, eqs)
# 96779702119491
