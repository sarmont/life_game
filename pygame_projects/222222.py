n = input()
ma = -1
mi = len(n)
text_mi = n
text_ma = ''
while not n.isdigit():
    if len(n) > ma:
        ma = len(n)
        text_ma = n
    if len(n) < mi:
        mi = len(n)
        text_mi = n
    n = input()
print(text_mi, text_ma)