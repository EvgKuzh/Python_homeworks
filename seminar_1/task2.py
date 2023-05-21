# Найдите сумму цифр трехзначного числа

print("введите трехзначное число: ")
a = int(input())

summ = 0
while a > 0:
    x = a % 10
    summ += x
    a //= 10
print(summ)
