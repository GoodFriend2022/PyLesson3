# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, 
# выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

from Functions import CreateArray

def FindNearNumber(array, number):
    diff = number
    for i in array:
        if number > i:
            if diff >= number - i:
                diff = number - i
                nearNumber = i
        elif number < i:
            if diff > i - number:
                diff = i - number
                nearNumber = i
        else: return i
    return nearNumber

n = int(input('Введите требуемое количество элементов > '))
x = int(input('Введите искомое число > '))
numbers = CreateArray(n)
uniqueNumbers = set(CreateArray(n))
print(numbers)
print(f'Введенное Вами число ближе всего к числу {FindNearNumber(uniqueNumbers, x)} из массива')

# numbers2 = [1, 3, 5, 8, 9, 12, 13]
# print(f'Введенное Вами число ближе всего к числу {FindNearNumber(numbers2, x)} из массива')


