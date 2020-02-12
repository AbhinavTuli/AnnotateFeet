#Used to manually go through each image and try setting threshold
#morphological closing was also performed to make the annotations better (code missing)
import random
import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageFilter

img = Image.open("/Users/abhinav/Documents/KT/footprint/abc.tif").convert('L')
threshold=80

img = img.point(lambda p: p > threshold and 255) 
pixels=img.load()
    
    #sort the boundary
for i in range(img.size[0]): 
    for j in range(img.size[1]):
        if i<10 or j<10:
            pixels[i,j]=0

img = img.filter(ImageFilter.MedianFilter(size = 3))
img = img.filter(ImageFilter.MedianFilter(size = 3))


cv2.imwrite( "/Users/abhinav/Documents/KT/annotation/abc.tig",img )
