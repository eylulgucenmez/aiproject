import cv2
import numpy as np

image_path = 'image.jpg' 
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Resim yüklenemedi: {image_path}")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #resmi hsvye çevirdim

lower_red = np.array([97, 70, 0]) # gülün en düşük renk değeri
upper_red = np.array([255, 255, 255])

roseMask = cv2.inRange(hsv, lower_red, upper_red)
BGmask = cv2.bitwise_not(roseMask)
hsv[BGmask > 0, 1] = 0 # bg siyah beyaz olacağından saturationu 0 a çektim
hsv[roseMask > 0, 0] = 135 # mor rengin hue uzayında bu değerde olduğunu buldum

purple_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # resmi hsv den rgb ye çevirdim

output_path = 'sonuc.jpg'
cv2.imwrite(output_path, purple_image) #sonuc.jpg olarak kaydettim.
