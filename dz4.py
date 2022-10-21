# Task 1.Вычислить число c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import os
# os.system('cls||clear')

# print('Вычислить число c заданной точностью d\n')

# from math import pi

# d =  int(input("\nВведите число для заданной точности числа Pi: "))

# print(f'\nчисло Пи с заданной точностью {d} равно {round(pi, d)}')


# Task 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def CheckEnteredNumber(number):
#     try:
#         int(number)
#         return True
#     except ValueError:
#         return False

# def PrimeFactors(number):
#     primeFactorsList=[]
#     primeFactorsList.append(1) # добавляем 1 по умолчанию,т.к. единица будет простым множителем для любого числа 
#     tempPrimeFactor=2 # задаем следующего "претендента" на простого множителя для введенного числа 
#     divisionResult=number
#     while divisionResult>1: # выполняем действия пока от введенного числа не останеться единица в результате деления
#             if (divisionResult%tempPrimeFactor)==0: # если число делиться нацело на текущего "претендента" на простой множитель, то делим на него.
#                 primeFactorsList.append(tempPrimeFactor)
#                 divisionResult=divisionResult/tempPrimeFactor
#             else:
#                 tempPrimeFactor=tempPrimeFactor+1 #иначе увеличиваем "претендена" на единицу 
#     return primeFactorsList

# mineNumber = input("Enter your integer number: ")
# if CheckEnteredNumber(mineNumber)==False:
#     print(f"Wrong format of the entered number {mineNumber}! Check your input, the number should be integer!")
# elif int(mineNumber)==0:
#     print("The entered number must NOT be zero!")
# else:
#     mineNumber=int(mineNumber)
#     result=PrimeFactors(mineNumber)
#     print(f"The entered number {mineNumber} has the following prime factors: {result}.")

# Task 3.	Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers=list(map(int,input('Введите последовательность чисел через пробел: ').split()))

# print("Cписок неповторяющихся элементов исходной последовательности: ", list(set(numbers)))


# Task 4.Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from calendar import c
# import os
# os.system("cls")
# from random import randint
# import itertools

# k = int(input('Задайте натуральную степень k: '))

# ratio_list = list([randint(0, 101) for i in range(k+1)]) # задаем случайный список
# if ratio_list[0] == 0: # если будет равен 0, томногочлен может быть неверным
#     ratio_list[0] = randint(1, 101)
# print(ratio_list)

# def get_polynomial(k, ratio_list): # далее идет загугливание информации
#     str1 = ['*x**']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
#     # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
#     # пустые кортежи заполняем пустотой ('')
#     print(polynomial)
#     for x in polynomial:
#         x.append(' + ') # проставляем + между кортежами
#     polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
#     print(polynomial)
#     polynomial[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
#     return "".join(map(str, polynomial)).replace(' 1*x',' x') # возвращаем строку

# list = get_polynomial(k, ratio_list)
# print(list)

# with open('file.txt', 'w') as data:
#     data.write(list)
# with open('file.txt', 'w') as data:
#     data.write(list)