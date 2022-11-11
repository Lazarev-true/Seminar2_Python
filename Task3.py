# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите размер списка: '))
dict = {x: eval('round((1 + 1 / x)**x, 2)') for x in range(1, n+1)}
print(f'Для n = {n} {dict}')
print('Сумма:', sum(dict.values()))