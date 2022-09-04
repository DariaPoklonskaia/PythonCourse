#Ex1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным 

# day = int(input('inter day of the week from 1 to 7: '))

# if day > 5 and day <8:
#     print('weekand')
# elif day > 0 and day <= 5:
#     print ('not weekand')
# else:
#     print ('There are only 7 days in a week, enter 1-7')

#Ex2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикатов. 


for x in range(0, 2):
    for y in range (0,2):
        for z in range (0,2):
            print(x, y, z, not(x or y or z) == (not x) or (not y) or (not z))
            


# Ex3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('inter non-zero X coordinate: '))
# y = int(input('inter non-zero Y coordinate: '))

# def f(coordX, coordY):
#     if coordX > 0 and coordY > 0:
#         return '1'
#     elif coordX < 0 and coordY > 0:
#         return '2'
#     elif coordX < 0 and coordY < 0:
#         return '3'
#     elif coordX > 0 and coordY < 0:
#         return '4'
#     else:
#         return 'Enter non-zero coordinates'

# print(f(x,y))

# Ex4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

# QuarterNum = int(input('inter integer quarter number from 1 to 4: '))

# def FindQuarterRange(number):
#     if number == 1:
#         return ' X > 0 and Y >0'
#     elif number == 2:
#         return ' X < 0 and Y >0'
#     elif number == 3:
#         return 'X < 0 and Y < 0'
#     elif number == 4:
#         return 'X > 0 and Y < 0'
#     else:
#         return 'there are  4 quarters, inter integer from 1 to 4'

# print(FindQuarterRange(QuarterNum))

#Ex5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

# user_x1 = int(input('inter x coordinate first point: '))
# user_y1 = int(input('inter y coordinate first point: '))

# user_x2 = int(input('inter x coordinate second point: '))
# user_y2 = int(input('inter y coordinate second point: '))


# def FindDistance(x1, y1, x2, y2):
#     distance = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
#     return int(distance*100)/100

# print(FindDistance(user_x1, user_y1, user_x2, user_y2))

