from lottery import chois_rull
from lottery import twenty_one


def menu():
    games_dict = {'1': chois_rull, '2': twenty_one}
    print(f'Добро пожаловать в казино Пангурбан!!!Пока у нас всего две игры:\n1: Лотерея\n'
          f'2: Очко\n'
          f'Но это пока)\n')


if __name__ == '__main__':
    while True:
        menu()
        v = input('Выбери номер игры для начала: ')
        if v == '1':
            chois_rull()

        if v == '2':
            twenty_one()
