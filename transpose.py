def transpose(matrix):

  rows = len(matrix)
  colms = len(matrix[0])

  output = [[matrix[i][j] for i in range(rows)] for j in range(cols)]

  return result


matrix = [[1, 2, 3], [4, 5, 6]]

new_matrix = transpose(matrix)
print("Transpose of  Matrix :")
for row in new_matrix:
    print(row)
