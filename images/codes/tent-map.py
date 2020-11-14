import numpy as np
import matplotlib.pyplot as plt

def T(x, n=1):
    y = x
    for i in range(1, n+1):
        y = 1 - np.abs(2*y - 1)
    return y

x = np.linspace(start=0, stop=1, num=10000)

for k in range(1, 4):
    y = T(x, k)
    plt.subplot(1, 3, k)
    plt.plot(x, y, color='black')
    plt.plot(x, x, color='black', linewidth=0.5)

plt.show()
