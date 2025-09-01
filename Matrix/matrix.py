class Matrix :
    def __init__(self,data):
        if not (isinstance(data,list) or len(data) == 0):
            raise TypeError("Matrix must be a non empty list of lists")
        row_length = len(data[0])
        for row in data:
            if not isinstance(row,list) or len(row) != row_length:
                raise ValueError("The lenght of rows must match each other")
        self.matrix = data
        self.rows = len(data)
        self.columns = len(data[0])
        
    def __str__(self):
        return f"[{"\n".join(" ".join(str(x)for x in row) for row in self.matrix)}]"
    
    def __add__(self,other):
        if not isinstance(other,Matrix):
            raise TypeError("The addition is only possible between matrices ")
        if self.rows != other.rows or self.columns != other.columns :
            raise ValueError("The dimension of matrices must be same")
        return(Matrix([[self.matrix[i][j]+other.matrix[i][j] for j in range(self.columns)]for i in range(self.rows)]))
    
    def __sub__(self,other):
        if not isinstance(other,Matrix):
            raise TypeError("The subtraction is only possible between matrices ")
        if self.rows != other.rows or self.columns != other.columns :
            raise ValueError("The dimension of the matrices must be same")
        return(Matrix([[self.matrix[i][j]-other.matrix[i][j] for j in range(self.columns)]for i in range(self.rows)]))
    
    def __mul__(self,other):
        if isinstance(other,(float,int)):
            #Scalar Multiplication
            return Matrix([[self.matrix[i][j] * other for j in range(self.columns)] for i in range(self.rows)])
        
        if not isinstance(other, Matrix):
            raise ValueError("The Multiplication is only possible with matrices and scalar values")
        
        if self.columns != other.rows:
            raise ValueError("The number of columns must match the number of rows of other matrix ")
        
        result = [[0 for j in range(other.columns)] for i in range(self.rows)]
        for row in range(self.rows): #0
            for column in range(other.columns):#0
                for k in range(self.columns):#1
                    result[row][column] += self.matrix[row][k] * other.matrix[k][column]
                    
        return result
    
    
    def _is_square(self):
        return self.rows==self.columns
    
    
    def _det_recursive(self,matrix):
        n = len(matrix)
        if n == 1 :
            return matrix[0][0]
        if n == 2 :
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for c in range(n):
            minor = [row[:c]+row[c+1:] for row in matrix[1:]]
            det += ((-1)**c) * matrix[0][c] * self._det_recursive(minor) 
        return det
        
    def det(self):
        if not self._is_square():
            raise ValueError("The determinant can be only calculated if it is a square matrix ")
        return self._det_recursive(self.matrix)
    def inverse(self):
        determinant = self.det()
        if determinant == 0:
            raise ValueError("The inverse of a singular matrix does not exist")
        
        n = self.rows
        cofactors = []
        for r in range(n):
            cofactor_row = []
            for c in range(n):
                minor = [row[:c] + row[c+1:] for row in (self.matrix[:r]+self.matrix[r+1:])]
                cofactor = (-1)**(c+r+2)*self._det_recursive(minor)
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
            
        adjoint = list(map(list,zip(*cofactors)))
        inverse = Matrix(adjoint)* (1/determinant)  
        return inverse
    
    
#__mul__ vs __rmul__
        """
        These are special magic methods or dunder methods used to define how object behaves when invloved in multiplication  operations
        __mul__  is called when the instance of a class is at the left side of the multiplication operator 
        __rmul__ is called when the instance of the class is at the right side of the multiplication operator
        """
        
#Polymorphism

        """
        Polymorphism defines same method behaving differently
        
        In python we cannot define two methods with the same name - the later one will overwrite the earlier
        Instead we write a single method and add type checks 
        -> This is not true overloading - its polymorphism with operator overloading because same method behaves differently depending on type of argument
        """