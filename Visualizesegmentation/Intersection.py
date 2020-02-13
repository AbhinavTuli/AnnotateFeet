#this module overlays original image over the output image

import cv2


origimg = cv2.imread("footprint.png")
#origimg = origimg.copyTo()
# cv2.imshow('original image',origimg)
outimg = cv2.imread("output.png")
gtimg = cv2.imread("groundtruth.png")


# Checking output image on different rgb scales
# for i in range(30) :
#     print(outimg[i+200, i+500])


for i in range(gtimg.shape[0]):
    for j in range(gtimg.shape[1]):
        if gtimg[i,j,1] == 1 :
            origimg[i, j, 2] = 255          #if groundtruth is 1, turn the green band to max value
        if outimg[i, j ,2] >100:
            origimg[i, j, 0] = 255          #if outimg is > 100  pm the blue scale, turn the blue band in the original image to max


cv2.imwrite('intersectui.png',origimg)
