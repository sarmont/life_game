# река, холм, лес

objects = dict()
text = input().split(', ')
for el in text:
    objects[el] = []
print(objects)
n = input()
while not n.isdigit():
    for key in objects:
        if len(set(key) & set(n)) == 0:
            objects[key].append(n)
    n = input()
#print(objects)
for key in objects:
    print(f"{key}: {', '.join(objects[key])}")

