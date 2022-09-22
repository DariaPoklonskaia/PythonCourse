#ex1. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел


# data = list(map(int, input('input numbers: ').split()))
# print(data)
# data = list(filter(lambda x: 9 < abs(x) < 100, data)) #abs модуль

# print(data)

#Ex1 from HW4. Вычислить число c заданной точностью d. 10^{-1} ≤ d ≤10^{-10}

# import math
# d = input('Введите число d указывающее степень округления числа pi ')
# d = d[2:len(d)] #убираем два первых символа 0.
# print(round(math.pi,len(d)))

#Ex1 from HW4. Вариант 2. считается число пи по формуле, и округление делается
# a = int(input('введите нужную точность 1#= '))
# pi_target = 0
# for i in range(1, 1000000):
#     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
# print(str(pi_target)[:a + 2])

#Ex2 from HW4.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
# n = int(input("Введите число N: "))
# i = 2
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2  #делим число на 2 пока делится. может быть повторение простого множителя. 
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")


#Ex3 from HW4. 
# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return list(set(nums)) #set выбирает уникальные элементы

# numbers = '1 1 2 2 3 455 66 66 2 1'
# print(elements(numbers))

#Ex4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}') # [хорошая запись как совместить формат числа и строки]
# flag = randint(0, 1)
# if flag == 1:
#     ans.append('+')
# elif flag == 0:
#     ans.append('-')
# k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans)) #соединенные элементы списка записываем черех пробел
# fout.close()

#Ex5 from HW4.сложение многочленов. здесь принимается что они имеют одинаковые степени. 
# import random
# def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
#     if b > 0:
#         res += '+' + str(b) + '*x'
#     if c > 0:
#         res += '+' + str(c)
#     return f'{a}*x^2' + res


# def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
#     if b > 0:
#         res += '+' + str(b) + '*x'
#     if c > 0:
#         res += '+' + str(c)
#     return f'{a}*x^2' + res

# f = open('dz40.txt', 'w')
# f.write(nmnogochlen1())
# print(nmnogochlen1())
# f.close()

# f = open('dz41.txt', 'w')
# f.write(nmnogochlen2())
# print(nmnogochlen2())
# f.close()

# f = open('dz40.txt', 'r')
# list_5 = str(f.readline()).split('x')
# c1 = b1 = a1 = 0
# if len(list_5) == 3:
#     c1 = list_5[2][1:]
# if len(list_5) >= 2:
#     b1 = list_5[1][3:-1]
# a1 = list_5[0][:-1]
# f.close()

# f = open('dz41.txt', 'r')
# list_51 = str(f.readline()).split('x')
# c2 = b2 = a2 = 0
# if len(list_51) == 3:
#     c2 = list_51[2][1:]
# if len(list_51) >= 2:
#     b2 = list_51[1][3:-1]
# a2 = list_51[0][:-1]
# f.close()

# f = open('dz42.txt', 'w')
# f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# f.close()

#Ex5 from HW4_var2. 
# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close

#Ex2. Дан список, вывести отдельно буквы и цифры 

# lst = ( "a", 'b', '2', '3' ,'c')
# numbers = list(filter(lambda x: x.isdigit(), lst))
# words = list(filter(lambda x: x.isalpha(), lst))
# print(*words) # распаковывается в массив если есть *, работает для функции принта
# print(*filter(lambda x: x.isdigit(), lst)) # распаковывается в массив если есть *, работает для функции принта

#Ex3.Преобразовать набора списков users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7] salary = [111,222,333]
# в другой набор ['user1', 4, 111] ['user2', 5, 222] ['user3', 9, 333]
# и потом вернуть в исходное состояние ['user1', 'user2', 'user3'] [4, 5, 9] [111, 222, 333]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# result = list(zip(users, ids, salary))
# print(*result)

#Ex3. Var from Sergey. дважды пройти зипом, и будет обратный результат, все вернется как было.

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))

# print(a,b,c, sep="\n")

#Ex4. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.1+2*3 => 7; Добавьте возможность использования скобок, меняющих приоритет операций

# expression = input('input: ')
# print(eval(expression)) решение при помощи библиотеки. My attemp

# expression = '1+2*3+4'

# data = list(filter(lambda x: x.isdigit(), expression))
# signs = list(filter(lambda x: not x.isdigit(), expression))
# print(data)
# print(signs)

# data = list(map(int, data))
# result = 0

# for i in range(len(signs)):
#     if signs[i] == "*":
#         result = result + data[i]*data[i+1]

# for i in range(len(signs)):
#     if signs[i] == "/":
#         result = result + data[i]*data[i+1]

# for i in range(len(signs)):
#     if signs[i] == "+":
#         result = result + data[i]+data[i+1]

# for i in range(len(signs)):
#     if signs[i] == "-":
#         result = result + data[i]+data[i+1]

# print(result)

#Ex4. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.1+2*3 => 7; Добавьте возможность использования скобок, меняющих приоритет операций

def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        elif symbol in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result

def calculate(lst: list) -> float:
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

def brackets(lst:list) -> list:
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calculate(lst[opening + 1:closing])] + lst[closing + 1:]
return lst


s = "(1+1)+20+2*50-2/2+(5+5)+10-(1+1)"
result = parse(s)
print(result)
result = brackets(result)
print(result)
print(calculate(result))