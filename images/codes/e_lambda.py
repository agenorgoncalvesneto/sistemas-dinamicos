import numpy as np
import matplotlib.pyplot as plt

def e(x, c, n=1):
    y = x
    for i in range(1, n+1):
        y = np.exp(x + c)
    return y

x = np.linspace(start=-1, stop=3, num=10000)

y = e(x, -1.5, 3)
plt.subplot(1, 3, 1)
plt.plot(x, y, color='black')
plt.plot(x, x, color='black', linewidth=0.5)

y = e(x, -1, 3)
plt.subplot(1, 3, 2)
plt.plot(x, y, color='black')
plt.plot(x, x, color='black', linewidth=0.5)

y = e(x, -0.5, 3)
plt.subplot(1, 3, 3)
plt.plot(x, y, color='black')
plt.plot(x, x, color='black', linewidth=0.5)

plt.show()
