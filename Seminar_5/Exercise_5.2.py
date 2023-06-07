

def sumAB(a, b):
    if a == 0:
        return b
    return sumAB(a-1, b+1)


one = int(input("Введите целое число A: "))
two = int(input("Введите целое число B: "))
result = (sumAB(one, two))
print(f"сумма {one} и {two} равна {result}")