from lottery import chois_rull
from lottery import twenty_one

if __name__ == '__main__':
    games_dict = {'1': chois_rull, '2': twenty_one}
    print(f'Добро пожаловать в казино Пангурбан!!!Пока у нас всего две игры:\n1: Лотерея\n'
          f'2: Очко\n'
          f'Но это пока)\n')
    v = input('Выбери номер игры для начала: ')

    if v == '1':
        chois_rull()

    if v == '2':
        twenty_one()


