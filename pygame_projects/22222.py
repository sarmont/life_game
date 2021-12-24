n = input()
q1 = []
q2 = []
while not n.isdigit():
    q1.append(len(n))
    q2.append(n)
    n = input()

print(q2[q1.index(max(q1))])
print(q2[q1.index(min(q1))])


