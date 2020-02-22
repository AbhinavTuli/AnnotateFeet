#this overlays ground truth and unet output over the original image 

from PIL import Image

def overlayFoot(ogImg,gtImg,outImg,output):
    outImg=outImg.convert('L')
    threshold=200
    outImg = outImg.point(lambda p: p > threshold and 255) 

    # ogPixels=ogImg.load()
    outPixels=outImg.load()
    gtPixels=gtImg.load()
    for i in range(ogImg.size[0]): 
            for j in range(ogImg.size[1]):
                if outPixels[i,j]!=0:
                    current_color = ogImg.getpixel( (i,j) )
                    new_color=(255,current_color[1],current_color[2])
                    ogImg.putpixel( (i,j), new_color)
                if gtPixels[i,j]!=0:
                    current_color = ogImg.getpixel( (i,j) )
                    new_color=(current_color[0],current_color[1],255)
                    ogImg.putpixel( (i,j), new_color)
    ogImg.save(output)


ogImg = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/overlay/footprint.png")
outImg = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/overlay/output.png")
gtImg = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/overlay/groundtruth.png")
overlayFoot(ogImg,gtImg,outImg,"try.png")