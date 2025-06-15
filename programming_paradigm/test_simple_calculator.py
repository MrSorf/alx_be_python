import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 1), 3)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(0, 4), 0)
        self.assertIsNone(self.calc.divide(4, 0))
    
if __name__ == '__main__':
    unittest.main()