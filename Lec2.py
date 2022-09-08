#Work with files
# colors = ['red', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) #no separators 
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# exit() позволяет не запускать код, который написан далее

#mode a - will create new; допишет если уже есть данные redblueredblueredblue
#mode w - перепишет полностью все заново. Было в файле redblueredblueredblue, станет redblue

#with open('file.txt', 'w') as data: 
    # data.write('line 1\n')
    # data.write('line 2\n') no need to close file in this method

    #________________
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line) #считывается = напечатается в терминале
# data.close()

# все данные в файлах хранятся как строки, если надо работать как с числами, то необходимо предварительно выполнить конвертацию.

###########################################

#import file_name as fn # можно задать сокращенное имя при помощи функции as и далее уже юзать сокращенное имя. 

#print(fn.function_name(x)) запуск функции из файла

####################################

# def new_string(symbol, count = 3): # по умочанию каунт будет равен 3, если функция вызывается без этого аргумента
#     return symbol*count

# print(new_string(4)) 12 тип распознается в момент вызова функции
# print(new_string(!, 2)) !!
