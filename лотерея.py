import time
#
tickets = []
players1 = []

def players(a,v):
    print('заполняем список участников')
    timing = time.time()
    k = 'yes'
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
         85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    for i in range(1000):
        print('Напишите "ready" для старта')
        d = input()
        if d == 'ready':
            print('Напишите Ваше имя')
            g = input()
            if g[0].isupper():
                v.append(g)
                print('Имя успешно зарегестрировано')
                k = 'yes'
            else:
                print('Имя должно начинаться с заглавной буквы')
                k = 'no'
            if k == 'yes':
                print('Напишите номер билета, которого хотите зарегистрировать за собой. Свободные билеты:', c)
                b = int(input())
                filtered_c = list(filter(lambda x: x==b,c))
                if time.time() - timing > 60.0:
                    v.remove(v[-1])
                    return('Время набора участников вышло')
                elif(filtered_c):
                    a.append(b)
                    c.remove(b)
                    print('Новый участник зарегистрирован')
                    print('Продолжаем набор участников')
                elif len(a)==100:
                    return('Максимальное кол-во участников')
                elif b > 100:
                    print('Некорректное название билета')
                else:
                    print('Данный билет уже занят')
            elif k == 'no':
                print('Попробуйте ещё раз')
        else:
            print('Некорректное значение')

m = 0
game_score = 'gamescoree'
while True:
        game_score=(game_score[:-1])
        m += 1
        game_score = game_score + str(m)
        print(game_score)
        players(players1,tickets)
        print('Список участников и их билетов в', game_score)
        game = (list(zip(players1, tickets)))
        print(game)
        # random_winner = random.randint(0,100)
        random_winner = 1
        for i in range(0,100):
            if random_winner == game[i][0]:
                print('Номер выйгрышного билета:',random_winner,'\nПоздравляем игрок под именем:',game[i][1],'-выйграл')
                break
            elif i > len(game):
                print('Номер выйгрышного билета:', random_winner, 'Победителя не было найдено!')
            else:
                h = True