import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,11000)
# print(x)
y1 = np.abs(x)
y2 = y1-1
y3 = np.square(y2)#: 计算各元素的平方
y4 = 1 - y3
y = np.sqrt(y4)
y = np.arccos(1-y1) - np.pi
# print(y2)
# np.sqrt(a) : 计算各元素的平方根
# for i in range(-5,5):
#     j = abs(i)
#     y.append(j)

plt.plot(x,y)
plt.show()