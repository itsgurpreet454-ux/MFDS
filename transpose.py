def transpose(matrix):

  rows = len(matrix)
  cols = len(matrix[0])

  result = [[matrix[i][j] for i in range(rows)] for j in range(cols)]

  return result


matrix = [[1, 2, 3], [4, 5, 6]]

transposed_matrix = transpose(matrix)
print("Transposed Matrix :")
for row in transposed_matrix:
    print(row)