import matplotlib.pyplot as plt
from numpy import cos, pi, linspace


# Original function f(x)
def o_func(x):
    return abs(x) - 2


# Series element a(x, n)
def a(x, n):
    return (8 / (pi ** 2 * n ** 2)) * ((-1) ** n - 1) * cos(pi * n * x / 4)


# Partial sum expression s(x, n)
def partial_sum(x, n):
    return sum([a(x, i) for i in range(1, n + 1)])


x = list(linspace(-4, 4, 200))
fig = plt.figure()
graph = fig.add_subplot()
plt.plot(x, [o_func(i) for i in x], label="Original")
print("Enter n:")
n = int(input())  # n-th partial sum
graph.set_title(f"Fourier series partial sum for n = {n}")
graph.plot(x, [partial_sum(i, n) for i in x], label="Approximation")
graph.grid()
graph.legend()
plt.show()
