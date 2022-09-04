# Задача 1 Напишите программу, которая принимает на вход два числа и проверяет является ли одно число квадратом другого. 

#
#a = int(input('Input first number'))

#print('Введите второе число')
#b = int(input())

#print(a**2 == b or b**2 == a)

#
# задача 2. Напишите программу которая на вход принимает 5 чисел и находит максимальное 
# num = [int(i) for i in input().split()] такой ввод может быть чере3 пробел сколько надо чисел 1 4 6 8 9 
# mlist = list(map(int, input().split()[:n])) после сплит можно записать количество элементов для ввода через [:n]

#print('Введите первое число')
#a1 = int(input())

#print('Введите второе число')
#a2 = int(input())

#print('Введите 3 число')
#a3 = int(input())

#print('Введите 4 число')
#a4 = int(input())

#print('Введите 5 число')
#a5 = int(input())

#numbers = [a1, a2, a3, a4, a5]

#print(numbers)


#max = numbers[0]


#for i in range(len(numbers)):
    #if (numbers[i] > max):
        #max = numbers[i]



#print(max)

#3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#print('Input number')
#num = int(input())

#r = range(-num, num +1)
#for i in r:
    #print(i, end=', ')

#4Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.  6,78 -> 7

#print('введите дробь')
#num = float(input())
#num2 = num *10

#if int(num2%10) == 0:
    #print('no')
#else:
    #print(int(num2%10))


#5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

print('введите число')
num = int(input())

if (num%5 == 0 and num%10 == 0 or num%15 == 0) and num%30 != 0 :
    print('good')
else:
    print('not good')

