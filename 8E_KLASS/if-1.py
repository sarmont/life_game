# создаем список нулей
s = [0]* 10000000

# стартовое значение
s[9] = 1
for i in range(9,12 + 1):
    s[i + 1] += s[i]
    s[i +2] += s[i]
    s[i *2] += s[i]

print(s[12])
