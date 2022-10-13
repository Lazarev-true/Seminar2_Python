# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

N = input('Введите число: ')
sum = 0
for i in range(len(N)):
    if N[i] == '.':
        continue
    else:
        sum += int(N[i])
print(sum)
