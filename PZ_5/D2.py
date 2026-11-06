#Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.

# Функция для вычисления площади и периметра
def rectangle(a, b):
    area = a * b
    perimeter = 2 * (a + b)

    return area, perimeter


# Ввод длины сторон
while True:
    try:
        a = float(input('Введите длину прямоугольника: '))
        b = float(input('Введите ширину прямоугольника: '))

        if a > 0 and b > 0:
            break
        else:
            print('Стороны должны быть положительными!')

    except ValueError:
        print('Ошибка! Введите числовые значения.')

# Вызов функции и получение результатов
S, P = rectangle(a, b)

# Вывод результатов
print('Площадь прямоугольника:', round(S, 2), 'Периметр прямоугольника:', round(P, 2))


def rectangle(a, b):
    area = a * b
    perimeter = 2 * (a + b)

    return area, perimeter


try:
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))

    if a <= 0 or b <= 0:
        print("Стороны должны быть положительными")
    else:
        area, perimeter = rectangle(a, b)

        print("Площадь:", area)
        print("Периметр:", perimeter)

except ValueError:
    print("Ошибка! Введите числа.")
