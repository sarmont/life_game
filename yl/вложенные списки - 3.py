q = [0] * 30000
prog = input()
pos = 0
for el in prog:
    if el == ">":
        pos += 1
        pos %= len(q)
    if el == "<":
        pos -= 1
        pos %= len(q)
    if el == "+":
        q[pos] += 1
        q[pos] = q[pos] % 256
    if el == "-":
        q[pos] -= 1
        q[pos] = q[pos] % 256
    if el == ".":
        print(q[pos])