import random

M = []

for i in range(4):
    row = []
    for j in range(8):
        row.append(random.randint(0, 20))
    M.append(row)

print("Початкова матриця M:")
for row in M:
    print(row)

N = []

for i in range(4):
    row = M[i].copy()
    maximum = max(row)
    max_index = row.index(maximum)

    row[0], row[max_index] = row[max_index], row[0]
    N.append(row)

print("\nМатриця після перестановки:")
for row in N:
    print(row)
