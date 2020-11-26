import numpy as np
from matplotlib import pyplot as plt

def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(figsize=(12,4))

mu = np.linspace(start=2, stop=4, num=10000)
for k in range(100, 300):
    y = h(1/2, mu, n=k)
    axes.scatter(mu, y, s=0.01, color='black', marker='.')
    
figure.savefig(fname='period-doubling.png', bbox_inches='tight')
plt.show()
