import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4), sharey=True)

x = np.linspace(start=0, stop=1, num=10000)

y = h(x, 3.2, 2)
axes[0].plot(x, y, color='black')
axes[0].plot(x, x, color='black', linewidth=0.5)

y = h(x, 3.2, 4)
axes[1].plot(x, y, color='black')
axes[1].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='h_3,2.png', bbox_inches='tight')
