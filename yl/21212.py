n = int(input())
k = 1
line = 1
while k <= n:
    for i in range(line):
        print(k, end=' ')
        k = k + 1
        if k > n:
            break
    print()
    line = line + 1
