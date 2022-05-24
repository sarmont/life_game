s = open('24.txt').readlines()
count  = 0
for line in s:
    if line.count('AOA') > line.count('OAO'):
        count += 1

print(count)

