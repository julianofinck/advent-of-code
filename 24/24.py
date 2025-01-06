"""
 Day 24: Crossed Wires 
"""
import re
with open("24/input.txt", "r") as f: inputs, gates = f.read().strip().split("\n\n")

inputs = {k: True if v == "1" else False for i in inputs.split("\n") for k, v in [i.strip().split(": ")]}

# Prepare all nodes
nodes = inputs.copy()
all_nodes = list(set(re.findall("[a-z0-9]{3}", gates)))
for n in all_nodes:
    if n not in nodes:
        nodes[n] = None

# Let the system run
old_new = {
    "x21 XOR y21 -> nnr": "x21 XOR y21 -> rqf",
    "y21 AND x21 -> rqf": "y21 AND x21 -> nnr",

    "kcm XOR grr -> fkb": "kcm XOR grr -> z16",
    "tnn OR bss -> z16": "tnn OR bss -> fkb",

    "qsj AND tjk -> z31": "qsj AND tjk -> rdn",
    "qsj XOR tjk -> rdn": "qsj XOR tjk -> z31",

    "gcg XOR nbm -> rrn": "gcg XOR nbm -> z37",
    "y37 AND x37 -> z37": "y37 AND x37 -> rrn"
}
for old, new in old_new.items():
    gates = gates.replace(old, new)


gates = [re.findall("(.{3}) (.{2,3}) (.{3}) -> (.{3})", gate)[0] for gate in gates.split("\n")]
while any(v is None for v in nodes.values()):
    for (in1, op, in2, out) in gates:
        if nodes[out] is None:
            if nodes[in1] is not None and nodes[in2] is not None:
                match op:
                    case "AND":
                        nodes[out] = nodes[in1] & nodes[in2]
                    case "OR":
                        nodes[out] = nodes[in1] | nodes[in2]
                    case "XOR":
                        nodes[out] = nodes[in1] ^ nodes[in2]
                    case _:
                        raise RuntimeError(f"What is this op? '{op}'")

# Read z nodes
z_nodes = {k: v for k, v in nodes.items() if k.startswith("z")}
final_number = "".join(["1" if z_nodes[k] else "0" for k in sorted(z_nodes.keys(), reverse=True)])
print(int(final_number, 2))

# Part 2 - four pairs of gates whose output wires have been swapped
#   two 45 bits numbers go in
#   222 logic gates
#   the sum must match
for op_type in ("XOR", "OR", "AND"):
    print(op_type, sum([1 if gate[1] == op_type else 0 for gate in gates]))

nodes_fig = list()
h = 1
w = list()
z1_ = z2_ = last_and = and__ = or_ = "   "
# Printing and comparing
for i in range(45):
    x, y = f"x{i:0>2}", f"y{i:0>2}"

    and_, = (gate[3] for gate in gates if all(a in gate[0:3] for a in (x, y, "AND")))
    xor_, = (gate[3] for gate in gates if all(a in gate[0:3] for a in (x, y, "XOR")))
    and__ = "   "
    if "   " not in (z1_, z2_):
        and__ = [gate[3] for gate in gates if all(a in gate[0:3] for a in (z1_, z2_, "AND"))]
        if and__:
            and__ = and__[0]
    z1, op, z2 = [gate[0:3] for gate in gates if gate[3] == f"z{i:0>2}"][0]
    if xor_ != z1:
        z1, z2 = z2, z1
    if last_and != and__:
        or_ = [gate[3] for gate in gates if all(a in gate[0:3] for a in (last_and, and__, "OR"))]
        if or_:
            or_ = or_[0]
        else:
            print(1)
    status_or = "     " if (or_ == z2 or i == 0 or last_and == and__) else f"({z2})"
    status_z = "" if (xor_ in (z1, z2) or i == 0) else "x"
    status_xor = "" if (z1 == xor_ or i == 0) else f"({z1})"
    print(f"{i:0>2}   (& {and_}  ^ {xor_} {status_xor})    {last_and} | {and__} = {or_} {status_or}    {z2} {op} {z1} = z{i:0>2} {status_z}")
    z1_ = z1
    z2_ = z2
    last_and = and_

fixed = [v.split(" ")[-1] for v in old_new.values()]
fixed.sort()
print(",".join(fixed))
# fkb,nnr,rdn,rqf,rrn,z16,z31,z37