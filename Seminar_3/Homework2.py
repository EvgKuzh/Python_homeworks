#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import os
def clear_console(): os.system('cls')
clear_console()

size = int(input("Введите размер списка: "))

from random import *
array = [randint(0, 100) for i in range(size)]
print(array)

x = randint(0, 100)
print()
print(f"x = {x}")
xMin = 999 #магическое число, для входа в if xSize<xMin
xSize = 0
xCurrent = 0
for i in array:
    if x>i:
        xSize = x - i
        if xSize<xMin:
            xMin = xSize
            xCurrent = i
    else:
        xSize = i - x
        if xSize<xMin:
            xMin = xSize
            xCurrent = i

print()
print(f"Самое близкое значение к {x} - это {xCurrent}")