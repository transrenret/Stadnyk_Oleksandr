import numpy as np
import matplotlib.pyplot as plt
def ctg(x):
    return 1 / np.tan(x)

fig = plt.figure()
x = np.linspace(-2, 8, 100)
plt.subplot(2, 2, 1)
plt.plot(x, np.cos(x))

plt.subplot(2, 2, 2)
plt.plot(x, np.tan(x))

plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x))

plt.subplot(2, 2, 4)
plt.plot(x, ctg(x))
plt.show()