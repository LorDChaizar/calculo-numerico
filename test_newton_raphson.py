import unittest
from math import *
import newton_raphson as nr

class TestNewtonRaphson(unittest.TestCase):

    def test_newton_raphson_case1(self):
        f = lambda x: x**2 - 10
        self.assertAlmostEqual(nr.newton_rapson(f, 3, 0.001, 100), sqrt(10), places=3)

    def test_newton_raphson_case2(self):
        f = lambda x: sin(x) - x/2
        self.assertAlmostEqual(nr.newton_rapson(f, 1, 0.0001, 100), 1.895494, places=5)

if __name__ == '__main__':
    unittest.main()