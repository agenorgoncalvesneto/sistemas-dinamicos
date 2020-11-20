import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharey=True)

mu = [2.9, 3, 3.1]
x = np.linspace(start=0.5, stop=0.8, num=3000)
for k in range(3):
    y = h(x, mu[k], 2)
    axes[k].plot(x, y, color='black')
    axes[k].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='h_3^2.png', bbox_inches='tight')
