import cv2
import matplotlib.pyplot as plt
import numpy as np

path="C:/opencv_udemy/piksel_isleme/OpenCV_Logo.png"
img=cv2.imread(path)


cv2.imshow("OpenCV",img)
print(img.shape) # width,height,channel(renkli mi?)
#channel-->3 renklidir.
#channel --1 grayscale
print("width: {} pixels".format(img.shape[0]))
print("height: {} pixels".format(img.shape[1]))
print("channel: {} pixels".format(img.shape[2]))

print("image size: {}".format(img.size))
print("data type{}".format(img.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()