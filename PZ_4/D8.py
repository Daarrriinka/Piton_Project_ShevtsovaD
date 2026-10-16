a = int(input("Введите A: "))
b = int(input("Введите B (B > A): "))
total_sum = 0
current = a

while current <= b:
    total_sum += current
    current += 1

print("Сумма чисел:", total_sum)
