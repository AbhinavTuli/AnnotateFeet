#apply the segmentation mask obtained from the unet to get only the feet and remove the background

from PIL import Image

def applyMask(img,mask,output):
    mask=mask.convert('L')
    threshold=200
    mask = mask.point(lambda p: p > threshold and 255) 

    imgPixels=img.load()
    maskPixels=mask.load()
    ct1=ct2=0
    for i in range(img.size[0]): 
            for j in range(img.size[1]):
                if maskPixels[i,j]==0:
                    imgPixels[i,j]=0
    img.save(output)


#Tesing the fn

# img = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/overlay/footprint.png")
# mask=Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/overlay/output.png")
# applyMask(img,mask,"a.png")