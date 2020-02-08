import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
img = Image.open('greyscale2.png')
pixels=img.load()
ann_img = np.zeros((img.size[0],img.size[1],1)).astype('uint8')
#ann_img[ 3 , 4 ] = 1 # this would set the label of pixel 3,4 as 1

cv2.imwrite( "ann_1.png" ,ann_img )

ct=0
for i in range(img.size[0]): 
    for j in range(img.size[1]):
        if(pixels[i,j]>150):
            ann_img[i,j]=1
            ct+=1
print(ct)