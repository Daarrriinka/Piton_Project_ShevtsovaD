# Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
n = int(input("Введите n (n > 1): "))
s = 0
i = 1
fact = 1

while i <= n:
    fact *= i
    s += fact
    i += 1

print("Сумма факториалов S:", s)
