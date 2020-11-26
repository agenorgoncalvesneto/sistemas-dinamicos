import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(figsize=(4,4))

x = np.linspace(start=0, stop=1, num=10000)
y = h(x, mu=3)

axes.plot(x, y, color='black')
axes.plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='h_3.png', bbox_inches='tight')
