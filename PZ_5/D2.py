#Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.

def per(m, n):
    return m * 2 + n * 2
def area(m, n):
    return m * n
m = int(input("Введите числo "))
n = int(input("Введите числo "))
print("Периметр: ", per(m, n), "Площадь: ", area(m, n))

