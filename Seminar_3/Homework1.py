#  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import os
def clear_console(): os.system('cls')
clear_console()

from random import *
n = int(input("Введите размер списка: "))
items = [randint(0, 5) for i in range(n)]
print(items)

x = randint(0, 5)

result = 0
for i in items:
    if i == x:
        result+=1
    else:
        next

print()        
print (f"колличество {x} в списке {result}")