import cv2

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("camera", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

