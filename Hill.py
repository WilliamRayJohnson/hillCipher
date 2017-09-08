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
        
    def convertToText(self, numbers):
        text = ''
        
        for num in numbers:
            text = text + chr(num + self.asciiOffset)
            
        return text
        
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
        
    def encrypt(self, plainText):
        plainTextMatrices = self.splitPlainTextIntoMatrices(plainText)
        cipherTextNumbers = []
        
        for PTMatrix in plainTextMatrices:
            multipliedValues = self.key.multiply(PTMatrix).getMatrixValue()
            for value in multipliedValues:
                cipherTextNumbers.append(value[0] % 26)
            
        cipherText = self.convertToText(cipherTextNumbers)
        return cipherText.upper()
        
    def decrypt(self, cipherText):
        return "Decrypt is not yet implemented"
        