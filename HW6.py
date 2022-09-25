# Ex1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# data = [1, 2, 3, 5, 1, 5, 3, 10] 
# result = []

# for el in data: 
#     if data.count(el) ==1:
#         result.append(el)
# print(result)

# Ex2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. Передел при помощи функции filter

# data = [1, 2, 3, 5, 1, 5, 3, 10] 
# result = list(filter(lambda x: data.count(x)==1 , data))

# print(result)

# Ex3. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.N = 4, тогда [ 1, 2, 6, 24 ]
# через list comprehension

# def f(x):
#     if x==1:
#         return 1
#     else: 
#         return x*f(x-1)
 
# number = int(input('Inter number: '))

# list1 = [f(i) for i in range(1, number+1)]

# print(list1)

#Ex4. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 0,56 -> 11

# s= input('inter number: ')
# lst = [int(x) for x in s if x.isdigit()]

# sum = 0
# for i in lst:
#     sum = sum + i
# print(sum)


