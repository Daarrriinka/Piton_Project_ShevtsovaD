a = int(input("Введите двухзначное число : "))
des = a // 10
edi = a % 10
desum = des + edi
if desum % 10 == 0:
    a+= 2
else:
    a-= 2
    print(f"Результат: {a}")

