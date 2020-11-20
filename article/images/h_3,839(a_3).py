import numpy as np
from matplotlib import pyplot as plt

def h(x, mu=3.839, n=3):
    y = x
    for k in range(n):
        y = mu*y*(1 - y)
    return y

figure, axes = plt.subplots(figsize=(4,4))

a3 = 0.959299
b3 = 0.953837
b3_line = 0.963

x = np.linspace(start=b3-0.0019, stop=b3_line, num=10000)
y = h(x, 3.839, n=3)
x, y = x[y>0.952], y[y>0.952]
x, y = x[y<0.96], y[y<0.96]
axes.plot(x, y, color='black')
axes.plot(x, x, color='black', linewidth=0.5)


#axes.scatter(a3, h(a3), color='black')
figure.savefig(fname='h_3,839(a_3).png', bbox_inches='tight')
plt.show()
