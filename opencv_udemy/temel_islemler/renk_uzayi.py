import cv2

img=cv2.imread("klon.jpg") #bgr
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Klon",img)
cv2.imshow("Klon_rbg",img_rgb)
cv2.imshow("Klon_hsv",img_hsv)
cv2.imshow("Klon_gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()