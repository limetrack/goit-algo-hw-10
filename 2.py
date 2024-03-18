import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, samples=10000):
    x_random = np.random.uniform(a, b, samples)
    y_random = np.random.uniform(a, func(b), samples)
    below_function = y_random < func(x_random)
    integral_area = below_function.sum() / samples * (b - a) * (func(b) - a)
    return integral_area

# Параметри інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтегралу методом Монте-Карло
mc_integral = monte_carlo_integration(f, a, b)

# Аналітичне обчислення інтегралу за допомогою SciPy
scipy_integral, error = spi.quad(f, a, b)

(mc_integral, scipy_integral, error)
