# Написать программу, которая проверяет счастливость билета.

number = (input('введите номер билета: '))

a0 = int (number[0])
a1 = int (number[1])
a2 = int (number[2])
a3 = int (number[3])
a4 = int (number[4])
a5 = int (number[5])

if a0+a1+a2 == a3+a4+a5:
    print ('yes')

else:
    print('no')
