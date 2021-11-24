import random
from pprint import pprint
import timer


def chois_rull():

    print(f'Приветсвую в лотерее! У вас 1000 фишек. Каждый проигрыш отнимет у вас 100 фишек. Удачи)')

    while True:
        start = input('Начать игру: ')
        money = 1000
        if start == 'да':
            chois_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9]]
            pr = 1000000
            my_list = []

            for i in chois_list:
                pprint(i)
            print()

            number_1 = int(input('Выберите число из первой строки #1: '))
            my_list.append(number_1)
            number_2 = int(input('Выберите число из первой строки #2: '))
            my_list.append(number_2)
            number_3 = int(input('Выберите число из первой строки #3: '))
            my_list.append(number_3)
            print()

            chois = random.sample(chois_list[1], 3)

            if chois == my_list:
                money += pr
                print(f'Поздравляю, числа совпали! Вы выйграли!'
                      f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            elif chois[0] == my_list[0]:
                money += 10 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            elif chois[0:2] == my_list[0:2]:
                money += 25 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            if chois[0] == my_list[1]:
                money += 5 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            elif chois[1] == my_list[0]:
                money += 5 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            elif chois[1] == my_list[1]:
                money += 5 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            elif chois[2] == my_list[2]:
                money += 5 * (pr // 100)
                print(f'{chois}\n'
                      f'{my_list}\n'
                      f'Ваш баланс: {money}')

            else:
                print(f'Не в этот раз:(\n'
                      f'{chois}\n'
                      f'{my_list}\n'
                      f'Попробуйте еще раз!'
                      f'Ваш баланс: {money - 100}')

            if money == 0:
                print(f'У вас закончилтсь фишки( они обновляться через 1 минуту. Ожидайте\n'
                      f'#####################')
                timer.timer()
                money = 1000
                print(f'Ваш баланс обновлен\n'
                      f'{money} фишек\n')

        if start == 'нет':
            break


def twenty_one():
    money = 100
    print(f'Приветсвую в Игре "ОЧКО"! У вас {money} фишек.'
          f' Каждый проигрыш отнимет у вас 10 фишек, а победа их добавит. Удачи)')
    while True:
        global user_result, point
        playing_cards = {'Туз': 11, 'Король': 4, 'Дама': 3, 'Валет': 2,
                         '10': 10, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                         '3': 3, '2': 2}

        start = input('Начать игру: ')

        if start == 'да':
            user_card = random.choice(list(playing_cards.items()))
            comp_card = random.choice(list(playing_cards.items()))
            two_comp_card = random.choice(list(playing_cards.items()))
            comp_point = int(comp_card[1] + two_comp_card[1])

            print(f'Ваша карта: {user_card[0]}\n'
                  f'Очки: {user_card[1]}')
            contin = input(f'Еще?\n')

            if contin == 'да':
                user_cards = random.choice(list(playing_cards.items()))
                point = int(user_card[1] + user_cards[1])
                user_result = (f'Ваша карты: {user_card[0]},{user_cards[0]}\n'
                               f'Очки: {user_cards[1]}\n'
                               f'Cумма очков: {point}\n')
                print(f'{user_result}\n'
                      f'Соперник : {comp_card[0]}, {two_comp_card[0]}\n'
                      f'Сумма очков {comp_point}\n')
                if point > comp_point:
                    money += 10
                    print(f'Вы выйграли!)\n'
                          f'Ваш баланс {money}')
                else:
                    money -= 10
                    print(f'Вы проиграли!(\n'
                          f'Ваш баланс {money}')

            else:
                print(f'Соперник : {comp_card[0]}, {two_comp_card[0]}\n'
                      f'Сумма очков {comp_point}\n\n'
                      f'{user_result}')
                if point > comp_point:
                    money += 10
                    print(f'Вы выйграли!)\n'
                          f'Ваш баланс {money}')
                else:
                    money -= 10
                    print(f'Вы проиграли!(\n'
                          f'Ваш баланс {money}\n')

            if money == 0:
                print(f'У вас закончилтсь фишки( они обновляться через 1 минуту. Ожидайте\n'
                      f'#####################')
                timer.timer()
                money = 100
                print(f'Ваш баланс обновлен\n'
                      f'{money} фишек\n')

        if start == 'нет':
            break



