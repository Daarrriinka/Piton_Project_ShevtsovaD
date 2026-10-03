a = float(input("Введите первое число : "))
b = float(input("Введите второе число : "))
c = a + b
if c % 5 == 0:
    print(f"Результат: {c + 1}")
else:
    print(f"Результат: {c - 2}")
