import math

A = []
B = []
C = []

for k in range(10):
    x = float(input(f"Введіть A[{k + 1}]: "))
    A.append(x)

for k in range(1, 11):
    b = ((-1) ** k) * math.sqrt(math.factorial(k))
    B.append(b)

for k in range(10):
    c = 2 * A[k] - 3 * B[k]
    C.append(c)

print("\nМасив A:", A)
print("Масив B:", B)
print("Масив C:", C)

print("\nМасив A:", [round(x, 3) for x in A])
print("Масив B:", [round(x, 3) for x in B])
print("Масив C:", [round(x, 3) for x in C])

sum_A = 0
sum_B = 0
sum_C = 0

for x in A:
    if x > 0:
        sum_A += x

for x in B:
    if x > 0:
        sum_B += x

for x in C:
    if x > 0:
        sum_C += x

print("\nСума додатних елементів A:", sum_A)
print("Сума додатних елементів B:",round ( sum_B,3))
print("Сума додатних елементів C:", round (sum_C,3))
