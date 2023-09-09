import cv2
img=cv2.imread("C:/opencv_udemy/cascade/images/face.png")
face_cascade=cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,9)
#ilk paramaetre ölçeklendirme değeri
#ikinci parametre ölçeklendirme değeri
#üçüncü parametre en az kaç yüz algılanınca onaylasın

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #diktorggen çizdirme

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()