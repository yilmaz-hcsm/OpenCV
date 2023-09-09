import cv2
import numpy
import numpy as np
import requests
#IP Webcam'den server oluşturup linki url ye yapışturuyoruz.
url = "http://192.168.1.34:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr=np.array(bytearray(img_resp.content), dtype=np.uint8)
    img=cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
    img=cv2.resize(img,(640,480))

    cv2.imshow("Android Camera",img)

    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()
