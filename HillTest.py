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
        self.cipher = Hill.Hill()
        
    def testConvertPlainTextToNumber(self):
        expectedPTNumbers = [19, 4, 18, 19]
        actualPTNumbers = self.cipher.convertToNumbers(self.plainText)
        
        self.assertEqual(actualPTNumbers, expectedPTNumbers)
        
if __name__ == '__main__':
    unittest.main()