#this goes through the entire original dataset and performs thresholding taking 80 as the threshold in an attempt to generate the ground truth values.
#not all the annotations turn out perfect and thus, we use oneFeet.py to manually fix individual feet annotations.

import random
import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageFilter
files = os.listdir("/home/kr08rises/footprint_dataset/")
for file in files:
    img = Image.open("/home/kr08rises/footprint_dataset/"+file).convert('L')
    threshold=80
    img = img.point(lambda p: p > threshold and 255) 
    #cordinate = x, y = 151, 200
    pixels=img.load()
    
    #sort the boundary
    for i in range(img.size[0]): 
        for j in range(img.size[1]):
            if i<10 or j<10:
                pixels[i,j]=0

    img = img.filter(ImageFilter.MedianFilter(size = 3))
    img = img.filter(ImageFilter.MedianFilter(size = 3))
    #img.save('greyscale2.png')

    pixels=img.load()
    ann_img = np.zeros((img.size[1],img.size[0],1)).astype('uint8')
    #ann_img[ 3 , 4 ] = 1 # this would set the label of pixel 3,4 as 1
    #ct=0
    for i in range(img.size[0]): 
        for j in range(img.size[1]):
            if(pixels[i,j]>150):
                ann_img[j,i]=1
                #ct+=1

    cv2.imwrite( "/Users/abhinav/Documents/KT/annotation/"+file,ann_img )

# img = img.filter(ImageFilter.MedianFilter(size = 3))

# img = img.filter(ImageFilter.FIND_EDGES())
# pixels=img.load()

# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         if pixels[i,j] == 255:
#             l.append([i,j])
#        if i<img.size[0] and i>=0 & j<img.size[1] and j>=0 and pixels([i][j])==255:

# img = img.filter(ImageFilter.FIND_EDGES)
