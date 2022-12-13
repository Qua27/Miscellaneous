import matplotlib.pyplot as plt
from numpy import sin, cos, pi, linspace


# Original function f(x)
def o_func(x):
    return (x - 2) * (x >= 0)


# Series element a1(x, n)
def a1(x, n):
    return (4 / (pi ** 2 * n ** 2)) * ((-1) ** n - 1) * cos(pi * n * x / 4)


# Series element a2(x, n)
def a2(x, n):
    return (-2 / (pi * n)) * ((-1) ** n + 1) * sin(pi * n * x / 4)


def a(x, n):
    return a1(x, n) + a2(x, n)


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
