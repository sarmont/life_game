questions = ['Хорошо ли вы учитесь?', 'Умеете ли вы хорошо водить машину?']
lst_answers = []
error = ""
for question in questions:
    print(question)
    answer = input()
    if not ('да' == answer or 'нет' == answer):
        error = question
        break
    lst_answers.append(answer)

if error != "":
    print(f'Вы допустили ошибку в вопросе "{error}". Ответ должен быть "да" или "нет"')
elif lst_answers[0] == 'да' and lst_answers[1] == 'да':
    print('Вы обладаете потрясающим умом, очень осторожны, и ваша скорость реакции поражает')
elif lst_answers[0] == 'нет' and lst_answers[1] == 'да':
    print('Ваша скорость достаточна высока и вы очень осторожны,'
          ' но вам нужно поработать над своим интеллектом')
elif lst_answers[0] == 'да' and lst_answers[1] == 'нет':
    print('Вы обладаете потрясающим умом,'
          ' но вам следует уделить внимание вашей скорости реакции и осторожности')
elif lst_answers[0] == 'нет' and lst_answers[1] == 'нет':
    print(
        'Ваши знания недостаточно высоки, у вас медленная скорость реакции,'
        ' а также имеются проблемы с осторожностью, но вам есть к чему стремиться')