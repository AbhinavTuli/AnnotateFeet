#the annotations are stored as binary images having 0 or 1. This helps in visualizing them.
from PIL import Image
import os

files =os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/")

for file in files:
    try:
        img = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/"+file)
        pixels=img.load()
        ct=0
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i,j] ==1:
                    ct+=1
                    pixels[i,j]=255
        print(ct)
        #img.show()
        img.save('/Users/abhinav/Documents/Foot Data and Manipulations/Testing/ViewAugAnns/'+file)
    except:
        print("nope")
