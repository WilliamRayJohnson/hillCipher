'''
@author William Ray Johnson
9/7/17
'''

import unittest

import Matrix
import Hill

class HillTest(unittest.TestCase):
    def setUp(self):
        self.key2x2 = Matrix.Matrix(2, 2, [7, 19, 8, 3])
        self.plainText = "test"
        self.cipherText = "BITT"
        self.cipher2x2 = Hill.Hill([7, 19, 8, 3])
        self.cipher3x3 = Hill.Hill([6,24,1,13,16,10,20,17,15])
        
    def testConvertPlainTextToNumber(self):
        expectedPTNumbers = [19, 4, 18, 19]
        actualPTNumbers = self.cipher2x2.convertToNumbers(self.plainText)
        
        self.assertEqual(actualPTNumbers, expectedPTNumbers)
        
    def testSplitPlainTextIntoMatrices(self):
        expectedMatrices = [Matrix.Matrix(2,1,[19,4]), Matrix.Matrix(2,1,[18,19])]
        actualMatricies = self.cipher2x2.splitPlainTextIntoMatrices(self.plainText)
        
        self.assertEqual(actualMatricies, expectedMatrices)
        
    def testConvertPlainTextToNumberWithPadding2x2(self):
        expectedMatrices = [Matrix.Matrix(2,1,[19,4]), Matrix.Matrix(2,1,[18,19]),
                            Matrix.Matrix(2,1,[8, 13]), Matrix.Matrix(2,1,[6,23])]
        actualMatricies = self.cipher2x2.splitPlainTextIntoMatrices("testing")
        
        self.assertEqual(actualMatricies, expectedMatrices)
    
    def testConvertPlainTextToNumberWithPadding3x3(self):
        expectedMatrices = [Matrix.Matrix(3,1,[19,4,18]), Matrix.Matrix(3,1,[19,23,23])]
        actualMatricies = self.cipher3x3.splitPlainTextIntoMatrices("test")
        
        self.assertEqual(actualMatricies, expectedMatrices)
        
    def testConvertNumbersToText(self):
        expectedText = "test"
        actualText = self.cipher2x2.convertToText([19,4,18,19])
        
        self.assertEqual(actualText, expectedText)
        
    def testEncrypt(self):
        expectedEncryption = "BITT"
        actualEncryption = self.cipher2x2.encrypt(self.plainText)
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
    def testEncryptWithWikipediaExample(self):
        wikiCipher = Hill.Hill([3,3,2,5])
        expectedEncryption = ("HIAT")
        actualEncryption = wikiCipher.encrypt("help")
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
    def testCalcDecryptionKeyWithWikipediaExample(self):
        cipher = Hill.Hill(([3,3,2,5]))
        expectedDecryptKey = Matrix.Matrix(2,2, [15,17,20,9])
        actualDecryptKey = cipher.getDecryptKey()
        
        self.assertEqual(actualDecryptKey.getMatrixValue(), expectedDecryptKey.getMatrixValue())
        
    def testCalcDecryptionKey(self):
        expectedDecryptKey = Matrix.Matrix(3,3, [8,5,10,21,8,21,21,12,8])
        actualDecryptKey = self.cipher3x3.getDecryptKey()
        
        self.assertEqual(actualDecryptKey.getMatrixValue(), expectedDecryptKey.getMatrixValue())
        
    def testDecrypt(self):
        expectedDecryption = "test"
        actualDecryption = self.cipher2x2.decrypt(self.cipherText)
        
        self.assertEqual(actualDecryption, expectedDecryption)
        
    def testInvertNumber(self):
        expectedInversion = 3
        actualInversion = self.cipher2x2.invertNumber(9)
        
        self.assertEqual(actualInversion, expectedInversion)
        
        
if __name__ == '__main__':
    unittest.main()