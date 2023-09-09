import cv2
import numpy as np


#amacımız resimlerı yumuşatmak.
img_filter = cv2.imread("C:/opencv_udemy/resmi_netlestirme/filter.png")
img_median = cv2.imread("C:/opencv_udemy/resmi_netlestirme/median.png")
img_bilateral = cv2.imread("C:/opencv_udemy/resmi_netlestirme/bilateral.png")

blur =cv2.blur(img_filter,(11,11))#pozitif tek syı olması gerekiyor.
cv2.imshow("originall",img_filter)
cv2.imshow("blur",blur)


blur_g=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("original2",img_filter)
cv2.imshow("blur2",img_filter)

blur_m = cv2.medianBlur(img_median,5)
cv2.imshow("original",img_bilateral)
cv2.imshow("blur_m",blur_m)

blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)
cv2.imshow("originalll",img_bilateral)
cv2.imshow("blur_b",blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
