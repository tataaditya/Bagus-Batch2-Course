# Kita akan belajar OpenCV

import cv2


# code dibawah untuk menampilkan foto
# image = cv2.imread(r"Day 25-29 OpenCV\Foto.jpg")

# if image is None:
#     print("Gambar tidak ditemukan")
# else:
#     # kita akan meresize fotonya kalau engga kegedean
#     resize_image = cv2.resize(image, (500,500), interpolation = cv2.INTER_AREA) #Interpolasi kita gunakan untuk men-smoothkan gambar akibat menurunya karena resize
#     cv2.imshow("foto orang ganteng", resize_image)
#     cv2.waitKey(0) #Program berjalan dengan menunggu dengan 2 buah indikator, delay time dan mencet tombol
    
#     cv2.destroyAllWindows()
    
# untuk mengaktifkan / memutar video
video = cv2.VideoCapture(r"Day 25-29 OpenCV\Video.mp4")

while True:
    status, frame = video.read()
    # status = true, ada frame yang diambil
    # frame = Image, 
    
    if not status:
        break
    
    
    cv2.imshow("Video gue", frame)
    cv2.waitKey(15)
    
video.release()
cv2.destroyAllWindows
        