a = int(input("Введите A: "))
b = int(input("Введите B (B > A): "))
c = b
d = 0

while c >= a:
    print(c)
    d += 1
    c -= 1

print("Количество чисел:", d)
