import numpy as np
import matplotlib.pyplot as plt

def h(x, mu, n=1):
    y = x
    for i in range(1, n+1):
        y = mu*y*(1-y)
    return y

x = np.linspace(start=0, stop=1, num=10000)
y = h(x, 3.839, n=3)

plt.plot(x, y, color='black')
plt.plot(x, x, color='black')
plt.show()
