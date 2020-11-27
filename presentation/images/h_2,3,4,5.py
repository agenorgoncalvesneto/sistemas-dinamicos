import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y


figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharey=True)

for k in range(3):
    x = np.linspace(start=0, stop=1, num=10000)
    y = h(x, mu=k+2)
    
    axes[k].plot(x, x, color='black', linewidth=0.5)
    axes[k].plot(x, y, color='black', linewidth=1)
    


figure.savefig(fname='h_2,3,4,5.png', bbox_inches='tight')
