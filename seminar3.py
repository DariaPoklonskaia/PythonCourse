#Ex1. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода - пустая строка.


# fname = input('file: ')

# f= open(fname, 'w')

# while True:
#     s=input('words')
#     if s=='':
#         break 
#     f.write(s+ '\n')
# f.close() 


#Ex2. В текстовом файле посчитать количество строк, а также для каждой отдельной 
# строки определить количество в ней символов и слов

# lines = 0

# listSymb = []
# listWords = []

# with open('file.txt') as file:
#     for line in file: 
#         lines +=1
#         symbols = len(line) 
#         listSymb.append(symbols)
#         words = 1
#         for s in line:
#             if s == ' ' :
#                 words += 1 #если пустая строка, то посчитает как одно слово... надо доработать если строка пустая \n
#         listWords.append(words)

# print(lines)
# print('words', listWords)
# print('symb', listSymb)

#Ex2. var2
# f = open('file.txt','r')
# countLines = 0
# countwordsInLines = []
# countCharsInLines = []
# for line in f:
#     countLines+=1
#     if line != '\n':
#         countwordsInLines.append(line.count(' ') + 1)
#     else:
#         countwordsInLines.append(0)
#     countCharsInLines.append(line.count('') -2)
# f.close()
# print(countLines)
# print(countwordsInLines)
# print(countCharsInLines)



#Ex3. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию 
# biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет 
# созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# k1=22, k2=31, k3=11, k4=91


# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)

# my_dict = {'first_one': 'we ca do it'}

# biggest_dict(k2=31, k3=11)

# print(my_dict)



#Ex4. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут 
# соответствовать правилам задания ключей в словарях
# Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

# def to_dict(lst):
#     return {element: element for element in lst} #element: (это значение) element (ключ) for element in lst (перебтраем все элементы списка)

# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

# Ex5. 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

# list1 = ['asdf', '34d', 'asdf', '123df'] #так ищет только целые слова из списка

# x = input('Inter number to find: ')

# if x in list1:
#     print('yes')
# else:
#     print('no')


# Ex5. var2. косяк - перебирает все символы в списке по одному. 

# list1 = ['asdf', '34d', 'asdf', '123df']

# x = input('Inter number to find: ')
# count = 0
# for i in range(len(list1)):
#     text = list1[i]
# #     for j in range(len(text)): #косяк так как перебирает все символы в списке по одному и можно найти цифры только.
# #         if text[j] == x:
# #             count+=1
# # print(count > 0)
#     if x in text:
#         count+=1
# print(count > 0)


# Ex6. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, 
# что её нет- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

spisok = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_str = 'qwe'
if spisok.count(find_str) < 2:
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:
    spisok1 = spisok[spisok.index(find_str) + 1:] # отрезаем первой вхождение
    print(spisok1)
    print(spisok1.index(find_str) + (len(spisok) - len(spisok1))) # ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали
