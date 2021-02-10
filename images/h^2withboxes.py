import numpy as np
from matplotlib import pyplot as plt


def h(x, mu, n=1):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
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

mu = [[2.75, 3, 3.25], [3.5, 3.75, 4]]
x = np.linspace(start=0, stop=1, num=10000)
for i in range(2):
    for j in range(3):
        y = h(x, mu[i][j], 2)
        axes[i][j].plot(x, y, color='black')
        axes[i][j].plot(x, x, color='black', linewidth=0.5)
        draw_box(mu[i][j], axes[i][j])

figure.savefig(fname='h^2withboxes.png', bbox_inches='tight')
