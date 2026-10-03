a = float(input("Введите первое число a: "))
b = float(input("Введите второе число b: "))
c = a * b
if c < 0:
    c *= 8
else:
    c *= 1.5
print(f"Результат: {c}")
