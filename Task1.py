# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

N = input('Введите число: ')
sum = sum(map(int, N.replace('.', '')))
print(sum)
