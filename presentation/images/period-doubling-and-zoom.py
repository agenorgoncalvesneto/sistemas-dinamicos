import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y


def draw_square(axes, xmin, xmax, ymin, ymax):    
    x = np.linspace(start=xmin, stop=xmax, num=10000)
    axes.plot(x, np.zeros(10000)+ymin, color='black', linewidth=1)
    axes.plot(x, np.zeros(10000)+ymax, color='black', linewidth=1)
    y = np.linspace(start=ymin, stop=ymax, num=10000)
    axes.plot(np.zeros(10000)+xmin, y, color='black', linewidth=1)
    axes.plot(np.zeros(10000)+xmax, y, color='black', linewidth=1)


figure1, axes1 = plt.subplots(figsize=(12,4))
figure2, axes2 = plt.subplots(nrows=1, ncols=2, figsize=(12,4))

draw_square(axes1, 3.41, 3.65, 0.745, 0.925)
draw_square(axes1, 3.82, 3.86, 0.125, 0.183)

mu = np.linspace(start=2, stop=4, num=10000)
mu20 = np.linspace(start=3.35, stop=3.65, num=3000)
mu21 = np.linspace(start=3.83, stop=3.855, num=250)
for k in range(100, 300):
    y = h(1/2, mu, n=k)
    axes1.scatter(mu, y, s=0.01, color='black', marker='.')
    
    y20 = h(1/2, mu20, n=k)
    axes2[0].scatter(mu20[y20>0.75], y20[y20>0.75], s=0.01, color='black', marker='.')

    y21 = h(1/2, mu21, n=k)
    axes2[1].scatter(mu21[y21<0.185], y21[y21<0.185], s=0.01, color='black', marker='.')
    
figure1.savefig(fname='period-doubling-and-zoom1.png', bbox_inches='tight')
figure2.savefig(fname='period-doubling-and-zoom2.png', bbox_inches='tight')
##plt.show()
