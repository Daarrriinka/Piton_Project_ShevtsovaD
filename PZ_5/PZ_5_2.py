#V26
#Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.

# создаём функцию, принимающую число K.
def InvertDigits(K):
    #создаём переменную для хранения перевёрнутого числа.
    result = 0

    while K > 0:
        digit = K % 10
        result = result * 10 + digit
        K //= 10
#возвращаем полученное число.
    return result

# Ввод пяти целых положительных чисел
for i in range(1, 6):
    while True:
        try:
            K = int(input(f'Введите число {i}: '))

            if K > 0:
                break
            else:
                print('Число должно быть положительным!')

        except ValueError:
            print('Ошибка! Введите целое число.')

    # Вызов функции
    print('Число в обратном порядке:', InvertDigits(K))


def InvertDigits(K):
    result = 0

    while K > 0:
        digit = K % 10
        result = result * 10 + digit
        K //= 10

    return result


try:
    i = 1

    while i <= 5:
        K = int(input("Введите положительное число: "))

        if K <= 0:
            print("Число должно быть положительным")
        else:
            print("Перевёрнутое число:", InvertDigits(K))
            i += 1

except ValueError:
    print("Ошибка! Введите целое число.")