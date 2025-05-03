from math import *
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3*np.pi, +3*np.pi, 60)
y = np.sin(x)
z = np.cos(x)
plt.title("Синусоида и Косинусоида")
plt.plot(x, y, 'r--', label='Sin')  
plt.plot(x, z, 'g--', label='Cos')  
plt.xlabel("Oсь X")
plt.ylabel("Ось Y")
plt.legend()
plt.show
