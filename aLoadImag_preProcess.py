# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:06:52 2017

@author: Administrator
"""

import os                    #python中的os模块用于处理文件和目录
import skimage               #python中的skimage模块用于图像处理
import numpy as np           #python中的numpy模块用于科学计算
from skimage import data,transform
from skimage.color import rgb2gray     #rgb2gray将图片转化为灰度
import matplotlib.pyplot as plt      #python中强大的画图模块
#here data_directory="/home/zhangxueying/image/TrafficSigns/Training"
def load_data(data_directory):
    directories=[d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory,d))]
    #d is every classification file
    labels=[]
    images=[]
    for d in directories:
        #每一类的路径
        label_directory=os.path.join(data_directory,d)
        file_names=[os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".jpg")]
        #file_names is every photo which is end with ".ppm"
        for f in file_names:
            images.append(skimage.data.imread(f))   #read image
            labels.append(int(d))                   #read label
    return images,labels

#images and labels are list

ROOT_PATH="D:"
train_data_directory=os.path.join(ROOT_PATH,"image/ng")
test_data_directory=os.path.join(ROOT_PATH,"image/ng")
images,labels=load_data(train_data_directory)

# Rescale the images in the `images` array
images28 = [transform.resize(image, (1920, 1080)) for image in images]
# Convert `images28` to an array
images28 = np.array(images28)
## Convert `images28` to grayscale
images28 = rgb2gray(images28)

