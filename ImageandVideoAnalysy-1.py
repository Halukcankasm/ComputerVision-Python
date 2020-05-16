import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('resim.jpg',0)
#'resim.jpg' = görüntünün adresi
#0=gri filtre

cv2.imshow('image', img)
#'image'=çerçeveismi

cv2.waitKey(0)
#klavye metodu , 0 yazarak klavyeden bir tuşa basılması için bekler

cv2.destroyAllWindows()
#Tüm pencereleri kapatır,içine bir parametre eklersek eklenen pencereyi kap




# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.show()


cv2.imwrite('TomAndJerry.png', img)

