q = [[1,5,8],
     [9,5,2],
     [4,8,1]]
print(q[0][1])
s = 0
for i in range(len(q)):
    for j in range(len(q)):
        if i == j:
            s += q[i][j]
print(s)


