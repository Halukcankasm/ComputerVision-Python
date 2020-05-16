import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    _,frame = cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    
    
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,255])
    """
    renk sınırları
    """

    
    
    maske = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame,mask = maske)
    """
     belirtilen sınırlar içindeki renkleri bul ve uygula
    """
    
   
    # #1.yol
    # kernel = np.ones((15,15),np.float32)/225
    # smoothed = cv2.filter2D(res,-1,kernel)
    
    # #2.yol(favori)
    # blur = cv2.GaussianBlur(res, (15,15), 0)
    
    # #3.yol
    # median = cv2.medianBlur(res, 15)
    
    
    # #4.yol
    # bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    # """
    # Bulanıklaştırma , arkadaki gürültüyü azaltmak için kullandık
    # """
    
    
    kernel = np.ones((5,5),np.uint8)
    
    erosion = cv2.erode(maske,kernel,iterations = 1)
    """
    Bu operatör görüntü üzerinde bir aşındırma işlemi uygular.
    Parametrelere göre belirtilen alan içerisindeki pikseller aşındırılır ve
    gürültülü olarak adlandırılan bozuk olan görüntü, gürültüden arındırılarak temizlenir
    """
    dilation = cv2.dilate(maske,kernel,iterations = 1)
    """
    Dilation (Yayma – Genişletme)
    Bu operatör giriş olarak verilen görüntü üzerinde parametreler ile verilen alan 
    içerisindeki sınırları genişletmektedir, bu genişletme sayesinde piksel gurupları büyür ve 
    pikseller arası boşluklar küçülür
    """
    
    opening=cv2.morphologyEx(maske, cv2.MORPH_OPEN, kernel)
    """
    nesnelerin arka tarfındaki küçük deliklerin kapatılması veya
    arka plandaki siyah noktaların kapatılmasında yararlıdır.
    """
    closing=cv2.morphologyEx(maske, cv2.MORPH_CLOSE, kernel)
    """
    nesneleri içindeki küçük deliklerin kapatılması
    veya nesnedeki küçük siyah noktaların kapatılmasında yararlıdır.
    """

    
    
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', maske)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    #cv2.imshow('smoothed', smoothed)
    # cv2.imshow('blur', blur)
    # cv2.imshow('median', median)
    # cv2.imshow('bilateral', bilateral)




    
    if  cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
cv2.release()    

    