import numpy as np
import matplotlib.pyplot as plt

def h(x, mu, n=2):
    y = x
    for i in range(1, n+1):
        y = mu*y*(1-y)
    return y

def draw_box(mu):
    p_mu_line, p_mu = 1/mu, (mu - 1)/mu
    x = np.linspace(start=p_mu_line, stop=p_mu, num=10000)
    const_p_mu = np.zeros(10000) + p_mu
    const_p_mu_line = np.zeros(10000) + p_mu_line
    plt.plot(x, const_p_mu, color='black')
    plt.plot(x, const_p_mu_line, color='black')
    plt.plot(const_p_mu, x, color='black')
    plt.plot(const_p_mu_line, x, color='black')
    
x = np.linspace(start=0, stop=1, num=10000)

mu_values = [2.75, 3, 3.25, 3.5, 3.75, 4]
for k in range(6):
    mu = mu_values[k]
    y = h(x, mu)
    plt.subplot(2, 3, k+1)
    plt.plot(x, y, color='black')
    plt.plot(x, x, color='black')
    #plt.plot(x, x, 'r--', color='black')
    draw_box(mu)

plt.show()
