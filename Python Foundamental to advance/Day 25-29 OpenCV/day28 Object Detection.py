# yey akhirnya kita object detectionqq
import cv2

# thresold (ambang batas)
# "0" disini untuk automatis grey image
image = cv2.imread(r"Day 25-29 OpenCV\Foto.jpg", 0)
resize_image = cv2.resize(image,(500,500), interpolation=cv2.INTER_AREA)

# cv2.threshold (1. parameter, 2 image)
_, threshold = cv2.threshold(resize_image, 127,255, cv2.THRESH_BINARY)

# sekarang kita bikin edge detection
# pakai fungsi cv2.Canny
# kita punya 2 buah threshold disini
image_edge = cv2.Canny(resize_image,100, 200)

# contour
_, threshold = cv2.threshold(resize_image, 127,255, cv2.THRESH_BINARY)
# cv2..findCountour
contours,_ = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# ubah warnanya ke BGR
image_with_contours = cv2.cvtColor(resize_image, cv2.COLOR_GRAY2BGR)

# cv2.drawcontours
cv2.drawContours(image_with_contours, contours, -1, (0,0,0), thickness=1)

# apa fungsi 
# -1, (0,255,0) ?
# -1 untuk menampilkan countours atau garis garis tepi
# (0,255,0) untuk warnanya

# Time to machine Learning object detection model !!
# cascade c;assifier kumpulan model yang siap pakai
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread(r"Day 25-29 OpenCV\Foto.jpg")

resize_image = cv2.resize(image,(500,500), interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resize_image,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(resize_image, scaleFactor= 1.1, minNeighbors=5, minSize=(30,30))

for (x,y,w,h) in face:
    cv2.rectangle(resize_image, (x,y),(x+w,y+h),(255,0,0), thickness=3)


# Bikin versi Video yuk
# Buka video
# video = cv2.VideoCapture("Day 25-29 OpenCV/Video.mp4")

# # Periksa apakah video berhasil dibuka
# if not video.isOpened():
#     print("Error: Video tidak ditemukan!")
# else:
#     while True:
#         # Baca frame per frame
#         ret, frame = video.read()
        
#         # Jika tidak ada frame lagi, hentikan loop
#         if not ret:
#             break

#         # Ubah ke grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Deteksi wajah
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

#         # Gambar kotak di sekitar wajah
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)

#         # Tampilkan hasil
#         cv2.imshow("Deteksi Wajah", frame)

#         # Tekan 'q' untuk keluar dari loop
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

# video.release()
# untuk menampilkan
# cv2.imshow('show', resize_image)

# buat versi kamera skrg
camera = cv2.VideoCapture(0)

while True:
    sts, frame = camera.read()
    
    if not sts:
        break
        
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(frame, scaleFactor= 1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0), thickness=3)
        # cv2.line(frame,(50,50),(250,50),(255,255,255), thickness = 2)
        cv2.putText(frame,"Terdeteksi Ganteng", (x,y-10) ,cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),thickness=2)
    
    cv2.imshow('Live Camera', frame)
    if cv2.waitKey(15) & 0xff == ord('q'):
        break

camera.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
