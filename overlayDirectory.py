from overlayFoot import overlayFoot
import os
from PIL import Image
#dataset =os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/")
# groundtruth=os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/")
# output=os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Output 1st Epoch/")
def overlayDir(datasetDir,gtDir,outDir,outputDir):
    dataset=os.listdir(datasetDir)
    for file in dataset:
        print(file)
        try:
            ds=Image.open(datasetDir+file)
            gt=Image.open(gtDir+file)
            out=Image.open(outDir+file)
            outputPath=outputDir+file
            overlayFoot(ds,gt,out,outputPath)
        except Exception as e:
            print(e)

datasetDir="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/"
gtDir="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/"
outDir="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Output 1st Epoch/"
outputDir="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Overlay/"
overlayDir(datasetDir,gtDir,outDir,outputDir)