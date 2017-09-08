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
        self.cipher = Hill.Hill([7, 19, 8, 3])
        
    def testConvertPlainTextToNumber(self):
        expectedPTNumbers = [19, 4, 18, 19]
        actualPTNumbers = self.cipher.convertToNumbers(self.plainText)
        
        self.assertEqual(actualPTNumbers, expectedPTNumbers)
        
    def testSplitPlainTextIntoMatrices(self):
        expectedMatrices = [Matrix.Matrix(2,1,[19,4]), Matrix.Matrix(2,1,[18,19])]
        actualMatricies = self.cipher.splitPlainTextIntoMatrices(self.plainText)
        
        self.assertEqual(actualMatricies, expectedMatrices)
        
    def testConvertPlainTextToNumberWithPadding(self):
        expectedMatrices = [Matrix.Matrix(2,1,[19,4]), Matrix.Matrix(2,1,[18,19]),
                            Matrix.Matrix(2,1,[8, 13]), Matrix.Matrix(2,1,[6,23])]
        actualMatricies = self.cipher.splitPlainTextIntoMatrices("testing")
        
        self.assertEqual(actualMatricies, expectedMatrices)
        
    def testConvertNumbersToText(self):
        expectedText = "test"
        actualText = self.cipher.convertToText([19,4,18,19])
        
        self.assertEqual(actualText, expectedText)
        
    def testEncrypt(self):
        expectedEncryption = "BITT"
        actualEncryption = self.cipher.encrypt(self.plainText)
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
    def testEncryptWithWikipediaExample(self):
        wikiCipher = Hill.Hill([3,3,2,5])
        expectedEncryption = ("HIAT")
        actualEncryption = wikiCipher.encrypt("help")
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
    def testDecrypt(self):
        expectedDecryption = "test"
        actualDecryption = self.cipher.decrypt(self.cipherText)
        
        self.assertEqual(actualDecryption, expectedDecryption)
        
        
if __name__ == '__main__':
    unittest.main()