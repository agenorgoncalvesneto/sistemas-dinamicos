import numpy as np
from matplotlib import pyplot as plt


def h(x, mu=4, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

def T(x, n=1):
    y = x
    for k in range(n):
        y = 1 - np.abs(2*y - 1)
    return y

def draw_box(mu, axes):
    p_mu_line, p_mu = 1/mu, (mu - 1)/mu
    x = np.linspace(start=p_mu_line, stop=p_mu, num=10000)
    const_p_mu = np.zeros(10000) + p_mu
    const_p_mu_line = np.zeros(10000) + p_mu_line
    axes.plot(x, const_p_mu, color='black', linewidth=0.5)
    axes.plot(x, const_p_mu_line, color='black', linewidth=0.5)
    axes.plot(const_p_mu, x, color='black', linewidth=0.5)
    axes.plot(const_p_mu_line, x, color='black', linewidth=0.5)


figure, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,8), sharex=True, sharey=True)

x = np.linspace(start=0, stop=1, num=10000)

for j in range(3):
    y = h(x, n=j+1)
    axes[1][j].plot(x, y, color='black')
    axes[1][j].plot(x, x, color='black', linewidth=0.5)

for j in range(3):
    y = T(x, n=j+1)
    axes[0][j].plot(x, y, color='black')
    axes[0][j].plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='T-and-h_4.png', bbox_inches='tight')
