from tabnanny import check
from turtledemo.penrose import start

#первый ход для крестиков-ноликов
def krestiki_noliki_first_move(number_of_game,player,number_of_move,moving):
    print(f'Игрок {player} делает {number_of_move} ход:')
    global table
    move1 = input()
    moving.append(move1)
    first_move = move1
    if move1 == '00':
        table = ('''           0 1 2
        0  x - -
        1  - - -
        2  - - -''')
        return table
    elif move1 == '01':
        table = ('''           0 1 2
        0  - x -
        1  - - -
        2  - - -''')
        return table
    elif move1 == '02':
        table = ('''           0 1 2
        0  - - x
        1  - - -
        2  - - -''')
        return table
    elif move1 == '10':
        table = ('''           0 1 2
        0  - - -
        1  x - -
        2  - - -''')
        return table
    elif move1 == '11':
        table = ('''           0 1 2
        0  - - -
        1  - x -
        2  - - -''')
        return table
    elif move1 == '12':
        table = ('''           0 1 2
        0  - - -
        1  - - x
        2  - - -''')
        return table
    elif move1 == '20':
        table = ('''           0 1 2
        0  - - -
        1  - - -
        2  x - -''')
        return table
    elif move1 == '21':
        table = ('''           0 1 2
        0  - - -
        1  - - -
        2  - x -''')
        return table
    elif move1 == '22':
        table = ('''           0 1 2
        0  - - -
        1  - - -
        2  - - x''')
        return table
    else:
        a = ('Введите корректное значение ячейки поля \nПрочтите пожалуйста правила "rules"')
        return a





#функция игры крестиков ноликов
def krestiki_noliki_game(number_of_game,player,number_of_move,table,symbol,moving):
    print(f'Игрок {player} делает {number_of_move} ход:')
    move = input()
    #проверка на возможность хода в ту или иную ячейку
    while True:
        if move in moving:
            print('Игрок уже поставил свой символ на эту ячейку!')
            move = input()
        else:
            moving.append(move)
            global table1
            new_table = list(table)
            #ход
            if move == '00':
                new_table[28]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '01':
                new_table[30]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)


            elif move == '02':
                new_table[32]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '10':
                new_table[45]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '11':
                new_table[47]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '12':
                new_table[49]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '20':
                new_table[62]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '21':
                new_table[64]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            elif move == '22':
                new_table[66]=f'{symbol}'
                table1 = ''.join(new_table)
                return(table1)

            else:
                print('Введите корректное значение ячейки поля \nПрочтите пожалуйста правила "rules"')
                return




#функция проверки завершенности игры
def check_game(table,player):
    check_table = list(table)
    global check_game_result

    if check_table[28] == 'o' and check_table[30] == 'o' and check_table[32] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[28] == 'x' and check_table[30] == 'x' and check_table[32] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[45] == 'o' and check_table[47] == 'o' and check_table[49] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[45] == 'x' and check_table[47] == 'x' and check_table[49] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[62] == 'o' and check_table[64] == 'o' and check_table[66] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[62] == 'x' and check_table[64] == 'x' and check_table[66] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[28] == 'o' and check_table[47] == 'o' and check_table[66] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[28] == 'x' and check_table[47] == 'x' and check_table[66] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[32] == 'o' and check_table[47] == 'o' and check_table[62] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[32] == 'x' and check_table[47] == 'x' and check_table[62] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[28] == 'o' and check_table[45] == 'o' and check_table[62] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[28] == 'x' and check_table[45] == 'x' and check_table[62] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[30] == 'o' and check_table[47] == 'o' and check_table[64] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[30] == 'x' and check_table[47] == 'x' and check_table[64] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[32] == 'o' and check_table[49] == 'o' and check_table[66] == 'o':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    elif check_table[32] == 'x' and check_table[49] == 'x' and check_table[66] == 'x':
        print(f'Поздравляю {player},вы победили!')
        print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
        check_game_result = 1

    else:
        check_game_result = 0






#интерфейс программы(основа программы)
print('Добро пожаловать в игру крестики-нолики!','\nДля того чтобы начать напишите "start"','\nДля того чтобы узнать правила игры напишите "rules"')
number_of_game = 0
player1 = 0
player2 = 0
check_game_result = 0
moving = []
for i in range(999):
    start_game = input()
    number_of_game += 1
    for j in range(999):
        if start_game == 'start':
            print(f'Игра #{number_of_game}')
            print('Игрок №1, напишите как вы хотите себя называть')
            player1 = input()
            print(f'Приветствую вас {player1}')
            print('Игрок №2, напишите как вы хотите себя называть')
            player2 = input()
            print(f'Приветствую вас {player2}')
            print(f'Игра #{number_of_game}')
            table = ('''                   0 1 2
                0  - - -
                1  - - -
                2  - - -''')
            print(table)
            # процесс игры

            number_of_move = 1
            print((krestiki_noliki_first_move(number_of_game,player1,number_of_move,moving)))

            number_of_move = 2
            symbol = 'o'
            print(krestiki_noliki_game(number_of_game,player2,number_of_move,table,symbol,moving))

            symbol = 'x'
            number_of_move = 3
            print(krestiki_noliki_game(number_of_game,player1,number_of_move,table1,symbol,moving))

            symbol = 'o'
            number_of_move = 4
            print(krestiki_noliki_game(number_of_game, player2, number_of_move, table1, symbol,moving))


            symbol = 'x'
            number_of_move = 5
            print(krestiki_noliki_game(number_of_game, player1, number_of_move, table1, symbol,moving))
            check_game(table1,player1)
            if check_game_result == 1:
                break
            else:
                check_game_result = 0

            symbol = 'o'
            number_of_move = 6
            print(krestiki_noliki_game(number_of_game, player2, number_of_move, table1, symbol,moving))
            check_game(table1,player2)
            if check_game_result == 1:
                break
            else:
                check_game_result = 0

            symbol = 'x'
            number_of_move = 7
            print(krestiki_noliki_game(number_of_game, player1, number_of_move, table1, symbol,moving))
            check_game(table1,player1)
            if check_game_result == 1:
                break
            else:
                check_game_result = 0

            symbol = 'o'
            number_of_move = 8
            print(krestiki_noliki_game(number_of_game, player2, number_of_move, table1, symbol,moving))
            check_game(table1,player2)
            if check_game_result == 1:
                break
            else:
                check_game_result = 0

            symbol = 'x'
            number_of_move = 9
            print(krestiki_noliki_game(number_of_game, player1, number_of_move, table1, symbol,moving))
            check_game(table1,player1)
            if check_game_result == 1:
                break
            else:
                print('Отличная игра! У вас ничья!')
                print('Для новой игры напишите "start"\nДля выхода из игры напишите "end"')
                break

        elif start_game == 'end':
            print('Закрываем игру')
            break
        #правила игры
        elif start_game == 'rules':
            print('Крестики-нолики — это очень древняя и интересная игра.\nЦель — поставка в один ряд три крестика или нолика и не дать своему сопернику сделать то же самое.\nУчастники по очереди ставят на свободные клетки поля знаки. Один играет крестиками, второй — ноликами. \nОбычно начинает ходить участник, ставящий крестики. Выигрывает тот, кто первым выстроит в ряд 3 свои фигуры по вертикали, горизонтали или диагонали.\nНачинают всегда крестики, соответсвенно игрок №1 начинает с них.\nНа игровом поле вы видите цифры 0 1 2 по диагонале и вертикали, чтобы поставить крестик или нолик введите номер желающей ячейки, например:01')
            break
        else:
            print('Некорректное значение', '\nДля старта игры напишите "start"','\nДля выхода из игры напишите "end"')
            break
