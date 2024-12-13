# from copyreg import pickle
# from os import write
# from random import random
# from re import ASCII
#
# from unicodedata import decimal
#
# a = 10
# b = a
# print (a)
# print (b)
# b = 20
# print (a)
# print (b)
#
# a = 20
# b = 30
# a = b
# print (b)
# print (a)
# b = 10
# print (a)
# print (b)
#
# a, b, c, d, e = 25, 30, 35, 40, 45
# print (a,b,c,d,e)
#
# m = 4,5,6,7,8,9
# print(m)
# b,c,d,e = 1,2,3,4
# g = b,c,d,e
# f = str ("васек")
# print (f)
# print (b,c,d,e)
# print (a)
# a = int (10)
# b = float (5.5)
# c = a+b
# print(c)
#
# a = 25
# b = 2
# c = a/b
# print (c)
# d = a//b
# print (d)
# e = float (a%b)
# print(e)
# f = a**b
# print(f)
# a = 10+16
# print((type(a)),(a))
# a = 20/10
# print(a)
#
# a = 666**999
# print(len(str(a)))
#
# import math
# a = math.sqrt(64)
# print (a)
# print (15**42)
#
# a = True
# print(type(a))
# print (a==1)
# print (a==0)
#
#
# a = 25
# if a > 15:
#     b = str ("ты тупой")#но ты в этом не виноват, это всё код.
# else:
#     b = str ("красавчик, брат")
# print (b)
# a = 0b100
# print (a)
# a = 33 < 33.1
# b = 0b100 > math.pi
# c = 40.0 == 40
# d = 0xc
# e = 55 != 0o102
# print (a,b,c,d,e)
#
# a=55
# if a%2 == 1:
#     b = str ("нечётное")
# else:
#     b = str ("чётное")
# print(b)
# print(hex(0xb64))
# a = 5+4
# print((bin(a)))
# print (oct(99))
# a = 98+1
# print (oct(a))
# print ((bin(a)))
# from decimal import Decimal
# a = (Decimal("2.44")*Decimal("3.122"))
# print (a)
# print(0.1 + 0.2 == 0.3)
# a = ((Decimal(0.2))+(Decimal(0.1)))
# print (a)
# b = 0.3
# print (b)
# c = a==b
# print (c)
# a = Decimal("0.2")+Decimal("0.1")
# print (a)
# b = Decimal("0.3")
# print (b)
# c = a==b
# print (c)
# a = float("0.2")+ float("0.1")
# b = "0.3"
# print (a)
# print (b)
# c = a==b
# print (c)
# print(Decimal("99.1"))
# print(99.1)
# print (99.1 == Decimal("99.1"))
# a = 64
# print (a)
# print (type(a))
# b = float(a)
# print(b)
# print(type(b))
# a = Decimal("4.8")
# print (type(a))
# b = float(a)
# print(b)
# print(type(b))
# a = 12.55
# print(round(a))
# b = round(a)
# print(b)
#
# a = 12.95
# b = math.floor(a)
# print (b)
# b = math.ceil(a)
# print(b)
# a = -50
# print(abs(a))
# seconds_since_birthdate = 450000000
# b = seconds_since_birthdate/31104000
# print (math.floor(b))
# c = seconds_since_birthdate//31104000
# print (c)
# print(b)
# d = b
# if b == d+0.1:
#     b = b
# else:
#     b = c
# e = round(e)
# print(e)
# seconds_since_birthdate = 490000000
# b = seconds_since_birthdate/31104000
# print(b)
# c = math.ceil(b)
# d = c-1
# print(d)
# c = int(b)
# print(c)
# a = "string"
# b = 'string'
# c = """string"""
# d = '''string'''
# print(a,b,c,d)
# print(a == b == c == d)
# a = 10
# b = 10
# c = 10
# d = 11
# print(a == b == c )
# a = "проприетарный"[3]
# print(a)
# b = "лоускилл"[5]
# a = "креативный"[0:6]
# print(a+"н")
# a = "12345678910"[4:-4:2]
# print(a)
# a = "Перед взятием среза проверьте, что"
# b = len(a)>=42
# print(b)
# if b == True:
#     print("all is good")
# else:
#     print("length error")
# if len(a)>=42:
#     print("all is good")
# else:
#     print("length error")
#
# print (c)
# b = a[7:41]
# a = "жили были дед, да бабка"
# b = len(a)
# print(b)
#
# a = "abcdefghijk 1456 ahalai-mahalai!wwwwwwwwwq"
# if len(a)>=42:
#     b = ("all is good")
# else:
#     b = ("error")
# print(b)
# if b == ("all is good"):
#     print(a[7:42:3])
# else:
#     print("add more words")
#
# a = "Сегодня я встал, почистил зубы,и вдруг мне пришла скидка,20 %.Конец предложения"
# f = "скидка"
# b = a.index("скидка")
# e = len(f)
# print(b)
# g = b+e
# h = g+1
# print(g)
# print(e)
# if a[g:h]==",":
#     e = e+1
# else:
#     e = e
# print(e)
# print (b)
# d = a.index(".Конец")
# print(d)
# print(a[(b+e):d])
#
# text = "5423534 lajksdfij;jhh абракадабра message: dfasdfs9d6f7686"
# template = 'message: '
# index = text.find(template)
# if index != -1:
#     print(text[index + len(template):])
# else:
#     print(index)
#
#
# text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
# template = 'message: '
# if template in text:
#     index = text.index(template)
#     print(text[index + len(template):])
#
# "_name".startswith("_")
# name = "_internal_attr_2"
# if not name.startswith("_"):
#     print(name)
# b = "П"
# d = "опрошайка"
# e = "попрошайка"
# if e.istitle():
#     print(e)
# else:
#     c = b+d
#     print(c)
# # ASCII
# # a = "здарова брат, я ща в 5 классе, прикол?"
# # if a.ASCII:
# #     print("true")
# # else:
# #     print("false")
#
# a = ""
# if len(a) != 0:
#     if a.endswith("_"):
#         print(True)
#     else:
#         print(False)
# else:
#     print("нулевая строка")
#
# a = "ну я типо такой стою дома, думаю надо решить пример, ну типо берут учебник, вот и открываю нужную страницу, а там типо вообще непонятно ничо, чо делать, думаю ну типо может в инете глянуть? а там типо тоже пусто, прикиньте"
# b = a.count("типо")
# print(b)
# a = "ЗДАРОВА БРАТ КАК ДЕЛА?"
# b = a.casefold()
# print(b)
# a = "А роза упала на лапу Азора"
# b = a.casefold().replace(" ","")
# print(b)
# print(b[::-1])
# print(b == b[::-1])
# a = "2024 год, Лев Смолев теперь звезда".split()
# # b = a.index("звезда")
# print(a)
# d = ", лохов,".join(a)
# print(d)
# a = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!"
# b = a.casefold().count("тр")
# print(b)
# a = "--+-- Запись номер 1 --+--"
# b = a.removesuffix("--+--")
# print(b)
# f = "!Да чтоб тебя таращило!"
# b = "Тестовый текст 3(!)"
# c = "Где мои деньги???"
# f = f.rstrip("!().?")
# b = b.strip("!().?")
# c = c.strip("!().?")
# e = f,b,c
# print(e)
# r = 15
# h = 10
# r = r/100
# v = math.pi*(r**2)*h
# v = round(v,2)
# print(v, "-объём цилиндра")
# a = "лёва "
# b = ("крутой")
# c = a+b
# print(c)
# n = 20**50
# n = str(n)
# m = len(n)
# print(m)
# a = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри"
# b = a.count(" ")
# c = b+1
# d = a.split()
# e = len(d)
# print(e)
# print(c,"слова в предложении")
# string = "Давным-давно, в далёкой-далёкой галактике номер 9 жил-был слесарь."
# print(len(string.split()))
# a = "2024 год, Лев Смолев теперь звезда".split()
#
# a= 142 - 40 / 10 * 3 + 10 == 194
# print(a)
# # a = "Сегодня утром {0} автомобиля и {0} омнибуса проехали по мосту {1}.".format(4, "Саутуарк")
# # print(a)
# # a = "Сегодня утром {0} автомобиля и {0} омнибуса проехали по мосту {1}.".format(input(), input())
# # print(a)
# # a = "Сегодня утром %s автомобиля и %s омнибуса проехали по мосту %s." % "dsa"
# # print(a)
# # a = "Сегодня утром * автомобиля и * омнибуса проехали по мосту -."
# # b = a.replace("*", input())
# # b = b.replace("-", input())
# # print(b)
# # a = "9"
# # print(14**2)
# # a = round(5.724609312,3)
# # print(a)
# # a = input("Введите кол-во тракторов ")
# # b = input("Введите кол-во картошки ")
# # c = input("Введите множитель ")
# # c = int(c)
# # d = "За прошедший месяц было продано __ мешков картошки и __ тракторов"
# # e = d[:50]
# # f = d[50:]
# # e = e.replace("__",b)
# # f = f.replace("__",a)
# # g = e+f
# # print(g*c)
# # print(f"За прошедший месяц было продано {b} мешков картошки и {a} тракторов\n"*c)
# # for i in range(5):
# #     print()
# #     for j in range(3):
# #         print(f'i = {i}, j = {j}')
# #
# # for i in range (1,10):
# #     print()
# #     for j in range(1,11):
# #         a = i*j
# #         print(f' {i} * {j} = {i*j}')
#
# # a = input('')
# # if a=="monday":
# #     print("8:00")
# # elif a=="sunday":
# #     print("10:00")
# # elif a =="thuesday":
# #     print("11:00")
# # else:
# #     print("Введите корректный день недели")
# #
# # a = 2%2
# # print(a)
# correct_login = "eerie"
# correct_password = "KirkinderXx03"
# print("Введите ваш логин")
# login =input()
# print("Введите ваш пароль")
# password = input()
# if login==correct_login and password==correct_password:
#     print("Добро пожаловать",login)
# else:
#     print("указанные данные не верные")
# # clients = []
# # print("Введите имя нового клиента")
# # for i in range(1,10):
# #     new_client = input()
# #     clients[i] = new_client
# # print(clients)
# # name = input()
# # if name==clients[0] or name==clients[1] or name==clients[2]:
# #     print('good')
# # else:
# #     print('wrong')
#
# clients = ['eerie','kirkinderxx','pozetuve03']
# print(clients[::-1])
# print("Введите имя нового клиента")
# for i in range(1,10):
#     new_client=input()
#     clients.append(new_client)
#     print(clients)
# print(clients)
# print("Количество клиентов с бонусной программой:",len(clients))
# for i in range(len(clients)):
#     print(f'{i+1}. {clients[i]}')
#
# import random
#
# number = random.randint(1,10)
# print("Введите любое число до десяти")
# guess = int(input())
# if guess==number:
#     print("Поздравляю! Вы выйграли!")
# else:
#     print("К сожалению вы проиграли")
#
# clients = ['eerie','kirkinderxx','redkavandr','pozetuve03']
# print("Введите ваш ник")
# client_name=input()
# if client_name in clients:
#     print('Вы являетесь нашим постоянным клиентом!')
# else:
#     print("Вы не являетесь нашим постоянным клиентом")
#
# coworkers = ["Дмитрий","Владислав","Андрей","Александр","Анатолий"]
# print('Имя первого пользователя',coworkers[0])
# print('Имя последнего пользователя',coworkers[-1])
# print('Имя каждого пользователя',coworkers[:])
# print('Имя каждого второго пользователя',coworkers[1::2])
# print('Количество пользователей:', len(coworkers))
# print('Введите имя нового пользователя')
# while True:
#     new_worker = input()
#     if (',') in new_worker:
#         print('Недопустимый символ в имени')
#     else:
#         break
# coworkers.append(new_worker)
# print('Новый список пользователей:', coworkers)
# print("Количество пользователей:",len(coworkers))
# print('Проверка пользователя на состав бригады, введите имя пользователя')
# a = input()
# if a in coworkers:
#     print('Пользователь состоит в бригаде')
# else:
#     print("Пользователь не состоит в бригаде")
#
# a = tuple([1,2,3,3,8,4,5,6])
# print(a)
# a = (1,2,3,4,5,6)
# print(a)
#
# #создадим множества
# a = set([1,2,3,4,4,9,5,4,6,7])
# print(a)
# a = {1,2,3,4,4,5,4,6,7}
# print(a)
# a = {}
# print(type(a))
# a = set([1,2,3,4,5,'wow','interesting'])
# print("Введите слово, которое должно быть в кортеже")
# d = input()
# if d in a:
#     for elem in a:
#         print(elem)
# else:
#     print("Вы ввели неправильное слово, попробуйте ещё раз, попыток осталось 2")
#     d = input()
# if d in a:
#     1==True
# else:
#     print("Вы ввели неправильное слово, попробуйте ещё раз, попыток осталось 1")
#     d = input()
# if d in a:
#     1 == True
# else:
#     print('''Вы ввели неправильное слово, попыток осталось 0
#     попробуйте позже''')
# if 'interesting' not in d:
#     print("Показать пример правильного множества?")
#     j = input()
#     if "да" in j:
#         print("Пример правильного множества")
#         for elem in a:
#             print(elem)
#     elif "нет" in j:
#         print("Всего доброго!")
#     else:
#         print("Повторите операцию снова")
# else:
#     print("Поздравляю, слово введено верно!")
#
# family = ("Лиза","Рита","Андрей","Дмитрий")
# print('Первый член семьи:',family[0])
# print('Последний член семьи:',family[-1])
# print('Четные члены семьи:')
# for i in range(len(family)):
#     i += 1
#     if i%2!=0:
#         print(family[i])
# print('Количество членов семьи:',len(family))
#
# a = {1,2,3,5,6,5,6,7,8,8,8,9}
# b = int(input())
# if b in a:
#     a.remove(b)
# else:
#     a.add(b)
# print(a)
# client_list=["dima","liza","oleg","vanya","semen"]
# client_list.extend(["borya","vasilisa"])
# print(client_list)
# client_list.insert(2,"roma")
# print(client_list)
# print('Введите ваше имя')
# new_client=input()
# client_list.append(new_client)
# if client_list[8] in client_list:
#     print("Зарегистрирован 10-ый посетитель!")
#     client_list.pop(8)
#     client_list.insert(8,new_client)
#     client_list.insert(9,"dima blinov")
#     print(client_list)
# else:
#     print("юбилейного посетителя пока нет")
# print("Обнаружен обман")
# client_list.sort(reverse=True)
# print(client_list)
# print("какое кол-во дел запланировано на сегодняшний день?")
# a = int(input())
# todo = []
# print("Введите ваши планы/дела по порядку")
# for i in range(a):
#     b = input()
#     todo.append(b)
# print(todo)
# print("Введите номер вашего дела, котоырй нужно отредактировать")
# nomer = int(input())
# nomer1 = nomer-1
# print(todo[nomer1])
# todo.pop(nomer)
# print("Введите новое отредактированное дело")
# с = input()
# todo.insert(nomer,с)
# print("Введите номер дела которое нужно удалить")
# d = int(input())
# d = d-1
# todo.pop(d)
# j = -1
# g = 0
# for elem in todo:
#     j = j+1
#     g = g+1
#     print(g,"-",todo[j])
# a = [0]*5
# b = a*5
# print(b)
# a = int(input('Введите кол-во строк массива: '))
# b = int(input('Введите кол-во столбцов массива: '))
# c = []
# for i in range(a):
#     c.append([0]*b)
# print(c)
# # a = []
# # for i in range(5):
# #     a.append([0]*3)
# #     print(a)
# # a = [[1,2,3],[3,2,1],[5,2,1]]
# # b = int(input('Введите номер строки: '))
# # c = int(input('Введите номер столбца: '))
# # d = a[b][c]
# # print('Ваш искомый массив под строкой:',b,'\nИ под столбцом:',c,'\nВаш искомый эллемент:',d)
# for i in range(a):
#     for j in range(b):
#         print('Введите сначала желаемый столбец,а затем заполните элемент столбца желаемым значением')
#         c[i][j]=int(input())
# print(c)
# from curses.ascii import isupper
# from random import random, randint
# from tabnanny import check
# from urllib.parse import unquote_to_bytes
#
# a = []
# for i in range(7):
#     a.append(['']*3)
# print(a)
# # for i in range(21):
# #     g = input('Составить новый план на текущую неделю? \n-')
# #     if g == 'да':
# for k in range(7):
#     g = input('Составить новый план на текущую неделю? \n-')
#     if g == 'да':
#         c = int(input('Введите номер недели: '))
#         for j in range(3):
#             l = input('Составить новый план на текущий день? \n-')
#             if l == 'да':
#                 d = int(input('На какое время дня вы хотите запланировать дело? (8:00-12:00)-0,(12:00-17:00)-1,(17:00-21:00)-2: '))
#                 a[c][d] = input('Введите ваш план/дело: ')
#             else:
#                 break
#     else:
#         print("Хотите удалить какое нибудь запланированное дело?")
#         m = input()
#         if m=='да':
#             z = int(input('Введите день недели, дело которого хотите удалить: '))
#             print(a[z])
#             v = int(input('Введите время дня плана, которого хотите удалить: '))
#             a[z].pop(v)
#         else:
#             break
#         break
# print(a)
# # translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# # print(translator)
# # translator['dog']='собака'
# # print(translator.values())
# from lib2to3.btm_utils import token_labels
# from random import random
# from ctypes import c_int
# from io import klass
# from curses.ascii import islower
# from curses.ascii import isupper
#
# number_book={}
# for i in range(10000):
#     a = input("Хотите добавить нового пользователя в телефонную книгу? \n-")
#     if a=="да":
#         b = input("Введите Имя пользователя \n-")
#         c = input("Введите номер телефона пользователя \n-")
#         number_book[b]= c
#     else:
#         break
# print('Хотите добавить двух новых пользователей? \n-')
# f = input()
# if f == "да":
#     for j in range(1):
#         h = input("Введите Имя пользователя \n-")
#         z = input("Введите номер телефона пользователя \n-")
#         number_book[h] = z
# else:
#     break
# print("хотите поменять номер телефона вашего друга на новый?")
# l = input()
# if l == 'да':
#     o = input('Имя пользователя')
#     a[o]=input()
# print(number_book)
# print(number_book.keys())
# print(number_book.values())

# import random
# students = ['Алиса','Роман','София','Артём','Андрей']
# students.sort()
# classes = ['Математика','Русский язык','Биология','История']
# student_marks = {}
# for student in students:
#     student_marks[student]={}
#     for class_ in classes:
#         marks = [random.randint(1,5) for i in range (3)]
#         student_marks[student][class_]=marks
# for student in students:
#     print(f'''{student},{student_marks[student]}''')
#
# while True:
#     a = int(input('Введите номер команды: '))
#     if a == 1:
#         student = input('Введите имя ученика: ')
#         class_ = input('Введите предмет: ')
#         mark= int(input('Введите оценку: '))
#         if student in student_marks.keys() and class_ in student_marks[student].keys():
#             student_marks[student][class_].append(mark)
#             print(f'Для студента {student} была добавлена оценка {mark} по предмету {class_}')
#         else:
#             print('Неверные имя студента или название предмета')
#     elif a == 2:
#         for student in students:
#             print(student)
#             for class_ in classes:
#                 mark_sum = sum(student_marks[student][class_])
#                 mark_count = len(student_marks[student][class_])
#                 print(f'{class_} - {mark_sum // mark_count}')
#                 print()
#     elif a == 3:
#         for student in students:
#             print(student)
#             for class_ in classes:
#                 print(f'\t{class_} - {student_marks[student][class_]}')
#             print()
#     elif a == 4:
#         student_=input('Введите имя ученика чьи средние оценки вы хотите увидеть или выйдите из программы(exit): ')
#         if student_ == ('exit'):
#             break
#         else:
#             for class_ in classes:
#                     mark_sum = sum(student_marks[student_][class_])
#                     mark_count = len(student_marks[student_][class_])
#                     print(f'Средние оценки ученика {student_}')
#                     print(f'{class_} - {mark_sum // mark_count}')
#                     print()
#     elif a == 5:
#         student_ = input('Введите имя ученика чьи оценки вы хотите увидеть или выйдите из программы(exit): ')
#         if student_ == ('exit'):
#             break
#         else:
#             for class_ in classes:
#                 print(f'\t{class_} - {student_marks[student_][class_]}')
#                 print()
#     elif a == 6:
#
#     elif a == 7:
#         print('Выход из программы')
# #         break
# password = input()
# def check_password():
#     if len(password)>=8:
#         for elem in password:
#             if elem.isupper():
#                 for elem in password:
#                     if elem.isdigit():
#                         for elem in password:
#                             if elem.islower():
#                                 b = +2
#                                 return b
#                             else:
#                                 a =+1
#                     else:
#                         a=+1
#             else:
#                 a=+1
#     else:
#         a=+1
#         print('Длина пароля меньше 8 символов')
#     return a
# check_password()
# c = check_password()
# if c ==2:
#     print('Пароль подходит')
# else:
#     print('Пароль не подходит')

# def is_success_code(code):
#     if code >=200 and code <=299:
#         return True
#     else:
#         return False
#
# print(is_success_code(300))

# Код на валидность mail.

#
# def is_valid_email(mail):
#     if '@' in mail:
#         a = mail.find('@')
#         if '.' in mail:
#             b = mail.find('.')
#             if a>b:
#                 print('@ должен стоять раньше чем .')
#                 return False
#             else:
#                 if ' ' in mail:
#                     print('Не должно быть пробелов')
#                     return False
#                 else:
#                     return True
#         else:
#             print('нет специального знака .')
#             return False
#
#     else:
#         print('Нет специального знака @')
#         return False
#
# print(is_valid_email('Pozetuve03.@mailru'))

# длина не менее 8 символов;
# есть хотя бы одна заглавная буква;
# есть хотя бы одна строчная буква;
# есть хотя бы одна цифра.
# #
# def isvalid_password(password):
#     upper,lower,digit=False,False,False
#     if len(password)>=8:
#         for elem in password:
#             if elem.isupper():
#                 upper = True
#             elif elem.isdigit():
#                 digit = True
#             elif elem.islower():
#                 lower = True
#         if upper == False:
#             print('Пароль должен содержать минимум 1 заглавную букву')
#             return
#         elif lower == False:
#             print('Пароль должен содержать минимум 1 прописную букву')
#             return
#         elif digit == False:
#             print('Пароль должен содержать минимум 1 цифру')
#             return
#     else:
#         print('Пароль должен содержать не меньше 8 символов')
#     if (upper, lower, digit) == (True,True,True):
#         print('Пароль подходит')
#         return True
# a = input()
# isvalid_password(a)

# def calculate_average(*args):
#     a = 0
#     for elem in args:
#         a += elem
#     print(a)
#     b = a/len(args)
#     return b
# #
# print(calculate_average(1.2, 0.9, 1.3, 1.1, 1.7))
# # 1.24
# def sort_data(**kwargs):
#    return sorted(kwargs.items())
# print(sort_data(z = 1, y = 2, x = 3))
# people = [
#    {'name': 'Анна', 'age': 20},
#    {'name': 'Борис', 'age': 25},
#    {'name': 'Виктор', 'age': 19}
# ]
# sorted_people = sorted(people, key=lambda person:person['age'])
# print(sorted_people)
# strings = ["apple", "banana", "cherry", "date", "elderberry"]

# def sort_strings_by_last_char(strings):
#    a = sorted(strings,key=lambda word:word[-1])
#    return a
# print(sort_strings_by_last_char(['zebra', 'apple', 'banana']))


# def sort_users_by_activity(users):
#    a = []
#    a = sorted(users, key=lambda user:user[-1])
#    return a


# user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
# print(sort_users_by_activity(user_activity))

# def sort_users_by_activity(users):
#    for elem in users:
#       a =+1
#       b = 'user'+'a'
#       print(b)
# #    return user('')
# users = [1,2,3,4,5,6]
# for elem in users:
#    a =+1
#    c = 'user'
#    b = c + a
#    print(b)
# sales_data* = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
#
#
# def sales_stats(sales_data, revenue=False, quantity=False):
#    if revenue == True:
#    sales_data =
#       for elem in args:
#          a =+1
#       print(args)
#       print(a)
#       return
#
# print(sales_stats(sales_data, revenue=True))
# def recursive_func(n=0):
#    recursive_func(n + 1)
# recursive_func(5)
#
# def factorial(n):
#     c = 0
#     d = n
#     e = n
#     if n == 0:
#         a = 1
#         return a
#     else:
#         while c < d:
#             c +=1
#             e -=1
#             n = n*(e)
#             if e ==1:
#                 break
#             else:
#                 f=1
#     return n
# print(factorial(5))
#
# def factorial(n):
#    # Базовый случай
#    if n == 0:
#        return 1
#
#    # Рекурсивный случай
#    else:
#        return n * factorial(n -1)
#
# print(factorial(3))
#
# def factorial1(n):
#     a=0
#     if n == 0:
#        a = 1
#        return a
#     else:
#         print((n*factorial(n-1)))
#
# print(factorial1(5))
#
# a = 'r'
# b = 'a'
# c = a+b
# print(c)
#
# def binary_search(lst,a):
#     k = len(lst)
#     d = k//2
#     if lst[d] == a:
#         print('Поиск заверешен')
#         return True
#     elif lst[d]>a:
#         e = binary_search(lst[d-1:],a)
#         if e == a:
#             print('Поиск заверешен1')
#             return True
#         else:
#             g = 1
#             return g
#     elif lst[d]<a:
#         f = binary_search(lst[d+1:],a)
#         if f == a:
#             print('Поиск заверешен2')
#             return True
#         else:
#             g = 2
#             return g
#
# print(binary_search([1, 2, 3, 4, 5], 4))

# b = [1,2,3,4,5]
# k = len(b)
# print(k)

# url_generator = generate_urls("/product/", 1, 3)
# def generate_urls(url):
#     for url in url_generator:
#         yield (url)
#
# print(generate_urls())
#
# first_names = ["Alice", "Bob", "Charlie"]
#
# last_names = ["Smith", "Johnson", "Williams"]
# import random
# def generate_user_data(first_names,last_names,*args):
#     for i in first_names:
#         a = first_names[random]
#         for j in last_names:
#             b = last_names[random]
#             for x in args:
#                 c = args[random]
#
#     d = a+b+c
#
# first_names = ["Alice", "Bob", "Charlie"]
# last_names = ["Smith", "Johnson", "Williams"]
# age=[[12,13],[16,17],[20,21]]
# print(generate_user_data(first_names,last_names,age))
#
# map,zip,yield,filter,all,any

# 1-yield


# a = randint(1,100)
# print(a)
#

#
# def classic():
#     a = randint
# import time
# #
# tickets = []
# players1 = []
#
# def players(a,v):
#     print('заполняем список участников')
#     timing = time.time()
#     k = 'yes'
#     c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#          31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
#          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
#          85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#     for i in range(1000):
#         print('Напишите "ready" для старта')
#         d = input()
#         if d == 'ready':
#             print('Напишите Ваше имя')
#             g = input()
#             if g[0].isupper():
#                 v.append(g)
#                 print('Имя успешно зарегестрировано')
#                 k = 'yes'
#             else:
#                 print('Имя должно начинаться с заглавной буквы')
#                 k = 'no'
#             if k == 'yes':
#                 print('Напишите номер билета, которого хотите зарегистрировать за собой. Свободные билеты:', c)
#                 b = int(input())
#                 filtered_c = list(filter(lambda x: x==b,c))
#                 if time.time() - timing > 60.0:
#                     v.remove(v[-1])
#                     return('Время набора участников вышло')
#                 elif(filtered_c):
#                     a.append(b)
#                     c.remove(b)
#                     print('Новый участник зарегистрирован')
#                     print('Продолжаем набор участников')
#                 elif len(a)==100:
#                     return('Максимальное кол-во участников')
#                 elif b > 100:
#                     print('Некорректное название билета')
#                 else:
#                     print('Данный билет уже занят')
#             elif k == 'no':
#                 print('Попробуйте ещё раз')
#         else:
#             print('Некорректное значение')
#
# m = 0
# game_score = 'gamescoree'
# while True:
#         game_score=(game_score[:-1])
#         m += 1
#         game_score = game_score + str(m)
#         print(game_score)
#         players(players1,tickets)
#         print('Список участников и их билетов в', game_score)
#         game = (list(zip(players1, tickets)))
#         print(game)
#         # random_winner = random.randint(0,100)
#         random_winner = 1
#         for i in range(0,100):
#             if random_winner == game[i][0]:
#                 print('Номер выйгрышного билета:',random_winner,'\nПоздравляем игрок под именем:',game[i][1],'-выйграл')
#                 break
#             elif i > len(game):
#                 print('Номер выйгрышного билета:', random_winner, 'Победителя не было найдено!')
#             else:
#                 h = True


# def funcia():
#     name = 'dmitrii'
#     def func2():
#         print('hello world',name)
#     return func2
#
#
# b = funcia()
# b()

# def sr_ar():
#     numbers1 = []
#     def numbers(number):
#         numbers1.append(number)
#         a = sum(numbers1)/len(numbers1)
#         return a
#     return numbers
#
# r = sr_ar()
# print(r(10))
# print(r(20))
# a =sr_ar()
# print(a(10))
# print(a(20))
# f=sr_ar()
# print(f(30))
# print(f(50))

# def create_counter():
#     count=0
#
#     def counter(a):
#         nonlocal count
#         b = a
#         c = b**2
#         count += 1
#         print(f"функция вызвалась {count} раз,",f"{b} в квадрате =",c)
#         return create_counter()
#     return counter
#
# kvadrat = create_counter()
# kvadrat(4)
# kvadrat(5)
# kvadrat(6)

# def create_counter():
#     count=0
#     def counter1():
#         nonlocal count
#         count += 1
#         return count
#     return counter1
#
# counter = create_counter()
# print(counter())
# print(counter())
# print(counter())
#
# def create_unique_checker():
#     b = set()
#     d = []
#     def create(a):
#         b.add(a)
#         d.append(a)
#         print(b, d)
#         if len(d)>len(b):
#             d.remove(a)
#             return False
#         else:
#             return True
#     return create
#
# c = create_unique_checker()
# print(c(10))
# print(c(10))
# print(c(20))

# b = set()
# b.add(5)
# print(b)
# f = ['.',',','-','+',' ',')','(']
# def format_phone_number(number):
#     g = []
#     for i in range(len(number)):
#         a = list(filter(bool,number[i]))
#         for j in range(len(a)):
#             if number[i][j] in f:
#                 a.remove(number[i][j])
#         g.append(a)
#     print(g)
#
# phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']
#
# h = (format_phone_number(phone_numbers))
# print(h)
#
#
# def format_phone_number(number):
#     for i in range(len(number)):
#         return ''.join(filter(str.isdigit, number))
#
# phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']
#
# print(format_phone_number(phone_numbers))

phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']


# def format_phone_number(number):
#    return ''.join(filter(str.isdigit, number))
#
# formatted_numbers = list(map(format_phone_number, phone_numbers))
#
# print(format_phone_number(phone_numbers))
# print(formatted_numbers)

# def decorator(func):
#
#     def inner():
#         print('start decorator')
#         func()
#         print('finish decorator')
#
#     return inner
#
# def say():
#     print('hello world')
#
# d = decorator(say)
# print(d)
# d()
# say = decorator(say)
# say()

# def funcia(func):
#     name = 'dmitrii'
#     def func2():
#         print('hello world',name)
#     return func2
#
# def say2():
#     print('dmitrii')
# b = funcia(say2())
# b()

# def decorator(func):
#     def func3(*args,**kwargs):
#         print('hello world')
#         func(*args,**kwargs)
#         print('hello world')
#     return func3
#
# def says(name,surname):
#     print('hi', name,surname)
#
# def says1(name,surname):
#     print('by', name,surname)
#
#
# d = decorator(says)
# d('dmitrii','blinov')
#
#
# e = decorator(says1)
# e('dmitrii','blinov')

# def priv(func):
#     def priv1(*args,**kwargs):
#         print('hello world')
#         func(*args,**kwargs)
#         print('hello world')
#     return priv1
#
# def says3(name,surname):
#     print('hi', name,surname)
#
# says3 = priv(says3)
# says3('dmitrii','blinov')
# times = 1
#
# def retry_if_result_is_none(*args):
#     def result():
#         global times
#         times += 1
#         if times > 1:
#             print('None1')
#         else:
#             print('None')
#         funcia()
#     return result
#
#
# def funcia():
#     print('Целевая функция запустилась')
#
# # funcia()
# count=0
# # def create_counter():
# #     global count
# #     count += 1
# #     print (count)
# #
# # @create_counter
# # def func2():
# #     print('Функция запустилась')
# # #
# # # for i in range(5):
# # #     func2(2)
# # #
# # # def func3():
# # #     print('Функция запустилась')
# #
# # for i in range(5):
# #     create_counter()
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() -- start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        return res
    return wrapper


# @timeit
# def large_sum(n):
#     return sum(range(n))
#
# a = 321313
#
# print(large_sum(a))

# count=0
# def create_counter(func):
#     global count
#     count += 1
#     print (count)
#
#
# @create_counter
# # @timeit
# def func2():
#      return 2*2
#
#
# print(func2())

# def create_counter():
#     count=0
#     def counter1():
#         nonlocal count
#         count += 1
#         return count
#     return counter1
#
# counter = create_counter()
# print(counter())
# print(counter())
# print(counter())
# print(create_counter())


#
# def create_counter():
#     count=0
#     def counter1():
#         nonlocal count
#         count += 1
#         return count
#     return counter1
#
# print(create_counter())
#
# @timeit
# def func2():
#     return 2*2
#
# func2()



# @timeit
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# def create_counter(func):
#     count = 0
#     def counter1(*args,**kwargs):
#         func(*args,**kwargs)
#         nonlocal count
#         count += 1
#         print('Затрачено попыток',count)
#     return counter1
#
# # @create_counter
# def chisla(number):
#     print('Полученное число',number*2)
#
# chisla = create_counter(chisla)
#
# chisla(3)
# chisla(2)
# chisla(4)

# import datetime
#
# def calculate_age(birth_date: str) -> int:
#     a = datetime.date.today()
#     a = str(a)
#     a_int = [a.split('-')]
#     b = birth_date
#     b_int = [b.split('-')]
#     year_now = int(a_int[0][0])
#     month_now = int(a_int[0][1])
#     day_now = int(a_int[0][2])
#     year_birth= int(b_int[0][0])
#     month_birth =int(b_int[0][2])
#     day_birth = int(b_int[0][1])
#     age = year_now-year_birth
#     month = month_now-month_birth
#     day = day_now-day_birth
#     if month < 0:
#         age = age-1
#     elif month == 0 and day < 0:
#         age = age-1
#     return(age)
#
# print('Введите дату рождения в формате:''год-день-месяц''')
# a = input()
# b = a.split('-')
# if len(b) == 3:
#     if '-' in a:
#         print('Ваш возраст')
#         print(calculate_age(a),'год')
#     else:
#         print('Введите корректную дату рождения в формате:''год-месяц-день''(через дефис)')
# else:
#     print('Введите корректную дату рождения в формате:''год рождения-месяц рождения-день рождения')
#
# def filter_adults(users):
#     a = list(filter(lambda x: users[x]>=18,users))
#     m = []
#     for i in range(len(a)):
#         m.append(users[a[i]])
#
#     f = dict(zip(a,m))
#     print('Список совершеннолетних:','\n',f)
#
# users = {'Дмитрий':18,'Оля':17,'Евгений':19,'Олеся':17}
# filter_adults(users)
#
# def generate_username(first_name: str, last_name: str) -> str:
#     full_name = first_name + last_name
#     dictionary = {}
#     d = first_name[0].lower()
#     e = d+'.'+last_name.lower()
#     dictionary[full_name] = e
#     print('Ваше уникальное имя:',e)
#     print(dictionary)
#
# print('Введите ваше имя:')
# first_name = str(input())
# print('Введите вашу фамилию:')
# last_name = str(input())
# generate_username(first_name,last_name)
#
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
# a = 5
# print(id(5))
# b = 3+2
# print(id(b))
#
# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
#
# print(a)

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(id(list_id_after)==(id(list_id_before)))
#
# a = set("The Zen of Python")
# print(a)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# print(a_set)
# a_and_b = a_set.intersection(b_set)
#
# print(a_and_b)
# a = "foo"
# b = "bar"
#
# print(1 and a or b)
#
# a = 1
# b = 2
# if a and b!= 0 : # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#
#     print(a,b)
#
# def linear_solve(a, b):
#     return b / a
#
# print(linear_solve(0,1))

# a = ["это", "маленький", "текст", "обидно"]
# b = -1
# print(len(a))
# for elem in a:
#     print(len(elem))
#
# list(map(str.upper, a))

a = [[],[],[],
     [],[],[],
     [],[],[]]
a[0].append('o')
print(a)

s = '-----------------'
li = list(s)
li[5] = 'A'
result = ''.join(li)  # AABAAAAAАA
print(result)