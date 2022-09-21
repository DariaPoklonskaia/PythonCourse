#Ex1.Напишите программу, удаляющую из текста все слова, содержащие ""абв""



# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "abc" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)

#Ex2.Создайте программу для игры с конфетами человек против человека. Человек против человека. Жеребьевка.
# from random import randint

# Qcandy = 2021
# m = 28


# def WhoTakesLast(Q, step):
#     i = randint(1, 2)
#     j = 2
#     if i == j:
#         j = 1
#     while Q > 0:
#         winner = ""
#         if Q > 0 and Q <= step:
#             user1 = Q
#         else:
#             user1 = randint(1, step)
#         Q = Q - user1
#         print(Q , i, end = ' ')
#         if Q == 0:
#             winner = "Игрок" + str(i)
#         if Q > 0 and Q <= step:
#             user2 = Q
#         else:
#             user2 = randint(1, step)
#         Q = Q - user2
#         print(Q, j, end = ' ')
#         if Q == 0:
#             winner = "Выиграл игрок" + str(j)

#     return winner

# print(WhoTakesLast(Qcandy, m))

#Ex2б.Создайте программу для игры с конфетами человек против человека. Подумайте как наделить бота ""интеллектом"". Жеребьевка.

# from random import randint

# Qcandy = 2021
# m = 28


# def WhoTakesLast(Q, step):
#     winner = ""
#     i = randint(1, 2)
#     print(i)
#     while Q > 0:
#         if i == 1:                     #первый ход у человека
#             if Q <= step:
#                 user1 = Q
#             else:
#                 user1 = randint(1, step)
#             Q = Q - user1
#             print(Q, "игрок1", end = ' ')
#             if Q == 0:
#                 winner = "Игрок1"
            
            
#             bot = Q % (step + 1)
#             if bot == 0:
#                 bot = randint(1, step)
#             Q = Q - bot
#             print(Q, end = ' ')
#             if Q == 0:
#                 winner = "Выиграл bot"

#         else:                        #первый ход у бота
#             bot = Q % (step + 1)
#             Q = Q - bot
#             print(Q, end = ' ')
#             if Q == 0:
#                 winner = "Выиграл bot"

#             user1 = randint(1, step)
#             Q = Q - user1
#             print(Q, end = ' ')
#             if Q == 0:
#                 winner = "Игрок1"
#     return winner

# print(WhoTakesLast(Qcandy, m))

#Ex3. Крестики-нолики. Simple version

from itertools import count


XO = [['+', '+', '+' ],['+', '+', '+'],['+', '+', '+'] ]

for i in range(len(XO)):
    for j in range(len(XO[i])):
        print(XO[i][j], end=' ')
    print()


def PlayXO():
    count = 0
    while True:
        if count%2 == 0:
            sign = 'X'
        else:
            sign = '0'
        print("player" + sign)
        a =  int(input('Введите строку: ')) 
        if a == -1:
            break
        b = int(input('Введите столбец: '))
        XO[a][b] = sign

        for i in range(len(XO)):
            for j in range(len(XO[i])):
                print(XO[i][j], end=' ')
            print()

        count += 1

        
        # for i in range(len(XO)):
        #     if XO[i][0] == XO[i][1] == XO[i][2] == "X" or "0":
        #         print("you win")
        #         break 
        # for j in range(len(XO[i])):
        #     if XO[0][j] == XO[1][j] == XO[2][j] == "X" or "0":
        #         print("you win")
        #         break
        # if XO[0,0] == XO[1, 1] == XO[2, 2] == "X" or "0":
        #    print("you win")
        #    break 

        # if XO[0,2] == XO[1, 1] == XO[2, 0] == "X" or "0":
        #    print("you win")
        #    break 

PlayXO()





    