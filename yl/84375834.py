word = max_word = min_word = input()
maxim = minim = len(word)
while word != 'стоп':
    if len(word) > maxim:
        maxim = len(word)
        max_word = word
    if len(word) < minim:
        minim = len(word)
        min_word = word
    word = input()
if set(min_word) < set(max_word):
    print('ДА')
else:
    print('НЕТ')
