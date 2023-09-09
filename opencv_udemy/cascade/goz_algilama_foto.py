import cv2

img = cv2.imread("C:/opencv_udemy/cascade/images/face.png")
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
