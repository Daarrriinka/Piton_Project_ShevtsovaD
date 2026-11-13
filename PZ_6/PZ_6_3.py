#Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
#такую точку из данного множества, сумма расстояний от которой до остальных его
#точек минимальна, и саму эту сумму.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2.
import random
import math

N = int(input("Введите количество точек: "))

X = []
Y = []

for i in range(N):
    X.append(random.randint(1, 10))
    Y.append(random.randint(1, 10))

print("Исходные точки:")

for i in range(N):
    print("Точка", i + 1, ":", X[i], Y[i])

A = []

for i in range(N):
    s = 0

    for j in range(N):
        if i != j:
            R = math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            s = s + R

    A.append(s)

k = A.index(min(A))

print("Точка с минимальной суммой расстояний:")
print("X =", X[k])
print("Y =", Y[k])
print("Сумма расстояний:", round(A[k], 2))

import random
import math

x = []
y = []

n = int(input("Введите количество точек (больше 2): "))

while len(x) < n:
    x.append(random.randint(-10, 10))
    y.append(random.randint(-10, 10))

print("Координаты точек:")

for i in range(n):
    print("Точка", i + 1, ":", x[i], y[i])

min_sum = float('inf')
best_point = 0

for i in range(n):
    total = 0

    for j in range(n):
        if i != j:
            r = math.sqrt((x[j] - x[i])**2 + (y[j] - y[i])**2)
            total += r

    if total < min_sum:
        min_sum = total
        best_point = i

print("Искомая точка:", x[best_point], y[best_point])
print("Минимальная сумма расстояний:", round(min_sum, 2))