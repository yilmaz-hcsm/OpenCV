import matplotlib.pyplot as plt
import numpy as np
import cv2
path="C:/opencv_udemy/piksel_isleme/OpenCV_Logo.png"
img=cv2.imread(path)
print(img.shape) # width,height,channel(renkli mi?)



(B,G,R)=cv2.split(img)
merged=cv2.merge([B,G,R])
black=np.zeros(img.shape[:2],dtype="uint8")


cv2.imshow("RED",cv2.merge([black,black,R]))#kırmızı hariç tüm renkleri siyaha eşitledik
cv2.imshow("BLUE",cv2.merge([B,black,black]))#mavi hariç tüm renkler siyah
cv2.imshow("GREEN",cv2.merge([black,G,black]))# yeşil hariç tüm renkler siyah
cv2.imshow("opencv",img)
"""
cv2.imshow("OpenCV-Black",black) # tüm değerleri siyah yapar
cv2.imshow("OpenCV-merged",merged) # hepsini birleştirir
cv2.imshow("OpenCV",img) #resmi yazdırır
cv2.imshow("OpenCV-B",B)# blue rengini gizler
cv2.imshow("OpenCV-G",G)# green rengini gizler
cv2.imshow("OpenCV-R",R)#red rengini gizler
"""



cv2.waitKey(0)
cv2.destroyAllWindows()