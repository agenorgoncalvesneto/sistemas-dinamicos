import numpy as np
from matplotlib import pyplot as plt

def E(x, lbda, n=1):
    y = x
    for k in range(n):
        y = np.exp(x + lbda)
    return y

figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharey=True)

lbda = [-1.1, -1, -0.9]
x = np.linspace(start=0, stop=2, num=20000)
for k in range(3):
    y = E(x, lbda[k])
    axes[k].plot(x, y, color='black')
    axes[k].plot(x, x, color='black', linewidth=0.5)
    
figure.savefig(fname='e_lambda.png', bbox_inches='tight')
