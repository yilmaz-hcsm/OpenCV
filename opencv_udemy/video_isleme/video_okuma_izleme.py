import cv2

#webcam üzerinden video alma

cap = cv2.VideoCapture(0)#0 olunca kameranı açar.
#başka bir yerden çekmek istersen videoyunun konumunu yazman gerekiyor.


while True:
    ret, frame = cap.read()
    """
    if ret==0:
      break
      #bu komudu kullandığımız zaman video bittiğinde kapanmasına yarıyor.
    """
    frame = cv2.flip(frame,1)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



