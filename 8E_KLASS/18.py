n = int(input())
words = []
for i in range(n):
    words.append(input())
print(words)
for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
        if words[i] > words[j]:
            words[i], words[j] = words[j], words[i]
print(words)