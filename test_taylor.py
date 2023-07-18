import unittest
import math
import taylor

class TestPolinomioTaylor(unittest.TestCase):
    
    def test_sin_0(self):
        f = lambda x: math.sin(x)
        pol = taylor.polinomio_taylor(f, 0, 4)
        x = 0.0
        expected = f(x)
        result = pol(x)
        self.assertAlmostEqual(expected, result)
        
    def test_sin_1(self):
        f = lambda x: math.sin(x)
        pol = taylor.polinomio_taylor(f, 0, 4)
        x = 1.0
        expected = f(x)
        result = pol(x)
        self.assertAlmostEqual(expected, result, places=4)
        
    def test_exp_0(self):
        f = lambda x: math.exp(x)
        pol = taylor.polinomio_taylor(f, 0, 4)
        x = 0.0
        expected = f(x)
        result = pol(x)
        self.assertAlmostEqual(expected, result)
        
    def test_exp_1(self):
        f = lambda x: math.exp(x)
        pol = taylor.polinomio_taylor(f, 0, 4)
        x = 1.0
        expected = f(x)
        result = pol(x)
        self.assertAlmostEqual(expected, result, places=4)

if __name__ == '__main__':
    unittest.main()