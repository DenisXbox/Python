# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

#day = int(input('Enter day number: '))
#if day > 7 or day < 1:
#   print('Please, repeat the input')
#elif day == 6 or day == 7:
#    print("Yes, it's weekend!")
#else:
#    print("No, it's not weekend!")


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
   print('3')
if x > 0 and y < 0:
   print('4')