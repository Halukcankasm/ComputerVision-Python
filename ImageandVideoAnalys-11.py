import cv2
import numpy as np

img_bgr = cv2.imread('image.jpg')
img_gray= cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.70
#Eşik değeri , nesnenin parlaklığına göre ayırt edeceğiz
#eğer değeri düşürürsek parlaklığı az olan resimleride elde edeceğiz
loc = np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr , pt , (pt[0]+w,pt[1]+h) , (0,255,255),2)
    """
    herhangi bir görüntüye dikdörtgen çizmek için kullanılır.
    Parametreler:
image: Dikdörtgenin çizileceği görüntüdür.
start_point: Dikdörtgenin başlangıç ​​koordinatlarıdır.
Koordinatlar, iki değerin tuplesleri olarak temsil edilir ( X koordinat değeri, Y koordinat değeri).
end_point: Dikdörtgenin bitiş koordinatlarıdır.
Koordinatlar, iki değerin tuplesleri olarak temsil edilir ( X koordinat değeri, Y koordinat değeri).
renk: Çizilecek dikdörtgenin kenarlık çizgisinin rengidir. 
BGR için bir demet geçiriyoruz. örneğin: (255, 0, 0) mavi renk için.
kalınlık: Dikdörtgen sınır çizgisinin piksel cinsinden kalınlığıdır.
-1 pikselin kalınlığı dikdörtgen şeklini belirtilen renkle dolduracaktır.
    """
    
cv2.imshow('detected', img_bgr)    
    