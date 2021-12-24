f = open('24 (1).txt')
s = f.readline()
s = [int(el) for el in s]
print(s)
max_count = 0
count = 1
for i in range(len(s)-1):
    if (s[i] % 2 == 0 and s[i+1] % 2 == 0) or (s[i] % 2 != 0 and s[i+1] % 2 != 0):
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1
print(max_count)