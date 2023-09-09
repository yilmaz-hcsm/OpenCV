import cv2

# Webcam'ı aç
cap = cv2.VideoCapture(0)

# Video dosyası adı ve parametreleri
fileName = "C:/opencv_udemy/webcam.avi"  # İleri eğilimli eğik çizgi veya ters eğik çizgileri kullanabilirsiniz
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frameRate = 30
resolution = (640, 480)

# VideoWriter nesnesini oluştur
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

# Ana döngü
while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kareyi yatay olarak çevir
    frame = cv2.flip(frame, 1)

    # Kareyi video dosyasına yaz
    videoFileOutput.write(frame)

    # Kareyi göster
    cv2.imshow("Webcam Live", frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Video dosyasını serbest bırak
videoFileOutput.release()

# Kamerayı serbest bırak
cap.release()

# Pencereleri kapat
cv2.destroyAllWindows()
