import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math

pi = math.pi

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(-1,1,0.0625)
Y = np.arange(-1,1,0.0625)
X, Y = np.meshgrid(X, Y)
Z = (1/4)+(1/4)*np.cos(2*pi*X)-(1/4)*np.cos(2*pi*Y)-(1/8)*np.cos(2*pi*X+2*pi*Y)+(1/8)*np.cos(2*pi*X-2*pi*Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()