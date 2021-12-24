a = '1, 4, 56, 67, 23'
b = '11, 4, 56, 67, 23'
c = '1, 4, 156, 167, 23'
# 4, 56,67,23, 1, 156, 167
a1 = set([n for n in a.split(', ')])
b1 = set([n for n in b.split(', ')])
c1 = set([n for n in c.split(', ')])
w = (a1 & b1) | c1
print(w)
print(sum([int(el) for el in list(w)]))

