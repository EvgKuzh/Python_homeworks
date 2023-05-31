#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

import os
def clear_console(): os.system('cls')


clear_console()

word = input("Enter word: ").lower()
dictionary = {1: 'aeioulnstrавеинорст', 2: 'dgдклмпу',
              3: 'bcmpбгёья', 4: 'fhvwyйы', 5: 'kжзхцч',
              8: 'jxшэю', 10: 'фщъ'}

result_points = 0

for i in word:
    for k, v in dictionary.items():
        if i in v:
            result_points += k

print()
print(f"Ваше колличество очков = {result_points}")