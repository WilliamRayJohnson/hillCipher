'''
@author William Ray Johnson
9/7/17
'''

import Matrix

class Hill:
    asciiOffset = ord("a")
    paddingValue = ord("x") - asciiOffset
    
    def __init__(self, keyValues):
        if len(keyValues) == 4:
            self.key = Matrix.Matrix(2, 2, keyValues)
        elif len(keyValues) == 9:
            self.key = Matrix.Matrix(3, 3, keyValues)
    
    def convertToNumbers(self, plainText):
        plainText = plainText.lower().replace(" ", "")
        plainTextNumbers = []
        
        for char in plainText:
            plainTextNumbers.append(ord(char) - self.asciiOffset)
            
        return plainTextNumbers
        
    def splitPlainTextIntoMatrices(self, plainText):
        plainTextNumbers = self.convertToNumbers(plainText)
        matrices = []
        
        if len(plainTextNumbers) % self.key.rows != 0:
            for padding in range(len(plainTextNumbers) % self.key.rows):
                plainTextNumbers.append(self.paddingValue)
                
        for slice in range(len(plainTextNumbers)//self.key.rows):
            matrices.append(Matrix.Matrix(self.key.rows, 1, plainTextNumbers[:self.key.rows]))
            plainTextNumbers = plainTextNumbers[self.key.rows:]
            
        return matrices
        
        
        