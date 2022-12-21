# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
import random

def CreateArray(lengthArray):
    array = []
    for i in range(lengthArray):
        array.append(random.randint(1, lengthArray//2))
    return array

def FindNumber(array, number):
    count = 0
    for i in array:
        if i == number:
            count += 1
    return count

n = int(input('Введите требуемое количество элементов > '))
x = int(input('Введите искомое число от 1 до N > '))
numbers = CreateArray(n)
print(numbers)
if FindNumber(numbers, x) == 0:
    print('Введенное Вами число отсутствует в массиве')
else:
    print(f'Введенное Вами число встречается в массиве {FindNumber(numbers, x)} раз(а)')
        


