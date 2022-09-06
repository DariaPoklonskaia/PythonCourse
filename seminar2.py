#Ex1. дана строка текста, состоящая из букв руссского алфавита. О и Р. Буква - О - соответствует выпаданию Орла. буква Р - Решки. Напишите программу, 
# которая подсчитывает наибольшее количество подряд Решек

# print('Input text that consist of Р and О: ')
# text = input()

# count = 0
# temp = 0

# for x in range(0, len(text)):
#     if (text[x] == 'Р' or text[x] == 'р'):
#         count += 1
#         temp = count
#     else:
#         count = 0

# print(temp)

#Ex1. Var2 

# seqeanceOR = input()
# t = 0 
# while 'R'*(t+1) in seqeanceOR:
#     t+=1

# print(t)


#Ex2. Найти в последовательности цифр и букв слово anton. не обязательно это должно быть подряд. Вывести номер холодильника. 
# нумерация начинается с 1. 

# fridgesList = ['antonHGFDD', '1a2n3t4o5n', 'lkjhdfsdhyf', 'qweandton', 'ntona']

# for x in range(0, len(fridgesList)):
#     if 'a' in fridgesList[x]:
#         fridgesList[x] = fridgesList[x][fridgesList[x].find('a'):] # обрезаем текст который был до нахождения буквы а
#         if 'n' in fridgesList[x]:
#             fridgesList[x] = fridgesList[x][fridgesList[x].find('n'):]
#             if 't' in fridgesList[x]:
#                 fridgesList[x] = fridgesList[x][fridgesList[x].find('t'):]
#                 if 'o' in fridgesList[x]:
#                     fridgesList[x] = fridgesList[x][fridgesList[x].find('o'):]
#                     if 'n' in fridgesList[x]:
#                         print(x +1)


#Ex2. var 2

# n = int(input()) #вводим число холодильников
# list1 = []  #пустой список 

# for i in range(n):   # запускаем цикл, в началн которого вводим название холодильника
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):] # обрезаем текст который был до нахождения буквы а, далее поиск по оставшемуся тексту
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                             list1.append(i + 1) # заносим в пустой список номера нужных холодильников

# print(*list1)


#Ex3. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('input number of members in sequence: '))

# for i in range(n):
#     print((-3)**i, end = ' ')

# Ex4. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.

# text1 = input('input text1: ')
# text2 = input('input text2: ')
# count = 0

# while text1 in text2: #???? infinite cycle for some reason ??? 
#     count +=1
#     text2 = text2[text2.find(text1):]
#     print(text2)

# print(count) 


# Ex4. Var2. working for case fffaaafff and fff (starts from text2)
# text1 = input()
# text2 = input()

# if text1 > text2:
#     print(text1.count(text2))
# else:
#     print(text2.count(text1))

#Ex4. Var3. НЕВЕРНО ТОЖЕ

a = 'pyt'
b = 'pythonpythonpyt'

count = 0

for i in range(0, len(b) - len(a)): #
    if b[i:i + len(a)] == a:
        count +=1

print(count)
