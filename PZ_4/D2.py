i = 0
c = 0

while i < 4:
    num = int(input("Введите целое число: "))
    if num % 2 == 0:
        c += 1
    i += 1

print("Количество чётных:", c)
