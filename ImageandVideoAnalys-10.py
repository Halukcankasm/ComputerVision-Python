import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    _,frame = cap.read()
    
    """
    Kenar algılama, bir resimdeki nesnelerin sınırlarını bulmak için kullanılan bir tekniktir
    ve çıktı olarak binary image verir.
    Genellikle, bu kenarları belirtmek için siyah bir arka plan üzerinde beyaz çizgiler çizeriz
    """
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    edges = cv2.Canny(frame, 100, 100)
    
  
    
    cv2.imshow('orginal',frame)
    cv2.imshow('laplacaia',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

   
    
    

    
    if  cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
cv2.release()    

    