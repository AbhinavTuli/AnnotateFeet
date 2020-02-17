#this overlays ground truth and unet output over the original image 

import cv2

def overlayFoot(ogImg,gtImg,outImg,output):
    for i in range(gtImg.shape[0]):
        for j in range(gtImg.shape[1]):
            if gtImg[i, j, 1] == 1 :
                ogImg[i, j, 2] = 255          #if groundtruth is 1, turn the blue band to max value
            if outImg[i, j, 2] >100:
                ogImg[i, j, 0] = 255          #if outimg is > 100 , turn the red band in the original image to max


    cv2.imwrite(output, ogImg)

# ogImg = cv2.imread("footprint.png")
# outImg = cv2.imread("output.png")
# gtImg = cv2.imread("groundtruth.png")
# overlayFoot(ogImg,gtImg,outImg,"try.png")