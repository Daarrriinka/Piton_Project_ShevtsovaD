a = 1
d = 3
count = 0

while a < 30:
    if a > 10:
        print(f"Элемент подходит: {a}")
        count += 1
    a += d

print("Количество элементов:", count)
