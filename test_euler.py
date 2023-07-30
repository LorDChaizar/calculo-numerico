import unittest
import euler

def example_function(x, y):
    return x + y  # Ejemplo: dy/dx = x + y

def another_example_function(x, y):
    return x**2 - y  # Ejemplo: dy/dx = x^2 - y

class TestEulerMethod(unittest.TestCase):
    def test_euler_method_example_function(self):
        x0 = 0
        y0 = 1
        h = 0.1
        n = 5
        expected_result = {'x': [0, 0.1, 0.2, 0.3, 0.4, 0.5],
                           'y': [1, 1.1, 1.22, 1.352, 1.5062, 1.68382]}
        result = euler.euler_method(example_function, x0, y0, h, n)
        self.assertEqual(result, expected_result)

    def test_euler_method_another_example_function(self):
        x0 = 0
        y0 = 2
        h = 0.2
        n = 4
        expected_result = {'x': [0, 0.2, 0.4, 0.6, 0.8],
                           'y': [2, 1.96, 1.8008, 1.497632, 1.04177152]}
        result = euler.euler_method(another_example_function, x0, y0, h, n)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
