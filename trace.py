def trace():
    size= int(input("Enter size of square matrix: "))

    A = []

    for r in range(size):
        row = []

        for c in range(size):
            row.append(int(input(f"A[{r}][{c}]: ")))

        A.append(row)

    Trace = 0

    for r in range(size):
        trace += A[r][r]

    print("Trace of matrix =", Trace)