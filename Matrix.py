'''
@author William Ray Johnson
9/4/17
'''

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