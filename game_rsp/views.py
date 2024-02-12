import random
from django.shortcuts import render


def rsp(request):
    user_choice = ''
    user_count = 0
    bot_choice = ''
    bot_count = 0
    result = ''

    # Получаем имя пользователя
    username = 'Привет!'
    if request.user.is_authenticated:
        if request.user.first_name:
            username = f'Привет, ' + request.user.first_name + '!'
        else:
            username = f'Привет, ' + request.user.username + '!'

    # Проверяем отправку формы
    if request.method == "POST":
        # Текущие очки
        user_count = int(request.POST['user_count'])
        bot_count = int(request.POST['bot_count'])

        # Если повтор игры
        if request.POST['rsp'] == 'next':
            result = 'next'
        else:
            # Выбор пользователя
            user_choice = request.POST['rsp']
            # Cлучайный выбор бота
            bot_choice = random.choice(['rock', 'paper', 'scissors'])


            # Определяем победителя
            if user_choice == bot_choice:
                result = 'draw'
            elif ((user_choice == 'rock' and bot_choice == 'scissors') or
                  (user_choice == 'scissors' and bot_choice == 'paper') or
                  (user_choice == 'paper' and bot_choice == 'rock')):
                result = 'user'
                user_count += 1
            else:
                result = 'bot'
                bot_count += 1

    # Передаем данные
    data = {
        'title': 'Игра "Камень, ножницы, бумага"',
        'username': username,
        'user_choice': user_choice,
        'user_count': user_count,
        'bot_choice': bot_choice,
        'bot_count': bot_count,
        'result': result,
    }

    return render(request, 'game_rsp/game_rsp.html', data)
