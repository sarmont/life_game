user_name = input()
flag = False
symbols = 'abcdefghijklmnopqrstuvwxyz1234567890_'
"""symb = ''
for i in range(ord('a'), ord('z') + 1):
    symb += chr(i)
print(symb)
"""
for let in user_name:
    if let not in symbols:
        flag = True
        print('Неверный символ:', let)
        break
if flag is False:
    print('OK')
