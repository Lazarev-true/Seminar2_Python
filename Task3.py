# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите размер списка: '))
#list = []
dict = {}
j = 1
sum = 0
for i in range(n):
    j = round((1 + 1/(i + 1))**(i + 1), 2)
    sum += j
    #list.append(j)
    dict[i + 1] = j
#print(list)
print(f'Для n = {n} {dict}')
print('Сумма:', sum)