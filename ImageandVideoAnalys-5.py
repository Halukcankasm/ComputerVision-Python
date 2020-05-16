import cv2
import numpy as np

img1 = cv2.imread('resim.jpg')
img2 = cv2.imread('Disney.jpg')

# #add = img1 + img2
# """
# İki görüntününde boyutlarının aynı olmak zorunda
# """

# #add = cv2.add(img1,img2)
# """
# iki görüntüyü birleştirdik fakat çok parlak renk uyumarı iyi değil
# """

# weighted = cv2.addWeighted(img1, 0.8 , img2, 0.5, 0)
# """
# Bu aynı zamanda görüntü eklemesidir,
#  ancak görüntülere farklı ağırlıklar verilir, 
#  böylece bir karıştırma veya şeffaflık hissi verir
# """
# cv2.imshow('weighted',weighted)


rows,cols,channels = img2.shape
"""
görüntünün boyutlarını almak üzereshape komutunu kullanın.
 Ardından, her piksel için genişlik, yükseklik ve kanal sayısını elde etmek üzere
 rows,cols,channels değişkenlerine atayın.
Yukarıdaki örnekte, Kanal Sayısı = 4; Alfa, Kırmızı, Yeşil ve Mavi kanalları temsil eder.
"""

roi = img1[0:rows,0:cols]
"""
img1 in 0:rows,0:cols kordinatlarında bulunan yeri kopyalayıp 'roi' atadık
"""

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
"""
Görüntüyü iyi analiz etmek için gri filtreleme uyguladık
"""

ret,mask = cv2.threshold(img2gray, 220, 255,cv2.THRESH_BINARY_INV)
"""
görüntünün siyah ve beyaz olarak tanımlanmasıdır.
Morfolojik operatörler gibi görüntü üzerindeki gürültüleri azaltmak 
veya nesne belirlemek gibi farklı amaçlar için kullanılır. 
Giriş olarak verilen görüntü üzerinde uygulanan thresholding tipine bağlı olarak, 
pikselleri verilen eşik değerine göre siyah ya da beyaz olarak günceller.
"""
cv2.imshow('MASK',mask)
# Siyah - Beyaz bir görüntü elde ettik

mask_inv=cv2.bitwise_not(mask)
"""
renklerin tam tersini uyguladık
255 demek beyaz demek yani 1 demek , 1 in tersi 0 dır , yani siyah demek
"""
cv2.imshow('mask_inv',mask_inv)

img1_BackGround=cv2.bitwise_and(roi,roi, mask = mask_inv)
"""
Burada and lediğimiz resimler aynı ayni,yani aynı resmi elde edeceğiz 
normal şartlarda beyazlar = 1 , siyahlar = 0 olarak kabul ederek
bitwese and(çarpım), or(toplama),xor(a,notb + nota + b) olarak işlem yapılır
Nurada mask olarak image2 nin gri filtreleme kullandıktan sonra
threshold uygılayatak görüntü üzerinfeki pikseller ile siyah beyaz elde ettiğimiz görüntüyü
resmin üzerine yazdık , fakat beyaz yerler tamamiyle saydam oldu 
mask=maskeleme
mask_inv=tamtersi olacak
"""

img2_fg=cv2.bitwise_and(img2, img2,mask=mask)
"""
Uygulanan maskeleme işleminde 
maskelenen görüntünün beyaz yerleti saydam oluyor ve 
arka kısımda kalan resimin görüntüsünü beyaz yerlerden görebiliyoruz
"""

dst = cv2.add(img1_BackGround , img2_fg)


cv2.imshow('dst', dst)
cv2.imshow('img1_BackGround',img1_BackGround)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows



