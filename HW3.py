#ex1/ Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# numbers = [2, 3, 5, 9, 3, 7, 1]

# sum = 0
# i = 1
# while i < len(numbers):
#     sum += numbers[i]
#     i += 2
# print(sum)


# Ex2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];

# numbers = [2, 3, 4, 5, 6]
# resultList = []
# i = 0
# j = len(numbers) - 1

# while i <= j:
#     product = numbers[i] * numbers[j]
#     i += 1
#     j = len(numbers) - 1 - i
#     resultList.append(product)

# print(resultList)

# Ex3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# floatNumbers = [-1.1, -2.2024, 3.105, 5, 10.0001]

# newlist = [] 
# for i in range(len(floatNumbers)):
#     if floatNumbers[i] < 0:
#         floatNumbers[i] = -1 * floatNumbers[i]
#     fractionPart = floatNumbers[i] % 1
#     count = 0
#     while floatNumbers[i] % 1 > 0:
#         floatNumbers[i]*=10
#         count += 1
#     fractionPart = round(fractionPart, count)
#     newlist.append(fractionPart)

# print(newlist)

# def findMax(anylist):
#     max = anylist[0]
#     for i in range(1, len(anylist)):
#         if anylist[i] > max:
#             max = anylist[i]
#     return max

# def findMin(anyanylist):
#     min = anyanylist[0]
#     for i in range(1, len(anyanylist)):
#         if anyanylist[i] != 0:
#             if anyanylist[i] < min:
#                 min = anyanylist[i]
#     return min


# diff = findMax(newlist) - findMin(newlist)

# roundMax = len(str(findMax(newlist))) - 2
# roundMin = len(str(findMin(newlist))) - 2

# if roundMax > roundMin:
#     diff = round(diff, roundMax)
# else:
#     diff = round(diff, roundMin)

# print(diff)


# Ex4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. 45 -> 101101


# n_10 = int(input('введите десятичное число: '))

# newSyst = 2
# N_new = 0

# if n_10 >= newSyst:
#     i = 0
#     quotient = n_10
#     while quotient != 0:
#         quotient = n_10//newSyst
#         residual = n_10 - quotient*newSyst
#         N_new = N_new + residual*(10**(i))
#         i += 1
#         n_10 = quotient
# else:
#     N_new = n_10

# print(N_new)

# Ex5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов



num = int(input('введите натуральное число: '))


def fib(n):
    if n == 0:
        return 0
    elif n in (1,2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

def negaFib(k):
    if k == 1:
        return 1
    elif k == 2:
        return -1
    else:
        return negaFib(k-2) - negaFib(k-1)


list = []
listNega = []

for e in range(0, num + 1):
    list.append(fib(e))


for i in range(1, num + 1):
    listNega.append(negaFib(i))


def revertlist(list1):
    i = 0
    j = len(list1) - 1
    while i <= j:
        temp = list1[i]
        list1[i] = list1[j]
        list1[j] = temp
        i +=1
        j = len(list1) - 1 - i
    return list1  

        
listresult = revertlist(listNega) + list

print(listresult)