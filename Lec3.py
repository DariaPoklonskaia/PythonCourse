# def f(x):
#     return x**2

# g = f
# print(f(4))
# print(g(4))
############################
# def calc1(x):
#     return x + 10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print (op(x))

# math(calc2, 10)
# math(calc1, 10)

###########################

# def sum(x, y):
#     return x+y

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)

# calc(mylt, 4, 5)

############################

# def sum(x, y):
#     return x+y

# f = sum # f = lambda q, w: q+w тоже что и функция выше, строчки 36-39, но с другими аргументами

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)

# calc(f, 4, 5)

####################

# sum = lambda x, y: x+y+1

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)

# calc(sum, 4, 5)

# #######################


# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)

# calc(lambda x, y: x+y+1, 4, 5)

####################### List comprehension #######
# list = []

# for i in range(1, 20):
#     if(i%2 == 0):
#         list.append(i)

# print(list) ##or

# list = [(i,i) for i in range(1, 21) if i%2 == 0]
# print(list)

# def f(x):
#     return x**3

# list1 = [f(i) for i in range(1, 21) if i%2 == 0]
# print(list1)

#######################
# f = open('fileTask.txt', 'w')
# while True:
#     s = input('Укажите число - ')
#     if s == "": 
#         break
#     f.write(s+"\n")
# f.close()

# list2 = []
# f = open('fileTask.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     if int(line) % 2 == 0:
#         list2.append(int(line))
# f.close()

# print(list2)


# list3 = [(i, i**2) for i in list2]

# print(list3)

####################### увеличим каждое число в списке на 10
# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x+10, li))

# print(li)

####################### функция map
# data = list(map(int,input().split())) # default separator is space. Вводим строку с числами, разделитель пробел. сразу преобразуем из строки в числа при помощи мэп. 
# print(data)

# data2 = map(int,'1 2 3 5 7'.split()) # один раз работается с итератором map, иначе нужно сохранять например в список

# for e in data2:
#     print(e)

    ####################### функция filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))

# print(res)

####################### из списка выбрать четные и выевсти кортеж числа и его квадрата

# data = '1 2 3 45 6 7'.split()

# res = map(int, data)

# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

####################### zip