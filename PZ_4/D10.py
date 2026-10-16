n = int(input("Введите N (N >= 3): "))
f1 = 1
f2 = 1
print(f1)
print(f2)
count_even = 0

i = 2
while i < n:
    f3 = f1 + f2
    print(f3)
    if f3 % 2 == 0:
        count_even += 1
    f1 = f2
    f2 = f3
    i += 1

print("Количество чётных чисел Фибоначчи:", count_even)
