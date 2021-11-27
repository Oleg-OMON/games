from lottery import chois_rull
from lottery import twenty_one
from models import register_user, check_db_user


def menu():
    global name
    games_dict = {'1': chois_rull, '2': twenty_one}
    print(f'Добро пожаловать в казино Пангурбан!!!\n')

    reg = input('Вы зашли первый раз?  да/нет \n')
    if reg == 'да':
        name = input('Ваше имя: ')
        email = input('Ваша почта: ')
        register_user(name, email)
    if reg == 'нет':
        check_db_user(name)


if __name__ == '__main__':
    menu()
    while True:
        print(f'1: Лотерея\n'
              f'2: Очко\n')
        v = input(f'Выбери номер игры для начала или любую клавишу для выхода из игры:\n'
                  )
        if v == '1':
            chois_rull()

        if v == '2':
            twenty_one()

        else:
            print('Спасибо за игру! Жждем Вас снова :)')
            break
