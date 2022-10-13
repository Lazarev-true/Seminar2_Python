# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции вводятся с клавиатуры

from random import randint

N = int(input('Введите размер списка: '))

list = []

for i in range(N):
    list.append(randint(-N, N + 1))
print(list)

el = input('Введите (через пробел) порядковые номера ' +
                'элементов, которые нужно перемножить: ').split()

for i in range(len(el)):
    if int(el[i]) > N or int(el[i]) <= 0:
        print(f'Элемента под номером {el[i]} нет')
        quit()

pr = 1
for i in range(len(el)):
    pr *= list[int(el[i]) - 1]
print(pr)