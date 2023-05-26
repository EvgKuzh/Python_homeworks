# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

size = 0
while size<=0:
    size = int(input("Введите колличество монет: "))

from random import randint
n = size
array = [randint(0, 1) for i in range(n)]

print(*array)

zero = 0
one = 0
for i in array:
    if i == 0:
        zero += 1
    if i == 1:
        one += 1

if zero == size or one == size:
    print("Все монеты повернуты одной стороной")
    exit()
elif zero > one:
    minNum = one
else:
    minNum = zero

print (f"{minNum} - минимальное колличество монет, которое нужно перевернуть")
