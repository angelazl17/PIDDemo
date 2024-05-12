# Created by Li Zhao at 5/5/2024
# @Author   : 初见
# @File     : PIDPlot.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np

def drawPlot(x,y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

# X 是一个 numpy 数组，包含了从 0 到 2π 等间隔的 200 个值
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
# drawPlot(x,y)

def demoDrawSubplot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    fig = plt.figure()
    # These are subplot grid parameters encoded as a single integer. 
    # For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
    # Alternative form for add_subplot(111) is add_subplot(1, 1, 1).
    fig.add_subplot(111)
    plt.scatter(x, y)
    plt.show()