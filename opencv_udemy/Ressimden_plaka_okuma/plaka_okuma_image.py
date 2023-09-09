import cv2
import numpy as np
import pytesseract
import imutils

# Resmi oku
img = cv2.imread("C:\\opencv_udemy\\Ressimden_plaka_okuma\\licence_plate.jpg")

# Resmi gri tona çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için gri tonlu resmi filtrele
filtered = cv2.bilateralFilter(gray, 6, 250, 250)

# Kenarları tespit etmek için Canny kenar algılayıcıyı kullan
edged = cv2.Canny(filtered, 30, 200)

# Resimdeki konturları bul
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)

# Konturları alanlarına göre sırala ve en büyük 10 konturu al
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

# Plaka konturunu saklayacak değişkeni tanımla
screen = None

# En büyük konturu bul ve dört köşeli olduğunu kontrol et
for c in cnts:
   epsilon = 0.018 * cv2.arcLength(c, True)
   approx = cv2.approxPolyDP(c, epsilon, True)
   if len(approx) == 4:
      screen = approx
      break

# Maskeyi oluştur ve plakanın olduğu bölgeyi beyazla doldur
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)

# Maskeyi kullanarak orijinal resmi kırp
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
cropped = gray[topx:bottomx+1, topy:bottomy+1]


#algılanan plakanın okunması için gereken kod satırı.
#text=pytesseract.image_to_string(cropped,lang="eng")
#print("detected text",text)


# İşlenmiş resimleri göster
cv2.imshow("Orijinal Resim", img)
cv2.imshow("Plaka Bölgesi", cropped)
cv2.imshow("Kenar Tespiti", edged)

# Kullanıcının herhangi bir tuşa basmasını bekleyin ve pencereleri kapatın
cv2.waitKey(0)
cv2.destroyAllWindows()
