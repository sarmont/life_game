s = [1, 45, 23, 456, 23, 345]

for start in range(len(s)):
    for finish in range(start, len(s)):
        print(s[start:finish + 1])
