s = input()
max_word_2 = []
while s != s.capitalize():
    words = [word for word in s.split()]
    m = -1
    max_word = ''
    for word in words:
        if len(word) > m:
            m = len(word)
            max_word = word
    max_word_2.append(max_word)
    s = input()
print(max_word_2)
max_word_2.sort()
print(' '.join(max_word_2))
"""
к верхнему или приведены
добавляет справа или
получить это число иначе
Добро
"""