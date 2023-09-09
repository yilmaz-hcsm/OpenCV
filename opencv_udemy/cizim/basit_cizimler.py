import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8) +255

#düz çizgi oluşturmak için
cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)

#dörtgen çimek için
cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),thickness=2)

#içini doldurmak için: kalınlığın başına - ekliyoruz
cv2.rectangle(canvas,(200,200),(400,400),(0,255,0),thickness=-2)

#çember çizmek için
cv2.circle(canvas,(250,250),100,(0,0,255),thickness=1)

#üçgen çizmek için 3 tane çizgi ekleyerek yaapbiliriz.

#5gen 4 gen 6 gen oluşturmak (çokgen) için:
points=np.array([[[110,110],[220,220],[110,400],[220,400],[220,500]]],np.int32)

cv2.polylines(canvas,[points],True,(0,0,100),5)

cv2.ellipse(canvas,(300,300),(80,20),10,90,360,(255,255,0),-1)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()