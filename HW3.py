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


floatNumbers = [1.1, 2.2024, 3.105, 5, 10.0001]

newlist = [] 
for i in range(len(floatNumbers)):
    fractionPart = floatNumbers[i] % 1
    count = 0
    while floatNumbers[i] % 1 > 0:
        floatNumbers[i]*=10
        count += 1
    fractionPart = round(fractionPart, count)
    newlist.append(fractionPart)

print(newlist)

def findMax(anylist):
    max = anylist[0]
    for i in range(1, len(anylist)):
        if anylist[i] > max:
            max = anylist[i]
    return max

def findMin(anyanylist):
    min = anyanylist[0]
    for i in range(1, len(anyanylist)):
        if anyanylist[i] != 0:
            if anyanylist[i] < min:
                min = anyanylist[i]
    return min


diff = findMax(newlist) - findMin(newlist)

roundMax = len(str(findMax(newlist))) - 2
roundMin = len(str(findMin(newlist))) - 2

if roundMax > roundMin:
    diff = round(diff, roundMax)
else:
    diff = round(diff, roundMin)

print(diff)
