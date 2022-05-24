import pprint

matrix = []
n, m = [int(a) for a in input().split()]
for i in range(n):
    matrix.append([0] * m)

print(matrix)

index = 1
column = 1
for i in range(m):
    for j in range(n):
        if column % 2 != 0:
            matrix[j][i] = index
            if index % n == 0:
                column += 1
                index += 4
            else:
                index += 1
        else:

            matrix[j][i] = index
            if index % (n + 1) == 0:
                column += 1
                index += n
            else:
                index -= 1


for el in matrix:
    print(*el)
