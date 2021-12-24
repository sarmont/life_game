line = int(input())
column = int(input())
table = list()
count = 0

for j in range(line):
    temp = list()
    for i in range(column):
        temp.append(input())
    table.append(temp)

for name in table:
    for name_2 in name:
        print(name_2, end="\t")
    print()

