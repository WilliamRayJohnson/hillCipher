'''
@author William Ray Johnson
9/4/17
'''

from fractions import gcd

class Matrix:
    def __init__(self, rows, cols, values):
        self.rows = rows
        self.cols = cols
        self.buildMatrix(values)
        
    def __eq__(self, other):
        return self.getMatrixValue() == other.getMatrixValue()
        
    def buildMatrix(self, values):
        self.matrix = []
        for row in range(self.rows):
            self.matrix.append(values[:self.cols])
            values = values[self.cols:]
         
    def getMatrixValue(self):
        return self.matrix
    
    def getSize(self):
        return str(self.rows) + "x" + str(self.cols)
        
    def setMatrixValue(self, matrix):
        self.matrix = matrix
        
    def multiply(self, matrix):
        matrixA = self.matrix
        matrixB = matrix.getMatrixValue()
        returnMatrix = Matrix(len(matrixA), 
                    len(matrixB[0]), ['-'] * (len(matrixA) * len(matrixB[0])))
        matrixC = returnMatrix.getMatrixValue()
        
        for row in range(len(matrixA)):
            for col in range(len(matrixB[0])):
                matrixC[row][col] = 0
                for mid in range(len(matrixA[0])):
                    matrixC[row][col] = matrixC[row][col] + matrixA[row][mid] * matrixB[mid][col]
              
        returnMatrix.setMatrixValue(matrixC)
        return returnMatrix
        
    def calcAdjugateMatrix(self):
        if self.getSize() == '2x2':
            adjugateMatrix = Matrix(2,2,[self.matrix[1][1], -self.matrix[0][1], -self.matrix[1][0], self.matrix[0][0]])
        elif self.getSize() == '3x3':
            A = (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1])
            B = -(self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0])
            C = (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])
            D = -(self.matrix[0][1] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][1])
            E = (self.matrix[0][0] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][0])
            F = -(self.matrix[0][0] * self.matrix[2][1] - self.matrix[0][1] * self.matrix[2][0])
            G = (self.matrix[0][1] * self.matrix[1][2] - self.matrix[0][2] * self.matrix[1][1])
            H = -(self.matrix[0][0] * self.matrix[1][2] - self.matrix[0][2] * self.matrix[1][0])
            I = (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0])
            
            adjugateMatrix = Matrix(3,3,[A,D,G,B,E,H,C,F,I])
            
            
        return adjugateMatrix
        
    def calcDeterminant(self):
        if self.getSize() == '2x2':
            determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        elif self.getSize() == '3x3':
            A = (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1])
            B = -(self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0])
            C = (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])
            
            determinant = self.matrix[0][0] * A + self.matrix[0][1] * B + self.matrix[1][0] * C
            
        return determinant**-1