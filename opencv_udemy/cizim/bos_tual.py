import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8) +255
#print(canvas) tüm değerleri 0'ken 255 eklersek beyaz bir ekran haline gelir, tüm değerler 255 olur

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()