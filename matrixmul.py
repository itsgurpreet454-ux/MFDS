m = int(input("Input rows for first matrix: "))
n = int(input("Input columns for first matrix: "))
p = int(input("Input columns for second matrix: "))

A = []
B = []
C = []

print("Input elements for first matrix:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

print("Input entries of second matrix:")
for i in range(n):
    row = []
    for j in range(p):
        row.append(int(input()))
    B.append(row)

for i in range(m):
    row = []
    for j in range(p):
        sum = 0

        for k in range(n):
            sum += A[i][k] * B[k][j]

        row.append(sum)

    C.append(row)

print("Final matrix:")

for i in range(m):
    for j in range(p):
        print(C[i][j], end=" ")
    print()


