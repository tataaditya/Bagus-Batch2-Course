import cv2
# disini bisa load gambar yang konstan
import numpy as np

# ini akan load image dari sistem numpy
image = np.zeros((500,500,3), dtype ='uint8')

# Kita akan menggambar
# line
#cv2.line(image,(50,50),(450,450),(0,255,0),thickness=4)

# circle
# Hafalin aja fungsinya yah.. parameternya ikut instruksi vscode
# cv2.circle(image,(250,250),100,(255,255,255), thickness= 2)

# # ! kalau mau  isi aja thickness jadi -1
# # rectangle
# cv2.rectangle(image, (50, 50), (450, 450), (0, 255, 0), thickness=-1)

# # polygon
# points = np.array([[150,200],[250,100],[350,200]], np.int32)
# points = points.reshape(-1,1,2)

# cv2.polylines(image, [points],isClosed=True, color= (255,255,0), thickness= 3)


# text
image = cv2.imread(r"Day 25-29 OpenCV\Foto.jpg")
resized_image = cv2.resize(image,(500,500),interpolation=cv2.INTER_AREA)
cv2.putText(resized_image,"gue ganteng", (50,50) ,cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),thickness=1)


cv2.imshow("image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows


camera = cv2.VideoCapture(0)

while True:
    sts, frame = camera.read()
    
    if not sts:
        break
    
    
    cv2.line(frame,(50,50),(250,50),(255,255,255), thickness = 2)
    cv2.putText(frame,"gue ganteng", (50,50) ,cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),thickness=1)
    cv2.imshow('Live Camera', frame)
    
    if cv2.waitKey(15) & 0xff == ord('q'):
        break

camera.release()
cv2.destroyAllWindows

