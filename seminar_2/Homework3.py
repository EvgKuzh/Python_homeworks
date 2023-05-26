# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 0
while n<=1:
    n = int(input("Введите целое положительное число: "))

import math

for i in range(1,n+1):
    result = int(math.pow(2,i))
    if result<=n:
        print(f"2 в степени {i} = {result}")