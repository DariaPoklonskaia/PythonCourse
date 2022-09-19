# import random
# def x(b=None):
#     if b is None:
#         b =  random.randint(1, 10)

#     a = b + 1
#     print(a)

# x_random1 = x()
# x_random1 = x()


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

#EX4 From HW3. из десятичного в двоичную.

# a=int(input('Введите число: '))
# b=bin(a)
# print(b[2:]) #[2:] убирает первые два символа

#var2. 
# N = int(input('Ведение число: '))
# ost = ''
# while N > 0:
#     ost = str(N%2) + ost #интересно новое прибалвяется вилдимо слева, а старое остается справа. если поменять местами слагаемые, то булет другой результат
#     N = N // 2

# print(ost)

#EX5 From HW3/ Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

# N= int(input('Ведение число: '))
# list = []
# list.append(0)
# list.append(1)
# list.insert(0, -1)

# print(list)

# def Fibonacci(n):
#     index = -1
#     for i in range(2, n + 1):
#         list.append(list[i*2 - 2] + list[i*2 - 3])
#         list.insert(0, (abs(list[0])+ abs(list[1])) * index)
#         index = index *-1
#     print(list)

# Fibonacci(N)

#######

# a = int(input('Enter the number: '))
# print(a)
# negofibonacci = [1,-1]
# fibonacci = [1,1]

# for i in range(2,a):
#     list = fibonacci[i-1]+fibonacci[i-2]
#     fibonacci.append(list)
#     list_nego = negofibonacci[i-2] - negofibonacci[i-1]
#     negofibonacci.append(list_nego)

# negofibonacci.reverse() #переворот списка!
# negofibonacci.append(0) # добавление  в позицию 0

# print(f' for a = {a} =>{negofibonacci+fibonacci}')

#########

# fib = int(input('5# введите число for fib = '))
# res_5 = []
# for i in range(fib+1):
#     if i==0:
#         res_5.append(i)
#     elif i==1:
#         res_5.append(i)
#         res_5.insert(0, i)
#     else:
#         res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
#         res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
# print(res_5)

#EX3 From HW3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

# list = [1.1, 1.2, 3.1, 10.01]
# mix_list = []

# for i in list:
#     mix_list.append(round(i-int(i), 2)) #округлять надо до длины числа. 

# print(list, end=' => ')
# print(max(mix_list) - min(mix_list))

#EX1. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае

# contains = lambda s, sample='ra': sample in s
# s = input()
# print(contains(s))

#EX2. НОД
# a = 27
# b = 21

# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)

#EX2. НОД. var2
# a = 27
# b = 21

# while b!=0:
#     a, b = b, a % b

# print(a)

#EX3. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

# n = open('numbers.txt', 'r')
# lst = [int(i) for i in n.readline().split()]
# for i in range(1, len(lst)):
#     if lst[i] - lst[i-1] > 1:
#         lst.insert(i, (lst[i] - 1))
# n.close()

# print(lst)

# если у функции f(x)  в return записано сразу две переменных return value1, value2. то далее можно писать так  при обращении к методу a, b = f(x, y)

#EX4. Напишите программу, удаляющую из текста все слова, содержащие "абв"

with open("words.txt", "r") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "abc" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(sentence)