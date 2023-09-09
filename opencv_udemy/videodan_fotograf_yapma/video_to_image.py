import cv2
import os

# Video dosyasının adı ve yolu
video_path = "video.mp4"

# Kaydedilecek resimlerin klasörü
output_folder = "frames"

# Klasörü oluştur (varsa yeniden oluşturmayacak)
os.makedirs(output_folder, exist_ok=True)

# Video yakalama nesnesini oluştur
cap = cv2.VideoCapture(video_path)

# Video çerçevesinin genişliği ve yüksekliği
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video çerçevesini saniyede bir kareyle yakala
frame_rate = 1

# Video çerçevesini yakalama hızını ayarla
cap.set(cv2.CAP_PROP_FPS, frame_rate)

# Sayacı başlat
frame_count = 0

# Video'nun her bir karesini işle
while True:
    ret, frame = cap.read()

    # Video sonuna ulaşıldıysa çık
    if not ret:
        break

    # Resmi kaydetmek için dosya adı
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

    # Resmi kaydet
    cv2.imwrite(frame_filename, frame)

    # İşlenen kare sayısını artır
    frame_count += 1

# Video yakalamayı serbest bırak
cap.release()

print(f"{frame_count} resim kaydedildi.")
