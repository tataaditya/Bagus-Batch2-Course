# import librarynya
import cv2

img = cv2.imread(r"Day 25-29 OpenCV\Foto.jpg")

# kita resize
resized_image = cv2.resize(img,(500, 500), interpolation= cv2.INTER_AREA)

# Ini untuk rotasi sebuah image
# rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)

(h,w) = resized_image.shape[:2] #shape[0], shape[1]

# cropping image
cropped_image = resized_image[150:350,150:350]

# kita mencari titik tengah / titik origin
# center =(w//2, h//2)

# rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
# rotated_image = cv2.warpAffine(resized_image, rotation_matrix,(w,h))

# Conversi warna gambar 
# grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# hsv (hue,saturation,value)
hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_HSV2BGR)

# Pixel Manipulation
pixel = resized_image[100,100]

# Ubah warna pixel
resized_image[100:400,100:400] = [0,0,255]

# flip gambar
flip_horizontal = cv2.flip(resized_image, 1)
flip_vertikal = cv2.flip(resized_image, 0)
flip_both = cv2.flip(resized_image, -1)

# cv2.imshow('Gambar 1', flip_horizontal)
# cv2.imshow("Gambar 2", flip_vertikal) 
cv2.imshow("Gambar 3", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# untuk save
cv2.imwrite(r'Day 25-29 OpenCV\Foto crop.jpg', cropped_image)

# Conversi warna gambar 
# grayscale
