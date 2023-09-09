import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

glasses_filter = cv2.imread('glasses_filter.png', -1)
nose_filter = cv2.imread('nose_filter.png', -1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Gözlük filtresinin boyutunu ayarlama
        glasses_width = w
        glasses_height = int(glasses_filter.shape[0] * (glasses_width / glasses_filter.shape[1]))

        # Gözlük filtresini yeniden boyutlandırma
        resized_glasses = cv2.resize(glasses_filter, (glasses_width, glasses_height))

        # Gözlük filtresini görüntüye ekleyin
        glasses_y = int(y + h * 0.25)  # Gözlük pozisyonunu yukarı kaydırma
        for i in range(glasses_height):
            for j in range(glasses_width):
                if glasses_y + i < frame.shape[0] and x + j < frame.shape[1]:
                    if resized_glasses[i, j, 3] != 0:
                        frame[glasses_y + i, x + j] = resized_glasses[i, j, 0:3]

        # Burun filtresinin boyutunu ayarlama ve küçültme
        nose_width = int(w * 0.2)
        nose_height = int(nose_filter.shape[0] * (nose_width / nose_filter.shape[1]))

        # Burun filtresini yeniden boyutlandırma
        resized_nose = cv2.resize(nose_filter, (nose_width, nose_height))

        # Burun filtresini görüntüye ekleme
        nose_y = int(y + h * 0.6)
        nose_x = int(x + w * 0.5 - nose_width / 2)
        for i in range(nose_height):
            for j in range(nose_width):
                if nose_y + i < frame.shape[0] and nose_x + j < frame.shape[1]:
                    if resized_nose[i, j, 3] != 0:
                        frame[nose_y + i, nose_x + j] = resized_nose[i, j, 0:3]

    # Görüntüyü yatayda aynalayarak işlemleri tamamlama
    frame = cv2.flip(frame, 1)
    cv2.imshow('Instagram Filtresi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
