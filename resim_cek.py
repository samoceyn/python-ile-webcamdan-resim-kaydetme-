import cv2
import numpy as np

kamera = cv2.VideoCapture(0)    # pc kamerasını kullan
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,800) # açılan kamera penceresini boyutlandır
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,800)

print(' poz verip resmi kaydetmek için q ya basın')

while True :
    ret , resim = kamera.read() 
    
    cv2.rectangle(resim,(230,70),(650,450),(55,55,55),4)  # kamerada belirtilen koordinatlara dikdörtgen çiz
    cv2.imshow("resim çekim", resim)        # görüntüle
    
    if cv2.waitKey(1) & 0xFF == ord("q"):  
        
        cv2.imwrite('samoceynn.jpg',resim)  # kaydet
        print('kaydedildi')
        break
    
kamera.release()
cv2.destroyAllWindows()   
