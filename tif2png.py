#the dataset contain images in .tif format which was creating certain issues.
#this helps in converting to png to avoid those
import cv2
import os
from PIL import Image
files = os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/dataset/")
for file in files:
    img = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/dataset/"+file)
    img.save( "/Users/abhinav/Documents/Foot Data and Manipulations/pngDataset/"+file[0:-3]+"png")
