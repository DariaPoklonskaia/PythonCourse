# import random
# def x(b=None):
#     if b is None:
#         b =  random.randint(1, 10)

#     a = b + 1
#     print(a)

# x_random1 = x()
# x_random1 = x()

#EX1. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае


#EX1 From HW3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2])) # можно делать перебор списка специальным образом list [1:5:2] - начальный индекс:конечный индекс:шаг; [1::2] начальный индекс::шаг

#range(stop); range(start, stop); range(start, stop, step)
#list[::-1] - перебор списка с конца.  
# сделать копию списка l = l1[:]

#EX3 From HW3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

# list1 = [1.1, 1.2, 3.105, 5, 10.01] #неуневерсальное решение совсем, так как для двух знаков после запятой только. 
# list2 = []
# for i in range(len(list1)):
#     a = round(list1[i]*10 % 10, 2)
# if a > 0:
#     list2.append(a)
# b = round(float((max(list2)-min(list2))*10/100), 2)
# print(b)

#EX4 From HW4. из десятичного в двоичную.

# a=int(input('Введите число: '))
# b=bin(a)
# print(b[2:])

#var2. 
N = int(input('Ведение число: '))
ost = ''
while 
    ost = str(N%2) + ost
    N // 2

print(ost)