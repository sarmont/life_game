from math import sqrt

count = 0
n = 300001
while count < 4:
    q = []
    d = 2
    while d ** 2 < n:
        if n % d == 0 and d % 3 == 0 and d != n:
            q.append(d)
        if n % (n//d) == 0 and (n//d) % 3 == 0:
            q.append(n//d)
        d += 1
    if n % sqrt(n) == 0 and sqrt(n) % 3 == 0:
        q.append(sqrt(n))

    if len(q) == 5:
        count += 1
        #print(q)
        print(n, max(q))
    n += 1

