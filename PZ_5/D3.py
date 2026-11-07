#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.

def count_digits(number):
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    print(count)
n = int(input("Введите числo "))
count_digits(n)