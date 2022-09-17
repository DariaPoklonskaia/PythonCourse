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