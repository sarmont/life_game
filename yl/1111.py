n = 3786427364
a = n % 10
b = n % 100 // 10
print(a + b)
m = 10 ** 8


print(int(str(n)[-1]) + int(str(n)[-2]))
s = [234,234,23,434,645,76,87,24,534,6,457,34,5,34]
for i in range(len(s)):
    if s[i] < m:
        m = s[i]