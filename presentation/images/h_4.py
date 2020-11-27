import numpy as np
from matplotlib import pyplot as plt

def h(x, mu=4, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(9,3), sharey=True)

x = np.linspace(start=0, stop=1, num=10000)
for k in range(3):
    y = h(x, n=k+1)
    axes[k].plot(x, y, color='black')
    axes[k].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='h_4.png', bbox_inches='tight')
