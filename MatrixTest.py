'''
@author William Ray Johnson
9/4/17
'''

import unittest

import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix2x2 = Matrix.Matrix(2, 2, [7, 19, 8, 3])
        self.matrix3x3 = Matrix.Matrix(3, 3, [2, 1, 1, 3, 2, 1, 2, 1, 2])
    
    def testBuildMatrix2x2(self):
        matrix = Matrix.Matrix(2, 2, [1,1,1,1])
        expectedMatrixValue = [[1,1],
                               [1,1]]
        actualMatrixValue = matrix.getMatrixValue()
        
        self.assertEqual(actualMatrixValue, expectedMatrixValue)

    def testBuildMatrix3x3(self):
        matrix = Matrix.Matrix(3, 3, [1,1,1,1,1,1,1,1,1])
        expectedMatrixValue = [[1,1,1],
                               [1,1,1],
                               [1,1,1]]
        actualMatrixValue = matrix.getMatrixValue()
        
        self.assertEqual(actualMatrixValue, expectedMatrixValue)
    
    def testMultiply2x2(self):
        matrixToMultiply = Matrix.Matrix(2, 1, [5, 17])
        expectedMatrixValue = [[358],
                               [91]]
        actualMatrixValue = self.matrix2x2.multiply(matrixToMultiply).getMatrixValue()
        
        self.assertEqual(actualMatrixValue, expectedMatrixValue)
        
    def testMultiply3x3(self):
        matrixToMultiply = Matrix.Matrix(3, 1, [5, 17, 14])
        expectedMatrixValue = [[41],
                               [63],
                               [55]]
        actualMatrixValue = self.matrix3x3.multiply(matrixToMultiply).getMatrixValue()
        
        self.assertEqual(actualMatrixValue, expectedMatrixValue)
        
    def testGetSize(self):
        self.assertEqual(self.matrix2x2.getSize(), "2x2")
        self.assertEqual(self.matrix3x3.getSize(), "3x3")
        
    def testEquals(self):
        matrixA = Matrix.Matrix(2, 2, [1,2,3,4])
        matrixB = Matrix.Matrix(2, 2, [1,2,3,4])
        
        self.assertEqual(matrixA, matrixB)
        
    def testCalcAdjugateMatrix2x2(self):
        expectedAdjugateMatrix = Matrix.Matrix(2,2,[3,-19,-8,7])
        actualAdjugateMatrix = self.matrix2x2.calcAdjugateMatrix()
        
        self.assertEqual(actualAdjugateMatrix.getMatrixValue(), expectedAdjugateMatrix.getMatrixValue())
        
    def testCalcAdjugateMatrix3x3(self):
        expectedAdjugateMatrix = Matrix.Matrix(3,3,[3,-1,-1,-4,2,1,-1,0,1])
        actualAdjugateMatrix = self.matrix3x3.calcAdjugateMatrix()
        
        self.assertEqual(actualAdjugateMatrix.getMatrixValue(), expectedAdjugateMatrix.getMatrixValue())
        
    def testCalcDeterminant2x2(self):
        expectedDeterminant = 9**-1
        actualDeterminant = Matrix.Matrix(2,2,[3,3,2,5]).calcDeterminant()
        
        self.assertEqual(actualDeterminant, expectedDeterminant)
        
    def testCalcDeterminant3x3(self):
    

if __name__ == '__main__':
    unittest.main()