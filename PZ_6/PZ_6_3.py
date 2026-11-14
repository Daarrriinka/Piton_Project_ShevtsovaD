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
    X.append(random.randint(-10, 10))
    Y.append(random.randint(-10, 10))

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
