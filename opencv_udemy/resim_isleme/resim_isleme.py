import cv2
img=cv2.imread("klon.jpg")# cv2.imread("klon.jpg",0) yaparsan görüntü renksiz olur.
#print(img)

#resmin boyutunu manuel olarak değiştirmeye yarar
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

#resmi ekranda göstermeye yarar
cv2.imshow("image",img)

#resmi yazdırmaya yarar.
cv2.imwrite("klon1.jpg",img)

#resmin ekranda kalmasını sağlar
cv2.waitKey(0)

#tüm pencerelerin kapanmasına yarar, tüm projeerinde kullan sıkıntı çıkmasın diye
cv2.destroyAllWindows()

#img=cv2.resize(img,(700,100)) şeklinde resmi boyutlandırabiliriz.