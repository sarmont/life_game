n = 5
s = 'asjdhk - ashdkj - jkas - hdjhs - akjdh - jashkdj - hjaksdh - ajdhaskj - dhaskjh'
words = [word for word in s.split(' - ')]
print(words)
count = 0
q = []
for el in words:
    if len(el) > n:
        q.append(el)
print('; '.join(q))