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
        self.calcDecryptionKey()
    
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
            for padding in range(self.key.rows - (len(plainTextNumbers) % self.key.rows)):
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
    
    def invertNumber(self, number):
        inversion = 1
        
        while (number * inversion) % 26 != 1 % 26:
            inversion += 1
        
        return inversion
        
    def calcDecryptionKey(self):
        determinate = self.key.calcDeterminant()
        adjugate = self.key.calcAdjugateMatrix()
        decryptKeyValues = []
        
        determinate = self.invertNumber(determinate**-1)
        for row in adjugate.getMatrixValue():
            for value in row:
                decryptKeyValues.append(((value + 26) * determinate) % 26) 
                
        self.decryptKey = Matrix.Matrix(self.key.rows, self.key.cols, decryptKeyValues)
        
    def getDecryptKey(self):
        return self.decryptKey
    
    def decrypt(self, cipherText):
        cipherTextMatrices = self.splitPlainTextIntoMatrices(cipherText)
        plainTextNumbers = []
        
        for CTMatrix in cipherTextMatrices:
            multipliedValues = self.decryptKey.multiply(CTMatrix).getMatrixValue()
            for value in multipliedValues:
                plainTextNumbers.append(value[0] % 26)
        
        plainText = self.convertToText(plainTextNumbers)
        return plainText.lower()
        