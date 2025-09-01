from matrix import Matrix
x = [[1,2,3],[4,5,6]]

y = Matrix(x)
z = Matrix([[1,2,3],[4,5,6]])
print(y+z)
print(y-z)
print(y*3)

A = Matrix([[1,1,1]])
B = Matrix([[1,0,0],[0,4,0],[0,0,6]])
print(A*B)

print(B.det())

C = Matrix([[4,3],[3,2]])
print(C.inverse())