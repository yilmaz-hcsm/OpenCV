#ROI: region on interest
import cv2
import matplotlib.pyplot as plt
import numpy as np

path="C:/opencv_udemy/piksel_isleme/basketball.jpg"
img=cv2.imread(path)
print("Shape: {}".format(img.shape))

roi=img[100:200, 0:50]
img[300:400,300:350]=roi

cv2.imshow("Basketball",img)
cv2.imshow("Basketball ROI",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()
