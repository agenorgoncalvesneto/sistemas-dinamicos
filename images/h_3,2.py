import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharey=True)

x = np.linspace(start=0, stop=1, num=10000)
for k in range(2):
    y = h(x, 3.2, k+1)
    axes[k].plot(x, y, color='black')
    axes[k].plot(x, x, color='black', linewidth=0.5)

y = h(x, 3.2, 4)
axes[2].plot(x, y, color='black')
axes[2].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='h_3,2.png', bbox_inches='tight')
