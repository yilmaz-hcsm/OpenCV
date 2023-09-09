import cv2
import matplotlib.pyplot as plt
import numpy as np

path="C:/opencv_udemy/piksel_isleme/forest.jpg"
img=cv2.imread(path)

corner=img[0:100,0:250]#[y_start:y_end, x_start:x_end]
img[0:100,0:250]=(255,0,0)# girilen değerleri mavi yap


cv2.imshow("Test",img)
cv2.imshow("Corner",corner)



cv2.waitKey(0)
cv2.destroyAllWindows()