

def square(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a*square(a, n-1)
    else:
        return square(a*a, n/2)



one = int(input("Введите целое число: "))
two = int(input("Введите степень: "))
result = (square(one, two))
print(f"число {one} в степени {two} равно {result}")