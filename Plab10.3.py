import matplotlib.pyplot as plt

x = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]

plt.title("Завдання №3")
plt.xlabel("x")
plt.ylabel("y")

plt.hist(x, 30, color = 'blue')


plt.show()