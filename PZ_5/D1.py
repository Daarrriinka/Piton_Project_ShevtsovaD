#Даны три целых числа. Определить у какого числа больше сумма цифр.
#Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.

def sum_sd(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
a,b,c = int(input("Введите число ")), int(input("Введите числo ")), int(input("Введите числo "))

sum_a = sum_sd(a)
sum_b = sum_sd(b)
sum_c = sum_sd(c)
if sum_a > sum_b and sum_a > sum_c:
    print("Наибольшая сумма у числа:", a,"Сумма цифр:", sum_a)
elif sum_b > sum_a and sum_b > sum_c:
    print("Наибольшая сумма у числа:", b, "Сумма цифр:", sum_b)
elif sum_c > sum_a and sum_c > sum_b:
    print("Наибольшая сумма у числа:", c, "Сумма цифр:", sum_c)