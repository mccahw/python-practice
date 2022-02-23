from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.title("The 'sine' function")
plt.show()

plt.plot(y, x)
plt.grid()
plt.title("The... uhhh... something else function...")
plt.ylabel("sin(x)")
plt.xlabel("x")
plt.show()

z = np.cos(x)
plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.legend()
plt.grid()
plt.show()

theta = np.linspace(0, 2*np.pi, 1000)
a = np.cos(theta)
b = np.sin(theta)
plt.plot(a, b)
plt.title("A circle")
plt.grid()
plt.show()

a = np.cos(theta) * np.cos(2*theta)
b = np.sin(theta) * np.cos(2*theta)
plt.plot(a, b)
plt.title("woah")
plt.show()