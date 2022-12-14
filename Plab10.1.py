import numpy as np
import matplotlib.pyplot as plt

a = 22
b = 14
plt.title("Завдання №1")
plt.xlabel("x")
plt.ylabel("y")
x = np.linspace(-3, 3, 100)
y = np.linspace(-10, 10, 100)
y = a * np.log(x) - b * x**3
plt.plot(x, y, linestyle = '-', color='green')

plt.show()