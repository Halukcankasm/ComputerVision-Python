import cv2
import numpy as np




img=cv2.imread('image.jpg')
ret,threshold=cv2.threshold(img,12, 255,cv2.THRESH_BINARY)
"""
Eşik değerini 12 ye ayarlayarak aslında elimizde pek ışık sahibi olmayan bir 
fotoğrafa uygun bir değer ayarladın , siyah = 0 , beyaz = 255 , eşik değeri 12,
12 nin altında kalanlar 0 , 12 nin üstünde olan piseller 1 olacak

Fakat yinede ışığın olmadığı görüntülerde istediğimiz anlaşılırlığı
 elde edmiyoruz

"""


image_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Resmi daha iyi analiz etmek için gri filtreleme uyguluyoruz

ret,threshold2=cv2.threshold(image_gray,12, 255,cv2.THRESH_BINARY)
"""
Görüntüye ardından siyah-beyaz renkler ile güncelliyoruz
Fakat yinede istediğimiz anlaşılırlığı elde edemiyoruz
"""

gaus = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 115, 1)
"""
Gaus sayesinde değişen aydınlatma sorunuyla başa çıkacağız.
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
src=gri filtreli resmimiz
maxValue=eşikten büyük tüm piksellere bu maks , yani beyaz
adaptiveMethod=Bu, eşiğin piksel neighborhood nasıl hesaplandığını gösterir
blockSize=neighborhod size
C=eşik değerinden çıkartılan sabit

"""


cv2.imshow('orginal', img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaus', gaus)


cv2.waitKey(0)
cv2.destroyAllWindows
