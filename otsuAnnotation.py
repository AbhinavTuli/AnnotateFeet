#an attempt to use OTSU to get better ground truth, however manually setting the threshold values as done before works out better.
import random
import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageFilter
files = os.listdir("/Users/abhinav/Documents/KT/pngfootprint/")
for file in files:
    img = cv2.imread("/Users/abhinav/Documents/KT/pngfootprint/"+file)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret,th1 = cv2.threshold(img_grey,127,255,cv2.THRESH_BINARY)
    th = cv2.threshold(img_grey, 0, 255, cv2.THRESH_OTSU)[1]
    # cv2.imwrite("./1/"+file,th1)
    #pixels=th.load()
    
    #sort the boundary
    for i in range(th.shape[0]): 
        for j in range(th.shape[1]):
            if i<10 or j<10:
                th[i,j]=0

    th = cv2.medianBlur(th, 3)
    th = cv2.medianBlur(th, 3)
    cv2.imwrite("./2/"+file,th)
    # cv2.imwrite("./3/"+file,th3)
