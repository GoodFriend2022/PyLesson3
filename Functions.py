import random
def CreateArray(lengthArray):
    array = []
    for i in range(lengthArray):
        array.append(random.randint(1, lengthArray//2))
    return array