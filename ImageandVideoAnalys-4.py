#import numpy as np
import cv2
img=cv2.imread('resim.jpg',cv2.IMREAD_COLOR)


jerryImage=img[130:200,230:300]
"""
Göürüntüdeni jerry nin bulunduğu koordinatlar
"""

img[0:70,0:70]=jerryImage
"""
görüntü içerisindeki [0:70,0:70] koordinatlarına jerry nin
görüntüsünü yapıştırıyoruz
"""

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
