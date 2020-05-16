import cv2
import numpy as np

cap=cv2.VideoCapture(0)

#Eğer videoyu kaydedeceksek
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame = cap.read()
#ret, = return , yani döndürüp anlık framleri alıp frame eşitliyor
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #ÇERÇEVENİN RENGİNİ FARKLI YAPTIK GRİ
    
    out.write(frame)
    
    cv2.imshow('VideoFrame', frame)
    cv2.imshow('VideoGrayFrame', grayFrame)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()    
