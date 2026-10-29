m = int(input("Введіть натуральне число m: "))

n = m
k = 0

print("Цифри числа у зворотному порядку:")

while n > 0:
    cifra = n % 10
    print(cifra, end=" ")
    n = n // 10
    k = k + 1

print()
print("Кількість цифр числа:", k)
