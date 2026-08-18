def input_matrix():
    rows=int(input("Enter no. of rows:"))
    colms=int(input("Enter no. of cols:"))
    X=[]
    print("Enter elements of matrix:")

    for i in range(r):
        row=list(map(int,input().split()))
        X.append(row)
    return X

X=input_matrix()

print("Matrix X:",X)
#Transpose of matrix
def transpose(X):
     Trans=[]
     for j in range(len(X[0])):
         row=[]
         for i in range(len(X)):
             row.append(X[i][j])
         Trans.append(row)

     return Trans
Trans=transpose(A)
print("Transpose of A:")
for row in Trans:
     print(row)
