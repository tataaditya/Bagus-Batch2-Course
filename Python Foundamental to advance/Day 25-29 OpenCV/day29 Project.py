# asikk ngeproject

import cv2 # Kita gunakan untuk membuka kamera
import mediapipe as mp # Untuk Mendeteksi tangan tangan kita
from math import hypot # untuk mencari sisi miring saat mencerahkan atau meredupkan
import screen_brightness_control as sbc
import numpy as np #interpolasi


camera = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    status, frame = camera.read() #BGR
    # convert ke RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    lm_list = []
    if result.multi_hand_landmarks: # kalau kosong [] - > False, kalau isi [nilai] -> True
        for handlandmark in result.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h , w, _ = frame.shape
                cx = int(lm.x*w)
                cy = int(lm.y*h)
                lm_list.append([id,cx,cy]) 

                mpDraw.draw_landmarks(frame,handlandmark,mphands.HAND_CONNECTIONS)

    if lm_list != []:
        x1 = lm_list[4][1]
        y1 = lm_list[4][2]
        x2 = lm_list[8][1]
        y2 = lm_list[8][2]
        # cv2.circle(frame, (x1,y1), 4, (255,0,0), thickness= -1)
        cv2.circle(frame, (x1,y1), 4, (255,0,0), thickness= -1)
        cv2.line(frame, (x1,y1), (x2,y2), (255,0,0), thickness= 3)
        
        hypotenuse = hypot(x2-x1, y2-y1)
        bright = np.interp(hypotenuse, [15,200],[0,100]) #200 = 100%, 15 = 0%
        print(bright, hypotenuse)

        # kita gunakan sbc
        sbc.set_brightness(int(bright))

   
    cv2.imshow('Screen Brightness Control', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 

camera.release()
cv2.destroyAllWindows

