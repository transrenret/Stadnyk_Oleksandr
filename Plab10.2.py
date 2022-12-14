import numpy as np
import matplotlib.pyplot as plt

x = [8,2,7,4,3,6]
y = [9,11,1,5,6,6]
z = [5,9,4,5,4,6]
fig = plt.figure()
plt.title("Завдання №2")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, label='x')
plt.plot(y, color='red', linestyle='--', label='y', marker='o', markersize=8, markerfacecolor = 'green',  markeredgecolor = 'green')
plt.plot(z, color='red', linestyle='-', label='z', marker='^', markersize=8, markerfacecolor = 'black',  markeredgecolor = 'black')
plt.legend()
plt.show()
