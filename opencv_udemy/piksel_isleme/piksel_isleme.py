import cv2
import numpy as np

path="C:/opencv_udemy/piksel_isleme/OpenCV_Logo.png"
img=cv2.imread(path)
#print(img) görüntü kontrol

#herhangi bir kordinata girmek için
#px=img[10,10]
#print(px)

(b,g,r)=img[50,30]
print("(0,0)- Red: {}, Green: {}, Blue: {}".format(r,g,b))

"""
BGR/RGB
B: 0-255
G: 0-255
R: 0-255
0 - BLACK
255 -WHITE
"""
blue=img[100,100,0]
green=img[100,100,0]
red=img[100,100,0]

print("Before:",img[100,100])
img[100,100]=[100,100,100] #piksel değiştirme
print("Atfer:",img[100,100])

#diğer değiştirme yöntemi
print("RED Value:",img.item(10,10,2))
img.itemset((10,10,2),100)
print("RED Value(after):",img.item(10,10,2))
