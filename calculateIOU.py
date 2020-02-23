#used to get the test case accuracy
import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageFilter
import statistics

def calcIOU(gtDir,outDir):
    arr=[]
    files = os.listdir(gtDir)
    for file in files:
        try:
            Intersection=set()
            Union=set()

            gt = cv2.imread(gtDir+file)
            # gtPixels=gt.load()
            print(file)
            out = cv2.imread(outDir+file)
            # out.show()
            # exit()
            # outPixels=out.load()
            # data = np.asarray(out)
            # print(data)
            # exit()
            for i in range(gt.shape[0]): 
                for j in range(gt.shape[1]):
                    if gt[i,j,1]==1 and out[i,j,2]>100:
                        Intersection.add((i,j))
                    if gt[i,j,1]==1 or out[i,j,2]>100:
                        Union.add((i,j))
            iou=len(Intersection)/len(Union)
            arr.append(iou)
            print(len(Intersection))
            print(len(Union))
            print(iou)
        except Exception as e:
            print(e)
    #print(arr)
    return statistics.mean(arr)

print(calcIOU("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/","/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Output 2nd Epoch/"))
    

