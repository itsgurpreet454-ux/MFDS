def newmatrix(name):
    print(f"MATRIX{name}")
    rows=int(input("enter no. of rows"))
    colms=int(input("enter no. of columns"))
    matrix=[]
    print("enter elements of row")
    for i in range(rows):
          row=list(map(float,input(f"row{i+1}:").split()))
          matrix.append(row)
    return matrix
X= newmatrix("A")
Y= newmatrix("B")

rows_X,colmsX =len(X),len(X[0])
rows_Y,colmsY =len(Y),len(Y[0])

if rows_X==rows_Y and colmsX == colmsY:
     addition=[]
     subtraction=[]
     for i in range(rows_X):
          add_row=[]
          sub_row=[]
          for j in range(colmsY):
               add_row.append(X[i][j]+Y[i][j])
               sub_row.append(X[i][j]-Y[i][j])
               addition.append(add_row)
               subtraction.append(sub_row)

               print("Addition")
               for row in addition:print(row)
               print("Subtraction")
               for row in subtraction:print(row)
               else:
                    print("for addition/subtraction matrix must have same same size.")









