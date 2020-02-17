#images of foot may not be vertical, this helps in rotating them to make them vertical
import os
import numpy as np
import cv2
def rotateFoot(inputImg,output):
	gray = cv2.cvtColor(inputImg, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	coords = np.column_stack(np.where(thresh > 0))
	angle = cv2.minAreaRect(coords)[-1] #find minimum area rectangle surrounding the foot
	if angle < -45:
		angle = -(90 + angle)
	else:
		angle = -angle
	#print(angle)

	(h, w) = inputImg.shape[:2]
	center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated = cv2.warpAffine(img, M, (w, h),
		flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
	cv2.imwrite(output,rotated)
	
# img = cv2.imread("/Users/abhinav/Documents/Feet Segmentation/Visualizesegmentation/footprint.png")
# rotateFoot(img,"anm.png")

