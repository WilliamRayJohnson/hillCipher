'''
@author William Ray Johnson
9/4/17
'''

class Matrix:
    def __init__(self, rows, cols, values):
        self.rows = rows
        self.cols = cols
        self.buildMatrix(values)
    
    def buildMatrix(self, values):
        self.matrix = []
        for row in range(self.rows):
            self.matrix.append(values[:self.cols])
            values = values[self.cols:]
         
    def getMatrixValue(self):
        return self.matrix
        
    def multiply(self, matrix):
        return matrix