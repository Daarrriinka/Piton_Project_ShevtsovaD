#Вариант 26
#Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
#положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то
#вывести порядковый номер первого элемента, нарушающего закономерность.

import random

N = int(input("Введите размер списка: "))

A = []

for i in range(N):
    A.append(random.choice([-1, 1]) * random.randint(1, 10))

print("Исходный список:", A)

k = 0

for i in range(1, N):
    if A[i] * A[i - 1] > 0:
        k = i + 1
        break

print("Результат:", k)

import random

a = []
n = int(input("Введите размер списка: "))

while len(a) < n:
    x = random.randint(-50, 50)
    if x != 0:
        a.append(x)

print("Исходный список:", a)

result = 0

for i in range(1, len(a)):
    if a[i] > 0 and a[i-1] > 0:
        result = i + 1
        break
    if a[i] < 0 and a[i-1] < 0:
        result = i + 1
        break

print("Результат:", result)