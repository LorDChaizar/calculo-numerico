import unittest
import math
import biseccion as bs

class TestBiseccion(unittest.TestCase):

    def test_biseccion(self):
        f=lambda x:(math.e)**x-3*(x**2)
        self.assertAlmostEqual(bs.biseccion(f, 0, 1, 0.03, 100), 0.847996, places=5)

    def test_biseccion_case1(self):
        f=lambda x: x**2 - 2
        self.assertAlmostEqual(bs.biseccion(f, 0, 2, 0.01, 100), math.sqrt(2), places=2)

    def test_biseccion_case2(self):
        f=lambda x: math.sin(x) - x/2
        self.assertAlmostEqual(bs.biseccion(f, 0, math.pi, 0.0001, 100), 1.895494, places=5)

if __name__ == '__main__':
    unittest.main()