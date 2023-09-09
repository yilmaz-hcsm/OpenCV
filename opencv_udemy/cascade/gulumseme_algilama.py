import cv2

# Görüntüyü yükle
img = cv2.imread("C:/opencv_udemy/cascade/images/smile.jpg")

# Yüz sınıflandırıcıyı yükle
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/frontalface.xml")

# Gülümseme sınıflandırıcıyı yükle
smile_cascade = cv2.CascadeClassifier("C:/opencv_udemy/cascade/haar_cascade/smile.xml")

# Görüntüyü gri tonlamalı yap
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Yüzleri algıla
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

# Yüzleri çerçevele ve gülümsemeleri arayın
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Yüz ROI'sini al
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    # Gülümsemeleri algıla
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

    # Gülümsemeleri çerçevele
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

# Sonucu görüntüle
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
