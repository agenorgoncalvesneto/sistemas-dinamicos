import numpy as np
import matplotlib.pyplot as plt

def h(x, mu, n=1):
    y = x
    for i in range(1, n+1):
        y = mu*y*(1-y)
    return y

x = np.linspace(start=0.5, stop=0.8, num=10000)

mu = [2.9, 3, 3.1]
for k in range(1, 4):
    y = h(x, mu[k-1], 2)
    plt.subplot(1, 3, k)
    plt.plot(x, y, color='black')
    plt.plot(x, x, color='black')
    
plt.show()
