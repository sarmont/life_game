password = 'Masha'
p = 5
for i in range(p):
    print('Введите пароль')
    print("У вас попыток", p - i)
    user_pas = input()
    if user_pas == password:
        print("Вы отгадали. Вы экстрасенс!")
        break
    else:
        print("Повторите попытку. Вы ошиблись!")