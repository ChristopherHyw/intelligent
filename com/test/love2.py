import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,11000)
y1 = np.sqrt(np.cos(x))
y2 = np.cos(200*x)
y3 = np.sqrt(np.abs(x)-0.7)
y4 = (4-x*x)**0.01
y = y1*y2+y3*y4
plt.plot(x,y)
plt.show()