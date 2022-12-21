# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# -----------------------------------
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# ------------------------------------
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

englishLetters = \
    {
        1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'],
        2: ['d', 'g'],
        3: ['b', 'c', 'm', 'p'],
        4: ['f', 'h', 'v', 'w', 'y'],
        5: ['k',],
        8: ['j', 'x'],
        10: ['q', 'z']
    }

rusianLetters = \
    {
        1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'е'],
        2: ['д', 'к', 'л', 'м', 'п', 'у'],
        3: ['б', 'г', 'ё', 'ь', 'я'],
        4: ['й', 'ы'],
        5: ['ж', 'з', 'х', 'ц', 'ч'],
        8: ['ш', 'э', 'ю'],
        10: ['ф', 'щ', 'ъ']
    }

userWord = input('Введите слово > ').lower()

def Score(word, dict):
    sum = 0
    for letter in word:
        for key, value in dict.items():
            if letter in value:
                sum += key
                break
    return sum

def Dictionary(word):
    english = set('qwertyuiopasdfghjklzxcvbnm')
    beforeLength = len(english)
    english.add(word[0])
    afterLength = len(english)
    if beforeLength == afterLength:
        return True
    return False

if Dictionary(userWord):
    print(f'Вы получили {Score(userWord, englishLetters)} очков')
else:
    print(f'Вы получили {Score(userWord, rusianLetters)} очков')
