import cv2

# Webcam'i başlat
vid = cv2.VideoCapture(0)

# Gülümseme sınıflandırıcısını yükle
smile_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/smile.xml")

# Yüz sınıflandırıcısını yükle
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)  # Görüntüyü yatay olarak çevirin

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Yüz ROI'sini seçin
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Gülümsemeleri algıla
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow('Smile Detection', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalamayı serbest bırak ve pencereleri kapat
vid.release()
cv2.destroyAllWindows()
