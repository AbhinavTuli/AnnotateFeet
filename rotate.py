#images of foot may not be vertical, this helps in rotating them to make them vertical
import os
import numpy as np
import cv2
img = cv2.imread("/Users/abhinav/Documents/feet/71.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.bitwise_not(gray)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

coords = np.column_stack(np.where(thresh > 0))
#print(coords.size)
angle = cv2.minAreaRect(coords)[-1] #find minimum area rectangle surrounding the foot
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle
#print(angle)

(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite("ab.png",rotated)
