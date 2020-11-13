import numpy as np
import matplotlib.pyplot as plt

def h(x, mu, n=1):
    y = x
    for i in range(1, n+1):
        y = mu*y*(1-y)
    return y

x = np.linspace(start=2, stop=4, num=20000)
for k in range(100, 500):
    y = h(1/2, x, n=k)
    plt.scatter(x, y, s=0.01, color='black', marker='.')
plt.show()
