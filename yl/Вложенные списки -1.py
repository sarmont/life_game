n = int(input())
milk = [int(input()) for _ in range(n)]
mi = int(input())
ma = int(input())
#print(milk)
for el in milk:
    if mi <= el <= ma:
        print(el)
