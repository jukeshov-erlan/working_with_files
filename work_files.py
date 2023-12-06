'''
ФАЙЛЫ. РАБОТА С ФАЙЛАМИ. JSON, МОДУЛИ И ПАКЕТЫ
'''

# open('путь до файла', 'режим') функция, позволяющая открывать файлы и работать с ними

# file = open('test.txt')
# print(file)

'''                                     ===============РЕЖИМЫ============='''
# 1. 'r' (read) - открывает файл в режиме чтения. Это режим по умолчанию. Если файл не существует, то ошибка

# file = open('test.txt', 'r')
# data = file.read()
# print(data)

# 2. 'w' (write) - открывает файл в режиме записи. Если передать не существующий, то создаст его.
# Перезаписывет файл

# file = open('test2.txt', 'w')
# file.write('hello world')

# 3. 'a' (append) - открывает файл для добавления. Все новое будет обновляться в конец. Если такого файла нет, то создаст его

# file = open('test2.txt', 'a')
# file.write('hello world ')

# 4. 'x' (exclusive) - создает уникальные файлы. Будет ошибка, если передать существующий файл. Работает только один раз

# file = open('test66.txt', 'x')
# file.read()

# 5. 't' (text) - Открывает файл в текстовом виде Режим по умолчанию

# 6. 'b' (binary) - Открывает файл в бинарном виде.

# rb - чтение в бинарном виде
# wb - запист в бинарном виде
# ab - дозапись в бинарном виде

# file = open('test.txt', 'rb')
# data = file.read()
# print(data)

# 7. '+' - Открывает файл не только в режиме чтения, но и записи
# 'r+'
# 'w+'




# ===========================МЕТОДЫ РЕЖИМОВ==============================
# 'r'

# 1. read() - если не передать аргументы, читает вест файл
# 2. readline() - считывает только одну строку за раз - str
# 3. readlines() - считывает все строки и сохраняет их в списки

# file = open('test.txt')
# # print(file.tell())
# data2 = file.read()
# # print(file.tell())
# file.seek(0)
# data2 = file.read()
# print(data2)
# file.close()


'''МЕТОДЫ РАБОТАЮЩИЕ СО ВСЕМИ РЕЖИМАМИ'''

# file.tell() - возвращает индекс, где находится указатель

# file.seek(index) - перемещаем указатель на указанный индекс

# f = open('test.txt')
# str_ = f.readline() #cчитвает всю строку
# str2 = f.readline(3) #считывает только указанное колво символов
# print(str_)
# print(str2)
# f.close()

# f = open('test.txt')
# list1 = f.readlines()
# print(list1)
# f.close()

# f = open('test.txt')
# for line in f:
#     print(line)

# f.close()

'''Методы режима w'''

# 1.write('string') - записывает строку в файл

# 2. writelines(list)

# f = open('test2.txt', 'w')
# # f.write('hello\nworld')
# f.writelines(['hello', 'world'])
# f.writelines(('g','o','o','d'))
# f.writelines({'a':1})
# f.close()

# a = ['hello', 'world', 'good', 'morning']
 
# f = open('test2.txt', 'w')
# for i in a:
#     i+= '\n'
#     f.write(i)
# f.close()

# try:
#     f = open('test2.txt')
#     data = f.read()
#     print(data)
# finally:
#     f.close()
#     print(f.closed)

'''КОНТЕКСТНЫЙ МЕНЕДЖЕР. ОТКРЫВАЕТ ФАЙЛ И ПРИ ЛЮБОМ РАСКЛАДЕ ФАЙЛ БУДЕТ ЗАКРЫТ'''    

# with open('test2.txt') as file:
#    print( file.read())

# with open('test2.txt', 'r+') as file:
#     file.write('anara')
#     data = file.read()
#     # print(data)
#     file.write('\nerlan')

# with open('test2.txt', 'w+') as file:
#     file.write('anara')
#     file.seek(0)
#     data = file.read()
    # print(data)
    # file.write('\nerlan')

# with open('test2.txt', 'a+') as file:
#     file.write(' erlan')
#     file.seek(0)
#     print(file.read())

