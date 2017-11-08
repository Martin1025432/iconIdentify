# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:11:14 2017

@author: Administrator
"""

import matplotlib.pyplot as plt      #python中强大的画图模块
from aLoadImag_preProcess import *                    #导入和预处理代码写于load.py中，需要用到其中加载和处理后的images28
plt.imshow(images28[1], cmap="gray")
traffic_signs = [1, 2, 3]      #随机选取

for i in range(len(traffic_signs)):     #i from 0 to 3
    plt.subplot(3, 1, i + 1)
    plt.axis('off')
#    plt.imshow(images28[traffic_signs[i]], cmap="gray")
    plt.imshow(images28[traffic_signs[i]], cmap="gray")    
    #你确实必须指定颜色图(即 cmap)，并将其设置为 gray 以给出灰度图像的图表。
    # 这是因为 imshow() 默认使用一种类似热力图的颜色图。
    plt.subplots_adjust(wspace=0.5)       #调整各个图之间的间距

# Show the plot
plt.show()