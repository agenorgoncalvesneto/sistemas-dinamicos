import numpy as np
from matplotlib import pyplot as plt


def h(x, mu=3.75, n=2):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y


def Rh(x, mu=3.75):
    y = L(h(L_inv(x)))
    return y


def L(x, mu=3.75):    
    p_mu_line, p_mu = 1/mu, (mu - 1)/mu
    y = (x - p_mu)/(p_mu_line - p_mu)
    return y


def L_inv(x, mu=3.75):
    p_mu_line, p_mu = 1/mu, (mu - 1)/mu
    y = (p_mu_line - p_mu)*x + p_mu
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


figure, axes = plt.subplots(figsize=(4,4))

x = np.linspace(start=0, stop=1, num=10000)

y = Rh(x)
axes.plot(x, y, color='black')
axes.plot(x, x, color='black', linewidth=0.5)

figure.savefig(fname='renormalization.png', bbox_inches='tight')
