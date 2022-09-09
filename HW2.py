#Ex1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 0,56 -> 11

# number = float(input('Inter number: '))

# after_point = str(number)

# for i in range (len(after_point)):
#     after_point = after_point[after_point.find('.'):]

# print(after_point)
# print(len(after_point))

# number = number * (10 ** (len(after_point) - 1))

# print(number)

# def SumOfDigits(num):
#     sum = 0
#     while num != 0:
#             sum = sum + int(num%10)
#             num = num/10

#     return sum

# print(SumOfDigits(number))

#Ex2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N


# number = int(input('Inter number: '))

# list1 = []
# product = 1

# for i in range(1, number+1):
#     list1.append(product)
#     product = product * (i+1)
    
# print(list1)

#Ex3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

# number = int(input('Inter number of sequence members: '))
# list1 = []
# sum = 0

# for n in range(1, number+1):
#     member = ( 1 + (1/n) )**n
#     sum = sum + member
#     list1.append(member)

# print(list1)
# print(sum)

#Ex4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].

# from random import randint

# number = int(input('Inter number of elements in list: '))
# list1 = []

# for i in range (1, number + 1):
#     element = randint(number*-1, number)
#     list1.append(element)

# print(list1)

#Ex5. Реализуйте алгоритм перемешивания списка.

# import random
 
# y = [1, 2, 3, 4]
# random.shuffle(y)
 
# print(y)

#Ex5. Var2. Реализуйте алгоритм перемешивания списка. 
from random import randint

any_list = [1, 2, 3, 4, 5, 6]

for i in range(len(any_list)):
    j = randint(0, len(any_list))
    temp = any_list[i]
    any_list[i] = any_list[j]
    any_list[j] = temp

print(any_list)

