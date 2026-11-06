#Даны три целых числа. Определить у какого числа больше сумма цифр.
#Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.

# Функция для вычисления суммы цифр числа
def sum_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


# Ввод трех целых чисел
numbers = []

for i in range(1, 4):
    while True:
        try:
            number = int(input(f'Введите число {i}: '))
            numbers.append(number)
            break
        except ValueError:
            print('Ошибка! Введите целое число.')

# Вычисление суммы цифр каждого числа
sums = []

for number in numbers:
    sums.append(sum_digits(number))

# Нахождение максимальной суммы цифр
max_sum = max(sums)

# Вывод результата
print('\nРезультаты:')

for i in range(3):
    print('Число:', numbers[i],
          'Сумма цифр:', sums[i])

print('\nНаибольшая сумма цифр:', max_sum)

for i in range(3):
    if sums[i] == max_sum:
        print('Подходящее число:', numbers[i])

def sum_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    sum_a = sum_digits(a)
    sum_b = sum_digits(b)
    sum_c = sum_digits(c)

    maximum = max(sum_a, sum_b, sum_c)

    print("Наибольшая сумма цифр:", maximum)

    if sum_a == maximum:
        print("Первое число:", a)

    if sum_b == maximum:
        print("Второе число:", b)

    if sum_c == maximum:
        print("Третье число:", c)

except ValueError:
    print("Ошибка! Введите целые числа.")