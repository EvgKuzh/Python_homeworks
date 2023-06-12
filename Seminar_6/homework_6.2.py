# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os
def clear_console(): os.system('cls')


clear_console()


def newRandomArray(size, minNumber, maxNumber):
    from random import randint
    newArray = []
    for i in range(size):
        newArray.append(randint(minNumber, maxNumber))
    return newArray


list1 = newRandomArray((int(input("Создайте массив: \nвведите размер: "))), (int(input(
    "введите минимальное значение: "))), (int(input("введите максимальное значение: "))))
print(list1)
print()
leftmost_value = int(
    input("Введите минимальное значение искомого диапазона: "))
rightmost_value = int(
    input("Введите максимальное значение искомого диапазона: "))

result = {}
for i in list1:
    if i > leftmost_value and i < rightmost_value:
        result[list1.index(i)] = i

if len(result) < 1:
    print(
        f"Нет значений принадлежащих диапазону ({leftmost_value};{rightmost_value}).")
else:
    print(f"Диапазону (({leftmost_value};{rightmost_value}) принадлежат:)")
    for k, v in result.items():
        print(f"индекс = {k}, значение = {v}")
