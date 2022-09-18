#Ex1. Вычислить число c заданной точностью d. 10^{-1} ≤ d ≤10^{-10}
# pi = 3.1415926535

# d = input('Введите желаемую точность для числа пи: ')

# for el in str(d):
#     if el == '.':
#         d = d[d.find('.'):]
#         accuracy = len(d) - 1

# print(d)
# print(accuracy)

# print((int(pi*(10**accuracy)))/(10**accuracy))

#Ex2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

# number = int(input('введите натуральное число: '))
# listRes = []

# for i in range(1, number + 1):
#     if number % i == 0:
#         listRes.append(i)

# print(listRes)

#Ex3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

# list1 = [1, 2, 3, 4, 5, 1, 5]
# result = []

# for i in list1:
#     if i not in result:
#         result.append(i)

# print(result)

#Ex3.Var2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

# list1 = [1, 2, 3, 4, 5, 1, 5]
# result = list(set(list1))
# print(result)

#Ex4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# from random import randint


# powerK = int(input('Задайте натуральную степень k: '))

# coeff = []

# def Coefficient(k):
#     for i in range(powerK + 1):
#         num = randint(0, 100)
#         coeff.append(num)
#     return coeff
    
# coeff = Coefficient(powerK)
# print(coeff)

# f = open('coefficients.txt', 'w')
# for i in range(0, powerK + 1):
#     a = str(coeff[i])
#     b = '^' + str(powerK)
#     if powerK == 0:
#         f.write(a)
#     else:
#         f.write(a + 'x' + b + ' + ')
#     powerK = powerK-1
    
# f.close() #можно еще добавиь условие если коэффициент равен нулю

#Ex5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

