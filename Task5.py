# Реализуйте алгоритм перемешивания списка.

from random import randint

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print ("Первоночальный список : ", list)

for i in range(0, len(list)-1):
    j = randint(i, len(list)-1) 

    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

print ("Список после перемешивания элементов: " + str(list))