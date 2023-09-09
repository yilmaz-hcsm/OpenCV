import cv2

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/eye.xml")

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Yüz bölgesini seçin
        roi_gray = gray[y:y + h, x:x + w]
        roi_frame = frame[y:y + h, x:x + w]

        # Gözleri algılamadan önce burun bölgesini maskeleyin
        roi_gray_nostrils = roi_gray.copy()
        cv2.rectangle(roi_gray_nostrils, (int(w * 0.3), int(h * 0.65)), (int(w * 0.7), h), (0, 0, 0), -1)

        eyes = eye_cascade.detectMultiScale(roi_gray_nostrils, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
