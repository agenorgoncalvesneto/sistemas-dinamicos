import numpy as np
from matplotlib import pyplot as plt

def T(x, n=1):
    y = x
    for k in range(n):
        y = 1 - np.abs(2*y - 1)
    return y

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(9,3), sharey=True)

x = np.linspace(start=0, stop=1, num=10000)
for k in range(3):
    y = T(x, k+1)
    axes[k].plot(x, y, color='black')
    axes[k].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='tent-map.png', bbox_inches='tight')
