import numpy as np
import cv2

img = cv2.imread('resim.jpg',-1)
cv2.line(img,(0,0),(150,150),(255,255,255),5)
"""
cv2.line(image, start_point, end_point, color, thickness)
#ÇİZGİ
start_point:Başlangıç noktası
end_point:Bitiş noktası
color:renk
thickness:çizginin piksel olarak kalınlığı
"""

cv2.rectangle(img,(0,0),(200,200),(0,255,0),(10))
"""
cv2.rectange(image, start_point, end_point, color, thickness)
#DİKDÖRTGEN
start_point:Başlangıç noktası
end_point:Bitiş noktası
color:renk
thickness:çizginin piksel olarak kalınlığı
"""


cv2.circle(img, (120,120), (20), (0,0,0),-1)
"""
#ÇEMBER
cv2.circle(image, center_coordinates, radius, color, thickness)
center_coordinates:Çemberin merkez noktası
radius:Yarıçap
color:Renk 
thickness:Kalınlık(10)=10 piksel kalılık.
Kalınlık yok ise , içi dolu olacak ise = -1
"""
pts=np.array([[10,5],[50,60],[40,50],[120,50],[6,2]],np.int32)
#Çokgenin noktaları
cv2.polylines(img,[pts],True,(0,255,255),5)
"""
#Çokgen
cv2.polylines(img,[noktalar],isClosed=True,color=(255,0,255),thickness=5)
plt.imshow(img)
"""

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0,130), font, 1, (200,255,255),2,cv2.LINE_AA)



cv2.imshow('clockFrame', img)
cv2.waitKey(0)
cv2.destroyAllWindows










