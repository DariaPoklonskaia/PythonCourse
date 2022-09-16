#Ex1. Разбор дз2. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 0,56 -> 11

# numb = float(input()) #won't woork for negative
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

#Var2
# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

#var3. 
# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

#Ex2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

# num = int(input('inter number '))
# product = 1
# for i in range(1, num +1):
#     product *= i
#     print(product, end=' ')

#Ex3. #Ex3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

# n = int(input('inter number '))

# def sequence(n):
#     return[round(( 1 + 1/x )**x, 2) for x in range(1, n +1)]

# print(sequence(n))
# print('sum of sequence  = ', round(sum(sequence(n)),2))

#Ex4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# from random import randint
# n = int(input('Введите число N - '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n))
# print(numbers)

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "": #need to add check that s не больше индекса в списке. чтобы не выходило за пределы
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)] #обязательно линию перевести в текст, так как иначе она пока ка строчке воспринимается
# f.close()
# print(result)


#Ex5.  Реализуйте алгоритм перемешивания списка. 

# from random import randint

# any_list = [1, 2, 3, 4, 5, 6]

# for i in range(len(any_list)):
#     j = randint(0, len(any_list)-1)
#     any_list[i], any_list[j] = any_list[j], any_list[i]
# print(any_list)

#Ex6. Транслитирация вводимого текста
# lang = {'а': 'a',
# 'б': 'b',
# 'в': 'v',
# 'г': 'g',
# 'д': 'd',
# 'е': 'e',
# 'ё': 'e',
# 'ж': 'zh',
# 'з': 'z',
# 'и': 'i',
# 'й': 'y',
# 'к': 'k',
# 'л': 'l',
# 'м': 'm',
# 'н': 'n',
# 'о': 'o',
# 'п': 'p',
# 'р': 'r',
# 'с': 's',
# 'т': 't',
# 'у': 'u',
# 'ф': 'f',
# 'х': 'kh',
# 'ц': 'ts',
# 'ч': 'ch',
# 'ш': 'sh',
# 'щ': 'shch',
# 'ъ': '',
# 'ы': 'y',
# 'ь': '',
# 'э': 'e',
# 'ю': 'yu',
# 'я': 'ya',
# ' ': ' '
# }

# value = 'Мама мыла раму'
# result = ''

# for i in value:
#     result += lang[i.lower()]

# print(result)

#Var2.Транслитирация вводимого текста
# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

# start_index = ord('а') #ord это utf код, где каждый символ имеет свой код
# title = 'Переводим этот текст, сейчас!'


# slug = ""
# for s in title.lower():

#     if "а" <= s <= "я":
#         slug += t[ord(s) - ord('а')]
# # elif s == "ё":
# # slug = 'yo'
# # elif s in " !?;:.,":
# # slug = "-"
#     else:
#         slug += s

# # while slug.count('--'):
# # slug = slug.replace('--', '-')

# print(slug)

#Ex7. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел

numbers = str(input('enter numbers and use space as separator : '))
list1 = []

for i in numbers:
    if i != ' ':
        num = int(i)
        list1.append(num)
print(list1)

#Ex8. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python