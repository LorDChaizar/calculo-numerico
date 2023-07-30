def euler_method(f, x0, y0, h, n):
    """
    Implementación del método de Euler para resolver ecuaciones diferenciales de primer orden.

    Parámetros:
        - f: La función que representa dy/dx.
        - x0: Valor inicial de x.
        - y0: Valor inicial de y.
        - h: Tamaño del paso.
        - n: Número de pasos.

    Devuelve:
        - Un diccionario con los valores de x y y en cada paso.
    """
    results = {'x': [x0], 'y': [y0]}
    x, y = x0, y0

    for _ in range(n):
        y += h * f(x, y)
        x += h
        results['x'].append(x)
        results['y'].append(y)

    return results

# Ejemplo de uso:
def example_function(x, y):
    return x + y  # Ejemplo: dy/dx = x + y

x0 = 0  # Valor inicial de x
y0 = 1  # Valor inicial de y
h = 0.1  # Tamaño del paso
n = 10  # Número de pasos

results_dict = euler_method(example_function, x0, y0, h, n)
print(results_dict)
