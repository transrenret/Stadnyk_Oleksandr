import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (np.sin(x/2) * np.cos(2*y))

x = np.linspace(-2 * np.pi, 2 * np.pi, 30)
y = np.linspace(-2 * np.pi, 2 * np.pi, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()