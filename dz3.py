# Task 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# print('Чтобы найти сумму элементов списка, стоящих на нечётной позиции. Задайте список из нескольких чисел.')
# userList = list(map(int, input('Введите числа списка через пробел: ').split()))
# print(f'Ваш список: {userList}')

# sumListNum = 0

# for i in range(1, len(userList), 2):
#     sumListNum = sumListNum + userList[i]

# print (f'Сумма элементов на нечетных позициях: {sumListNum}')


# Task 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import sample

# def fill_list(number):
#     ls=sample(range(1,number*2),number)
#     return ls

# def multy(lst):
#     lst1=[]
#     len_lst=len(lst)//2
#     for i in range(len_lst):
#         lst1.append(lst[i]*lst[len(lst)-1-i])
#     if len(lst)%2:
#         lst1.append(lst[len(lst)//2])
#     return lst1

# start_list=fill_list(int(input('Enter a number ')))
# print (start_list)
# print (multy(start_list))


# Task 3. Задайте список из вещественных чисел.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# lst = list(map(float, input("Введите числа через пробел:").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# Task 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное

# s = ""
# n = int(input("Введите число: "))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)