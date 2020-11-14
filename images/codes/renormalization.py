import numpy as np
import matplotlib.pyplot as plt

def h(x, mu=3.7, n=2):
    y = x
    for i in range(1, n+1):
        y = mu*y*(1-y)
    return y

def Rh(x, mu=3.7, n=1):
    y = x
    for i in range(1, n+1):
        y = L(h(L_inv(y)))
    return y

def L(x, mu=3.7):    
    p_mu, p_mu_line = (mu - 1)/mu, 1/mu
    y = (x - p_mu)/(p_mu_line - p_mu)
    return y

def L_inv(x, mu=3.7):
    p_mu, p_mu_line = (mu - 1)/mu, 1/mu
    y = (p_mu_line - p_mu)*x + p_mu
    return y

def draw_box(mu=3.7):
    p_mu_line, p_mu = 1/mu, (mu - 1)/mu
    x = np.linspace(start=p_mu_line, stop=p_mu, num=10000)
    const_p_mu = np.zeros(10000) + p_mu
    const_p_mu_line = np.zeros(10000) + p_mu_line
    plt.plot(x, const_p_mu, color='black')
    plt.plot(x, const_p_mu_line, color='black')
    plt.plot(const_p_mu, x, color='black')
    plt.plot(const_p_mu_line, x, color='black')
    
x = np.linspace(start=0, stop=1, num=10000)

y = Rh(x)
plt.subplot(1, 2, 2)
plt.plot(x, y, color='black')
plt.plot(x, x, color='black')

y = h(x)
plt.subplot(1, 2, 1)
plt.plot(x, y, color='black')
plt.plot(x, x, color='black')
draw_box()

plt.show()
