import unittest
from main import Matrix

class TestMatrix(unittest.TestCase):

    def test_initialization(self):
        m = Matrix()
        self.assertEqual(m.length, 0)
        self.assertEqual(m.A, [])

    def test_average_calculation(self):
        m = Matrix()
        m.C = [[10, 20], [30, 40]] 
        # (10+20+30+40) / 4 = 25
        result = m.get_average()
        self.assertEqual(result, 25.0)

    def test_multiply_logic(self):
        m = Matrix()
        m.length = 2
        m.A = [[1, 1], [1, 1]]
        m.B = [[2, 2], [2, 2]]
        
        m.multiply()
        
        expected = [[4, 4], [4, 4]]
        self.assertEqual(m.C, expected)

if __name__ == '__main__':
    unittest.main()
