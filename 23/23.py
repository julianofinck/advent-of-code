"""
 Day 23: LAN Party 
"""
with open("23/input.txt", "r") as f: conns = f.read().strip().split("\n")
def part1():
    inter_conn_computers = list()
    # Get 1st connection
    for conn in conns:
        # If Chief Historian, first letter must be a t
        if "t" in (conn[0], conn[3]):
            c1, c2 = conn.split("-")
            
            # Get 2nd connection
            for conn2 in conns:
                if conn != conn2 and (c1 in conn2 or c2 in conn2):
                    c3, = (c for c in conn2.split("-") if c not in (c1, c2))

                    # Get 3rd connection
                    for conn3 in conns:
                        if conn3 not in (conn, conn2) and c3 in conn3 and (c1 in conn3 or c2 in conn3):
                            set_ = {c1, c2, c3}
                            if set_ not in inter_conn_computers:
                                inter_conn_computers.append(set_)
    return inter_conn_computers

trios = part1()
print(len(trios))   # 5883 too high

unique_pcs = list(set([pc for con in conns for pc in con.split("-")]))
lans_found = list()
skip_trios = list()
for i, trio in enumerate(trios):
    if i in skip_trios:
        continue

    # Check if more connected
    for new_pc in unique_pcs:
        if new_pc not in trio:
            # Try to connect
            connected = 0
            for pc in trio:
                connection = False
                for conn in conns:
                    if pc in conn and new_pc in conn:
                        connection = True
                        break
                if not connection:
                    break
                connected += 1
            if connected == len(trio):
                trio.add(new_pc)
            trio.add(pc)

    # LAN found
    lan = trio
    lans_found.append(lan)

    # If trio in LAN skip trio
    for j, trio in enumerate(trios):
        if j not in skip_trios:
            if all([pc in lan for pc in trio]):
                skip_trios.append(j)

trios = set([",".join(sorted(list(trio))) for trio in trios])
trios = list(trios)
trios.sort()

max_size = max([len(lan) for lan in lans_found])
biggest_lan, = (lan for lan in lans_found if len(lan) == max_size)
biggest_lan = ",".join(sorted(list(biggest_lan)))

print(f"Biggest LAN: '{biggest_lan}'")
