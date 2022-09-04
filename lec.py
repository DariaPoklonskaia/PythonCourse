# print('hello world')

a = 123
b = 1.23

print(a)
print (b)

value = None

value = 12456
print(value)
# print(type(value))

s = "hello ' world"
p = ' qwe " jhg '
print(s)
print(p)

print (s,p)
print (s, ' - ', p)

print ('{} - {} - {}'.format(a, b, s)) # format
print (f'{a} - {b} - {s}'.format(a, b, s)) #interpolation

print ('{1} - {2} - {0}'.format(a, b, s)) # format with changing order

f = True
print(f)

list = [1, 2]

list2 = ['dfg', 'dfgdf']
print(list)

print(list2)

print('input a')
a = input() #ввод в формате строки
print('input b')
b = input()
print('{} {}'.format(a,b))

print('input a')
a = int(input()) #ввод в формате числа или float(input()) в формате вещественных