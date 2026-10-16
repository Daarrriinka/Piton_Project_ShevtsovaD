n = int(input("Введите количество чисел N: "))
i = 0
c = 0

while i < n:
    num = float(input("Введите число: "))
    if num == 0:
        c += 1
    i += 1

print("Количество нулей:", c)
