#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.

# Функция для подсчета количества цифр числа
def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count


# Ввод целого числа
while True:
    try:
        number = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Ошибка! Введите целое число.')

# Вызов функции
result = count_digits(number)

# Вывод результата
print('Количество цифр в числе:', result)


def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count


try:
    number = int(input("Введите число: "))

    print("Количество цифр:", count_digits(number))

except ValueError:
    print("Ошибка! Введите целое число.")