import cv2
import numpy as np

image_path = 'image.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Resim yüklenemedi: {image_path}")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask1 | mask2

masked_image = cv2.bitwise_and(image, image, mask=mask)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
background_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

background_gray[mask != 0] = 0

mor = np.zeros_like(image)
mor[:] = [122, 0, 122]

mor_gul = cv2.bitwise_and(mor, mor, mask=mask)

result = background_gray + mor_gul

output_path = 'sonuc.jpg'
cv2.imwrite(output_path, result)

cv2.imshow('Sonuc', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

output_path
