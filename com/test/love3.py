# coding:utf-8
__author__ = 'taohao'
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math


def drawHeart():
    t = np.linspace(0, math.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 3)
    plt.plot(x, y, color='red', linewidth=2, label='h')
    plt.plot(-x, y, color='red', linewidth=2, label='-h')
    plt.xlabel('t')
    plt.ylabel('h')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

    plt.legend()
    plt.show()


drawHeart()