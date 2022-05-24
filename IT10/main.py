import random
q = [random.randint(0, 100) for i in range(10)]
print(*q)
m = 0
m_n = None
for n in q:
    buf = n
    s = 0
    while buf > 0:
        s += buf % 10
        buf //= 10
    # m = max(s, m)
    if s > m:
        m = s
        m_n = n
print(m_n)

