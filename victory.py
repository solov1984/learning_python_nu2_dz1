game_on = True
number_of_questions = 5

while game_on:
    number_of_right_answers = 0

    # Верный ответ - 1870
    year = input("1/5. В каком году родился Ленин? ")
    number_of_right_answers += int(year == '1870')

    # Верный ответ - 1962
    year = input("2/5. В каком году родился Виктор Цой? ")
    number_of_right_answers += int(year == '1962')

    # Верный ответ - 1946
    year = input("3/5. В каком году родился Фредди Меркьюри? ")
    number_of_right_answers += int(year == '1946')

    # Верный ответ - 1953
    year = input("4/5. В каком году родился Андрей Макаревич? ")
    number_of_right_answers += int(year == '1953')

    # Верный ответ - 1961
    year = input("5/5. В каком году родился Вячеслав Бутусов? ")
    number_of_right_answers += int(year == '1961')

    separat = ' - '
    print('Количество верных ответов', number_of_right_answers,sep=separat)
    print('Количество ошибочных ответов', number_of_questions - number_of_right_answers,sep=separat)
    print('Процент верных ответов', number_of_right_answers / number_of_questions * 100,sep=separat)
    print('Процент ошибочных ответов', (number_of_questions - number_of_right_answers) / number_of_questions * 100,sep=separat)

    repeat_game_str = input('Повторить викторину? (да/нет) ')
    game_on = (repeat_game_str == 'да')
