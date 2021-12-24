f = open('17.txt')
data = f.readlines()
data = [int(el) for el in data]
print(data)
q = []
count = 0
for i in range(len(data)-2):
    if data[i] < data[i+1]<data[i+2]:
        count += 1
        q.append(data[i+2] - data[i])
print(count, min(q))













