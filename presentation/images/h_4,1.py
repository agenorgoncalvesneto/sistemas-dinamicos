import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

def draw_square(axes, xmin=0, xmax=1, ymin=0, ymax=1):    
    x = np.linspace(start=xmin, stop=xmax, num=10000)
    axes.plot(x, np.zeros(10000)+ymin, color='black', linewidth=0.5)
    axes.plot(x, np.zeros(10000)+ymax, color='black', linewidth=0.5)
    y = np.linspace(start=ymin, stop=ymax, num=10000)
    axes.plot(np.zeros(10000)+xmin, y, color='black', linewidth=0.5)
    axes.plot(np.zeros(10000)+xmax, y, color='black', linewidth=0.5)

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharey=True)

for k in range(3):
    x = np.linspace(start=0, stop=1, num=10000)
    y = h(x, mu=4.1, n=k+1)
    
    axes[k].plot(x, x, color='black', linewidth=0.5)
    
    x[y < -0.15] = np.nan
    x[y > 1.1] = np.nan
    y[y < -0.15] = np.nan
    y[y > 1.1] = np.nan
    axes[k].plot(x, y, color='black')
    
    draw_square(axes[k])
    x[y < 0] = np.nan
    x[y > 1] = np.nan
    axes[k].plot(x, np.zeros(shape=x.shape), color='red', linewidth=1.5)
    


figure.savefig(fname='h_4,1.png', bbox_inches='tight')
